import pandas as pd
import plotly.express as px

df = pd.read_csv("Admission_Predict.csv")

fig = px.scatter(df,df["TOEFL Score"],df["GRE Score"],df["Chance of admit"])


fig.show()