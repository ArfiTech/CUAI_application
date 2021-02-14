import pandas as pd #dataframe 다루는 모듈인 pandas 불러오기
data_df = pd.read_csv('data.csv') # CSV 파일 불러오기
data_df

import matplotlib.pyplot as plt # 데이터 시각화 모듈인 matplotlib 불러오기

plt.plot(data_df['x'], data_df['y']) # (x좌표, y좌표) 대입, 선 그래프 그리기