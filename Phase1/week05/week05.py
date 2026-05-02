import pandas as pd

df = pd.read_csv("C:/Users/ivank/Desktop/Ivan/DS učenje/Phase1/week04/patients.csv")

print(df.head(5))

print(df["anxiety_score"].max(), df["anxiety_score"].min(), df["anxiety_score"].mean())

severe_df = df[df["anxiety_score"] >= 15]
print(severe_df)

print(df.describe())