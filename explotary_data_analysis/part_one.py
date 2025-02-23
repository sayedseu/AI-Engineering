import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)

df = pd.read_csv(r"C:\Users\sayed\PycharmProjects\dataAnalysisWithPython\data\automobileEDA.csv", names=None)


def showCorelation(relations):
    corelation = df[relations].corr()
    print(corelation)


def showEngineSizeAndPriceScatterplot():
    sns.regplot(x="engine-size", y="price", data=df)
    plt.ylim(0, )
    plt.show()


def showHighwayMpgAndPriceScatterplot():
    sns.regplot(x="highway-mpg", y="price", data=df)
    plt.ylim(0, )
    plt.show()


def showPeakRpmAndPriceScatterplot():
    sns.regplot(x="peak-rpm", y="price", data=df)
    plt.ylim(0, )
    plt.show()


def showBodyStyleAndPrice():
    sns.boxplot(x="body-style", y="price", data=df)
    plt.show()


# showCorelation(['engine-size', "highway-mpg", "peak-rpm", "price"])
#
# print("\n")

print(df.describe(include=['object']))


