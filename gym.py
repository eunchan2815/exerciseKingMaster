import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
df = pd.read_csv('exerciseKingMaster/gym_members_exercise_tracking.csv')
# print(df.isnull(10))
age = df["Age"]
gender = df["Gender"]
weight = df["Weight"]
height = df["height"]
m_pm = df["Max_BPM"]
avg_pm = df["Avg_BPM"]
hours = df["Session_Duration (hours)"]
burned = df["Calories_Burned"]


# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import StandardScaler, LabelEncoder
# from sklearn.metrics import classification_report, accuracy_score

# # 1. 데이터 로드
# file_path = '/mnt/data/gym_members_exercise_tracking.csv'
# df = pd.read_csv(file_path)

# # 2. BMI 열 추가 (새로운 특징)
# df['BMI'] = df['Weight (kg)'] / (df['Height (m)'] ** 2)

# # 3. 범주형 데이터 인코딩 (운동 유형)
# le = LabelEncoder()
# df['Workout_Type_Encoded'] = le.fit_transform(df['Workout_Type'])  # Workout_Type을 숫자로 변환

# # 4. 독립 변수(X)와 종속 변수(y) 정의
# X = df[['Max_BPM', 'Avg_BPM', 'Session_Duration (hours)', 'Calories_Burned', 'BMI']]
# y = df['Workout_Type_Encoded']

# # 5. 데이터 스케일링 (특징 스케일 조정)
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # 6. 학습 데이터와 테스트 데이터로 분할
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# # 7. 모델 정의 및 학습
# clf = RandomForestClassifier(random_state=42)
# clf.fit(X_train, y_train)

# # 8. 예측 및 평가
# y_pred = clf.predict(X_test)

# # 정확도 및 분류 리포트 출력
# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("\nClassification Report:\n", classification_report(y_test, y_pred))

# # 9. 실제 레이블 복원
# y_pred_labels = le.inverse_transform(y_pred)
# y_test_labels = le.inverse_transform(y_test)

# # 10. 샘플 테스트 데이터와 결과 보기
# test_results = pd.DataFrame({
#     'Max_BPM': X_test[:, 0],
#     'Avg_BPM': X_test[:, 1],
#     'Session_Duration (hours)': X_test[:, 2],
#     'Calories_Burned': X_test[:, 3],
#     'BMI': X_test[:, 4],
#     'True Workout_Type': y_test_labels,
#     'Predicted Workout_Type': y_pred_labels
# })

# print("\nSample Results:\n", test_results.head(10))
