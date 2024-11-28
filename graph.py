import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcl
import pandas as pd
import seaborn as sns
import numpy as np

def showExercise3D(data, type, mainData):

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    colors = [
        (0,0,1), ## 컬러바 가장 옅은쪽
        (0,1,0),
        (1,1,0),
        (1,0,0) ## 컬러바 가장 진한쪽
    ]
    cmap = mcl.LinearSegmentedColormap.from_list('my_cmap', colors, gamma=2)


    # 축 설정
    sc = ax.scatter(
        mainData['Age'], mainData['Weight (kg)'], mainData['Height (m)'], 
        c=mainData['Workout_Type'], cmap=cmap
    )


    # 컬러바 추가
    plt.colorbar(sc, label='Workout Type')
    ax.set_xlabel('Age')
    ax.set_ylabel('Weight (kg)')
    ax.set_zlabel('Height (m)')
    plt.title(type + " exercisers data scatter plot")
    plt.show()


def showPairPlot(dataframe):
    sns.pairplot(dataframe, diag_kind='kde', markers='o', plot_kws={'alpha' : 0.05})
    plt.show()



df = pd.read_csv('exerciseKingMaster/gym_members_exercise_tracking.csv')


df["Gender"] = df["Gender"].replace({"Male": 1, "Female": 2}).astype(int)
df["Workout_Type"] = df["Workout_Type"].replace({"Yoga": 1, "HIIT": 2, "Cardio": 3, "Strength": 4}).astype(int)

yogaDf = df[df["Workout_Type"] == 1]
HIITDf = df[df["Workout_Type"] == 2]
Cardio = df[df["Workout_Type"] == 3]
Strength = df[df["Workout_Type"] == 4]
