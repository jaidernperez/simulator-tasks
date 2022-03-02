import pandas as pd

from models.machine import Machine
from models.task import Task
from models.work import Work


def initialize_works(dataframe_p):
    dataframe_index = [i for i in dataframe_p.index]
    return [Work(dataframe_p.iloc[i_df]['works'],
                 [Task(machine, dataframe_p.iloc[i_df][machine.name]) for machine in machines])
            for i_df in dataframe_index]


def recorre_works(time):
    for work in works:
        if work.do_task_available(time):
            return True
    return False


def is_simulation_finished():
    for work in works:
        if not work.is_finished():
            return False
    return True


def get_min_time_doing_works():
    time = 0
    while not is_simulation_finished():
        if not recorre_works(time):
            time = time + 1
    return time


# ---------------------------------------------------------------------------------------------------------------------
dataframe = pd.read_csv("../data/data.csv")

columns = [column for column in dataframe.columns]
machines = [Machine(name_machine) for name_machine in columns[1:len(columns)]]
works = initialize_works(dataframe)

print(f"\nTiempo mínimo de ejecución de todos los trabajos: {get_min_time_doing_works()}\n")
for item in [i for i in works]:
    print(item.__str__(), "\n")
