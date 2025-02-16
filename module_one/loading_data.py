import pandas as pd
import numpy as np

# "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

df = pd.read_csv("automobile.csv", header=None)

# show the first 5 rows using dataframe.head() method
df.head(5)

# Check the bottom 10 rows of data frame "df"
df.tail(10)

# create headers list
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]
df.columns = headers

# Now, we need to replace the "?" symbol with NaN so the dropna() can remove the missing values:
df1 = df.replace('?', np.nan)

# You can drop missing values along the column "price" as follows:
# Here, axis=0 means that the contents along the entire row will be dropped wherever the entity 'price' is found to
# be NaN

df = df1.dropna(subset=['price'], axis=0)

# Save Dataset
# df.to_csv("automobile.csv", index=False)

# check the data type of data frame "df" by .dtypes
# print(df.dtypes)

# If we would like to get a statistical summary of each column such as count, column mean value, column standard
# deviation, etc., use the describe method:
# print(df.describe())
# print(df.describe(include="all"))
# print(df[['length', 'compression-ratio']].describe())

# This method prints information about a data frame including the index dtype and columns, non-null values and memory
# usage
print(df.info())
