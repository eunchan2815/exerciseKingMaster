import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np

# 데이터 생성
np.random.seed(42)
data = pd.DataFrame({
    'Var1': np.random.rand(100),  # 독립변수 1
    'Var2': np.random.rand(100),  # 독립변수 2
    'Var3': np.random.rand(100),  # 독립변수 3
    'Var4': np.random.rand(100),  # 독립변수 4
    'Target': np.random.rand(100)  # 종속변수
})

print(data.head())



fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 축 설정
sc = ax.scatter(
    data['Var1'], data['Var2'], data['Var3'], 
    c=data['Target'], s=data['Var4']*100, cmap='viridis'
)

# 컬러바 추가
plt.colorbar(sc, label='Target')
ax.set_xlabel('Var1')
ax.set_ylabel('Var2')
ax.set_zlabel('Var3')
plt.title("3D Scatter Plot with Color and Size")
plt.show()