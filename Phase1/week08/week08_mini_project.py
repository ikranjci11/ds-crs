import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from pylab import savefig

#loading the data and setting the parent directory
script_dir = Path(__file__).parent
df_meta = pd.read_spss(script_dir / "ipsos-w4.sav")
df = pd.read_csv(script_dir / "ipsos-w4.csv", na_values=" ")

#Intial inspection of the data
print(df.head())
print(df.shape)
print(df.dtypes)
print(pd.isnull(df).sum())

#delete cases with missing values
df = df.dropna()


#cleaning descriptive statistics variables
df.rename(columns= {"s.age.t4" : "Age", "s.gen.t4" : "Gender", "s.inc.t4" : "Household Income"}, inplace=True)
df["Gender"] = df["Gender"].astype(str)
df["Household Income"] = df["Household Income"].astype(str)



#label gender and income values
df.loc[df["Gender"] == "1.0", "Gender"] = "Male"
df.loc[df["Gender"] == "2.0", "Gender"] = "Female"
df.loc[df["Gender"] == "3.0", "Gender"] = "Other"
df.loc[df["Household Income"] == "1.0", "Household Income"] = "Less than 400€"
df.loc[df["Household Income"] == "2.0", "Household Income"] = "More than 400€, but less than 600€"
df.loc[df["Household Income"] == "3.0", "Household Income"] = "More than 600€, but less than 1400€"
df.loc[df["Household Income"] == "4.0", "Household Income"] = "More than 1400€, but less than 2000€"
df.loc[df["Household Income"] == "5.0", "Household Income"] = "More than 2000€"



#calculating total adjustment disorder symptoms and sever adjustment disorder symptoms
df["Adjustment Disorder"] = df["ad.1.t4"] + df["ad.2.t4"] + df["ad.3.t4"] + df["ad.4.t4"] + df["ad.5.t4"] + df["ad.6.t4"] + df["ad.7.t4"] + df["ad.8.t4"]
df["Severe AjD"] = df["Adjustment Disorder"] >= 18.5
df["Severe AjD"] = df["Severe AjD"].astype(str)
df.loc[df["Severe AjD"] == "True", "Severe AjD"] = "Yes"
df.loc[df["Severe AjD"] == "False", "Severe AjD"] = "No"



#check for inconsistent or invalid values
print(df["Age"].max())
print(df["Age"].min())
print(df["Adjustment Disorder"].max())
print(df["Adjustment Disorder"].min())
print(df["Adjustment Disorder"].value_counts())
print(df.describe())


#summary statistics and analytics
print("Average age of the participants is: " ,df["Age"].mean().round(2))
print("The average result on the ADNM-8 scale measuring Adjustment Disorder symptoms is: " ,df["Adjustment Disorder"].mean().round(2))
print("The number of aprticipants with severe Ajd symptoms (over 18.5) is: ", df["Severe AjD"].value_counts().loc["Yes"])
print("Proportion of participants with severe AjD symptoms depending on their household income:\n", df.groupby(["Household Income"]).value_counts(["Severe AjD"]))
print("Proportion of participants with severe AjD symptoms depending on their gender:\n", df.groupby("Gender")["Severe.AjD"].value_counts(normalize=True).mul(100).rename("percent").reset_index())

#statistics plots
sns.histplot(x="Age", data=df)
plt.title("Figure 1. Histogram for variable Age (N=994).")
plt.savefig(script_dir / "Age histogram.png", bbox_inches="tight")
plt.clf()

sns.histplot(x="Adjustment Disorder", data=df)
plt.title("Figure 2. Histogram for variable Adjustment Disorder (N=994).")
plt.savefig(script_dir / "AjD histogram.png", bbox_inches="tight")
plt.clf()

sns.countplot(x="Severe AjD", hue= "Gender", data=df, stat="percent", multiple="dodge", shrink=0.8)
plt.title("Figure 3. Proportion of participants with severe AjD symptoms depending on their gender (N=994).")
plt.savefig(script_dir / "Gender and severity countplot.png", bbox_inches="tight")
plt.clf()

sns.boxplot(x="Adjustment Disorder", y="Household Income", palette="twilight", data=df, 
            order=["Less than 400€", "More than 400€, but less than 600€", "More than 600€, but less than 1400€", "More than 1400€, but less than 2000€", "More than 2000€"])
plt.title("Figure 4. Distributions of AjD symptoms for participants \n with varying household incomes (N=994).")
plt.savefig(script_dir / "Income and AjD symptoms boxplots.png", bbox_inches="tight")
plt.clf()
