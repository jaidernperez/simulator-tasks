import pandas as pd

from models.machine import Machine
from models.task import Task
from models.work import Work


def initialize_works(dataframe_p):
    dataframe_index = [i for i in dataframe_p.index]
    return [Work(dataframe_p.iloc[i_df]['works'],
                 [Task(machine, dataframe_p.iloc[i_df][machine.name]) for machine in machines])
            for i_df in dataframe_index]


dataframe = pd.read_csv("../data/data.csv")

columns = [column for column in dataframe.columns]
machines = [Machine(name_machine) for name_machine in columns[1:len(columns)]]
works = initialize_works(dataframe)
