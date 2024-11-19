import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# CSV 파일 로드
df = pd.read_csv('exerciseKingMaster/gym_members_exercise_tracking.csv')

# 값 대체 및 타입 변환
df["Gender"] = df["Gender"].replace({"Male": 1, "Female": 2}).infer_objects(copy=False)
df["Workout_Type"] = df["Workout_Type"].replace({"Yoga": 1, "HIIT": 2, "Cardio": 3, "Strength": 4}).infer_objects(copy=False)

# 독립 변수와 종속 변수 선택
X = df[["Age", "Gender"]]
Y = df[["Weight (kg)", "Height (m)"]]

# 데이터 분할
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=2)

# 선형 회귀 모델 훈련
lr = LinearRegression()
lr.fit(X_train, Y_train)  # 모델 훈련
