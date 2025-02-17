import pandas as pd
import numpy as np
import matplotlib.pylab as plt

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = pd.read_csv(r"C:\Users\sayed\PycharmProjects\dataAnalysisWithPython\data\auto.csv", names=headers)

df.replace("?", np.nan, inplace=True)


def print_missingValue():
    missing_data = df.isnull()
    for column in missing_data.columns.values.tolist():
        print(missing_data[column].value_counts())


avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
avg_bore = df["bore"].astype("float").mean(axis=0)
avg_stroke = df["stroke"].astype("float").mean(axis=0)
avg_horsepower = df["horsepower"].astype("float").mean(axis=0)
avg_peak = df["peak-rpm"].astype("float").mean(axis=0)

df["normalized-losses"] = df["normalized-losses"].replace(np.nan, avg_norm_loss)
df["bore"] = df["bore"].replace(np.nan, avg_bore)
df["stroke"] = df["stroke"].replace(np.nan, avg_stroke)
df["horsepower"] = df["horsepower"].replace(np.nan, avg_horsepower)
df["peak-rpm"] = df["peak-rpm"].replace(np.nan, avg_peak)

# replace the missing 'num-of-doors' values by the most frequent
df["num-of-doors"] = df["num-of-doors"].replace(np.nan, "four")

# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)

# print(df['num-of-doors'].value_counts())
# print(df['num-of-doors'].value_counts().idxmax())

print(df.head())
