import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import form
import os
import graph

df = pd.read_csv('exerciseKingMaster/gym_members_exercise_tracking.csv')


df["Gender"] = df["Gender"].replace({"Male": 1, "Female": 2}).astype(int)
df["Workout_Type"] = df["Workout_Type"].replace({"Yoga": 1, "HIIT": 2, "Cardio": 3, "Strength": 4}).astype(int)



X = df[["Age", "Gender"]]
Y = df[["Weight (kg)", "Height (m)"]]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=2)
lr = LinearRegression()
lr.fit(X_train, Y_train)


def recommend_workout(age, gender, weight, height):
    input_data = pd.DataFrame([[age, gender]], columns=["Age", "Gender"])
    predicted_values = lr.predict(input_data)
    
    predicted_weight, predicted_height = predicted_values[0]
    
    similar_user = df[(np.abs(df["Weight (kg)"] - predicted_weight) < 5) & 
                      (np.abs(df["Height (m)"] - predicted_height) < 5)]
    
    isDataSuccess = True;
    if (age < min(df["Age"]) or age > max(df["Age"])):
        isDataSuccess = False;

    if similar_user.empty:
        print("비슷한 사용자가 없으므로 기본 운동을 추천합니다.")
        workout_recommendation = "Yoga"
    elif (not isDataSuccess):
        print("닌 운동하지 마세요")
    else:
        workout_type_counts = similar_user["Workout_Type"].value_counts()
        workout_recommendation = workout_type_counts.idxmax()
        print(f"평균 체중: {predicted_weight:.2f} kg, 평균 키: {predicted_height:.2f} m")
        workout_map = {1: "Yoga", 2: "HIIT", 3: "Cardio", 4: "Strength"}
        print(f"추천된 운동: {workout_map[workout_recommendation]}")
        graph.showExercise3D(df[df["Workout_Type"] == int(workout_recommendation)], workout_map[workout_recommendation])
    return workout_recommendation


bodyInfoQuestions = [
    form.Question("성별", "안녕하세요. 당신의 성별을 알려주세요.", ["남성", "여성"] ),
    form.Question("나이 ", "나이를 입력해주세요.", [] ),
    form.Question("키", "키(cm)를 알려주세요.", [] ),
    form.Question("몸무게", "몸무게(kg)를 알려주세요.", [] ),
    form.Question("이름", "이름이 무엇인가요?", [] ),]

bodyInfoForm = form.Form("정보 조사", bodyInfoQuestions)
bodyInfoForm.StartQuestion()


os.system("clear")
recommend_workout(int(bodyInfoForm.GetAnswerData(1)), int(bodyInfoForm.GetAnswerData(0)), int(bodyInfoForm.GetAnswerData(3)), int(bodyInfoForm.GetAnswerData(2)))

