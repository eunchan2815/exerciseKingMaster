import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

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
    
    # 예측된 체중과 키를 출력
    print(f"예측된 체중: {predicted_weight:.2f} kg, 예측된 키: {predicted_height:.2f} m")
    
    similar_user = df[(np.abs(df["Weight (kg)"] - predicted_weight) < 5) & 
                      (np.abs(df["Height (m)"] - predicted_height) < 0.1)]
    
    if similar_user.empty:
        print("비슷한 사용자가 없으므로 기본 운동을 추천합니다.")
        workout_recommendation = "Yoga"
    else:
        workout_type_counts = similar_user["Workout_Type"].value_counts()
        workout_recommendation = workout_type_counts.idxmax()
        
        workout_map = {1: "Yoga", 2: "HIIT", 3: "Cardio", 4: "Strength"}
        print(f"추천된 운동: {workout_map[workout_recommendation]}")
    return workout_recommendation

recommend_workout(30, 2, 60, 1.65)
