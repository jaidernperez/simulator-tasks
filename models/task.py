from models.machine import Machine


class Task:
    machine: Machine
    time_task: int
    state: str
    start_time: int
    end_time: int

    def __init__(self, machine_p, time_task_p):
        self.machine = machine_p
        self.time_task = time_task_p
        self.start_time = 0
        self.end_time = 0
        self.set_initial_state()

    def set_initial_state(self):
        # states: TASK_AVAILABLE, TASK_DOING, TASK_FINISHED
        super()

    def is_available(self):
        super()

    def is_doing(self):
        super()

    def is_finished(self):
        super()

    def do_task(self, time_p):
        super()

    def change_state_if_has_finished(self, time_p):
        super()

    def __str__(self):
        return f"(Machine: {self.machine.__str__()}, time_task: {self.time_task}, state: {self.state}," \
               f" start time: {self.start_time}, end_time: {self.end_time})"
