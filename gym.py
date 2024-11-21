import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
import form
import os
import graph

df = pd.read_csv('exerciseKingMaster/gym_members_exercise_tracking.csv')

# 데이터 전처리
df["Gender"] = df["Gender"].replace({"Male": 1, "Female": 2}).astype(int)
df["Workout_Type"] = df["Workout_Type"].replace({"Yoga": 1, "HIIT": 2, "Cardio": 3, "Strength": 4}).astype(int)

# 나이, 성별, 몸무게, 키에 따라 운동 종목을 추천하는 모델
X2 = df[["Age", "Gender", "Weight (kg)", "Height (m)"]]
Y2 = df["Workout_Type"].values
# 1차원 배열로 변환

X2_train, X2_test, Y2_train, Y2_test = train_test_split(X2, Y2, test_size=0.05, random_state=2)
exLr = LogisticRegression(max_iter=1000)
exLr.fit(X2_train, Y2_train)

def recommend_workout(age, gender, weight, height):
    if age < min(df["Age"]) or age > max(df["Age"]):
        raise ValueError("입력된 나이가 데이터 범위를 벗어났습니다.")
    if weight < min(df["Weight (kg)"]) or weight > max(df["Weight (kg)"]):
        raise ValueError("입력된 몸무게가 데이터 범위를 벗어났습니다.")
    if height < min(df["Height (m)"]) or height > max(df["Height (m)"]):
        raise ValueError("입력된 키가 데이터 범위를 벗어났습니다.")
    
    recommand = exLr.predict([[age, gender, weight, height]])[0]
    workout_map = {1: "Yoga", 2: "HIIT", 3: "Cardio", 4: "Strength"}
    print(f"추천된 운동: {workout_map[recommand]}")
    graph.showExercise3D(df[df["Workout_Type"] == recommand], workout_map[recommand])
    graph.showPairPlot(pd.DataFrame(df[["Age", "Gender", "Weight (kg)", "Height (m)", "Workout_Type"]]))

bodyInfoQuestions = [
    form.Question("성별", "안녕하세요. 당신의 성별을 알려주세요.", ["남성", "여성"] ),
    form.Question("나이 ", "나이를 입력해주세요.", [] ),
    form.Question("키", "키(cm)를 알려주세요.", [] ),
    form.Question("몸무게", "몸무게(kg)를 알려주세요.", [] ),
    form.Question("이름", "이름이 무엇인가요?", [] ),]
bodyInfoForm = form.Form("정보 조사", bodyInfoQuestions)
bodyInfoForm.StartQuestion()

# 결과 출력
os.system("clear")
recommend_workout(
    int(bodyInfoForm.GetAnswerData(1)),
    int(bodyInfoForm.GetAnswerData(0)),
    int(bodyInfoForm.GetAnswerData(3)),
    float(bodyInfoForm.GetAnswerData(2))
)
