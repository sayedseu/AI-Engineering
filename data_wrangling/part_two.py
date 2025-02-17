import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)

df = pd.read_csv(r"C:\Users\sayed\PycharmProjects\dataAnalysisWithPython\data\laptop_pricing.csv", header=0)

df.replace("?", np.nan, inplace=True)

avg_weight = df["Weight_kg"].astype("float").mean(axis=0)
df["Weight_kg"] = df["Weight_kg"].replace(np.nan, avg_weight)

df['Screen_Size_cm'] = np.round(df['Screen_Size_cm'], 2)
common_screen_size = df['Screen_Size_cm'].value_counts().idxmax()
df['Screen_Size_cm'] = df['Screen_Size_cm'].replace(np.nan, common_screen_size)

# Data standardization: convert weight from kg to pounds
df["Weight_kg"] = df["Weight_kg"] * 2.205
df.rename(columns={'Weight_kg': 'Weight_pounds'}, inplace=True)

# Data standardization: convert screen size from cm to inch
df["Screen_Size_cm"] = df["Screen_Size_cm"] / 2.54
df.rename(columns={'Screen_Size_cm': 'Screen_Size_inch'}, inplace=True)

df['CPU_frequency'] = df['CPU_frequency'] / df['CPU_frequency'].max()

bins = np.linspace(min(df["Price"]), max(df["Price"]), 4)
group_names = ['Low', 'Medium', 'High']
df['Price-binned'] = pd.cut(df['Price'], bins, labels=group_names, include_lowest=True)

# Indicator Variable: Screen
dummy_variable_1 = pd.get_dummies(df["Screen"])
dummy_variable_1.rename(columns={'IPS Panel': 'Screen-IPS_panel', 'Full HD': 'Screen-Full_HD'}, inplace=True)
df = pd.concat([df, dummy_variable_1], axis=1)

# drop original column "Screen" from "df"
df.drop("Screen", axis=1, inplace=True)

print(df.head(10))


def show_price_graph():
    plt.bar(group_names, df["Price-binned"].value_counts())
    plt.xlabel("Price")
    plt.ylabel("count")
    plt.title("Price bins")
    plt.show()


def print_missingValue():
    missing_data = df.isnull()
    for column in missing_data.columns.values.tolist():
        print(missing_data[column].value_counts())
        print("\n")
