import pandas as pd

df = pd.read_csv("C:/Users/ivank/Desktop/Ivan/DS učenje/Phase1/Week06/survey.csv")

print("The shape of this dataframe (rows, columns) is:  ", df.shape)

print(pd.isnull(df).sum())


df_clean_age = df.query("Age >= 18 and Age < 76")

print(df_clean_age["Age"].max())
print(df_clean_age["Age"].min())

#num_rows = len(df_clean_age.index)
print("Number of rows with participants older than 18 and younger than 75: " + str(df_clean_age.shape[0]))


print(df.value_counts(["Gender"]))

print("Proportion of people who sought treatment depending on their self-employment status:\n", df.groupby(["self_employed"]).value_counts(["treatment"]))