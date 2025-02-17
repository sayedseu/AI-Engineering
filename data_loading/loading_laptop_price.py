import pandas as pd
import numpy as np

data_frame = pd.read_csv(r"C:\Users\sayed\PycharmProjects\dataAnalysisWithPython\data\laptops_train.csv", header=None)

headers = []
for head in data_frame.iloc[0]:
    headers.append(head)

data_frame.drop(index=data_frame.index[0], axis=0, inplace=True)

data_frame.columns = headers

data_frame.replace('?', np.nan, inplace=True)

print(data_frame.info())