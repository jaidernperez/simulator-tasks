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
        self.state = "TASK_AVAILABLE"

    def is_available(self):
        if self.time_task == 0:
            self.state = "TASK_FINISHED"
        return self.state == "TASK_AVAILABLE"

    def is_doing(self):
        return self.state == "TASK_DOING"

    def is_finished(self):
        return self.state == "TASK_FINISHED"

    def do_task(self, time_p):
        if self.machine.is_available():
            self.state = "TASK_DOING"
            self.machine.set_state("MACHINE_BUSY")
            self.start_time = time_p
            self.end_time = self.time_task + time_p
            return True
        return False

    def change_state_if_has_finished(self, time_p):
        if time_p >= self.end_time:
            self.state = "TASK_FINISHED"
            self.machine.set_state("MACHINE_AVAILABLE")
            return True
        return False

    def __str__(self):
        return f"(Machine: {self.machine.__str__()}, time_task: {self.time_task}, state: {self.state}," \
               f" start time: {self.start_time}, end_time: {self.end_time})"

