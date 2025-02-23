import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)

df = pd.read_csv(r"C:\Users\sayed\PycharmProjects\dataAnalysisWithPython\data\automobileEDA.csv", names=None)

hm = 'highway-mpg'
price = 'price'

lm = LinearRegression()

X = df[[hm]]
Y = df[[price]]
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]

lm.fit(Z, Y)

Y_hat = lm.predict(Z)


def showReggPlot():
    sns.regplot(x="peak-rpm", y="price", data=df)
   # sns.regplot(x="highway-mpg", y="price", data=df)
    plt.ylim(0, )
    plt.show()


def showResidualPlot():
    sns.residplot(x=df['highway-mpg'], y=df['price'])
    plt.show()


def showDistributionPlot():
    ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
    sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values", ax=ax1)

    plt.title('Actual vs Fitted Values for Price')
    plt.xlabel('Price (in dollars)')
    plt.ylabel('Proportion of Cars')

    plt.show()
    plt.close()



showDistributionPlot()