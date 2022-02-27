import pandas as pd

dataframe = pd.read_csv("../data/data.csv")

columns = [i for i in dataframe.columns]
machines = columns[1:len(columns)]
works = dataframe['works']

print(f"Dataframe:\n{dataframe.head()}\n")
print(f"Row 1:\n{dataframe.loc[0]}\n")
print(f"Index:\n{dataframe.columns}\n")
print(f"Machines:\n{machines}\n")
print(f"Workslll:\n{works}\n")
