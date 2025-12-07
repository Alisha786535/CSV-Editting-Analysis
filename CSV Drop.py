import numpy as np
import pandas as pd
import seaborn as sns
df=pd.read_csv("Final_Marks_Data.csv")
df.isna().sum()
df["Student_ID"].isna().sum()
int(df.shape[0]*70)
int(df.shape[1]*80)
df.dropna(axis=0,thresh=5)
