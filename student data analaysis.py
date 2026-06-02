
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:\\Users\\blaks\\Downloads\\data set.csv")

df.head()
df.info()
df.describe()
df.isnull().sum()
df = df.dropna()
df[['Math_Score','Science_Score','English_Score']].mean()
sns.barplot(x='Gender', y='Math_Score', data=df)
plt.show()
df.groupby('Gender')['Math_Score'].mean()
sns.barplot(x='Gender', y='Math_Score', data=df)
plt.show()
sns.histplot(df['Math_Score'])
plt.show()
sns.scatterplot(x='Science_Score', y='Math_Score', data=df)
plt.title("Science vs Math Score")
plt.show()
