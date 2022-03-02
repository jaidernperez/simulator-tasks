class Machine:
    name: str
    state: str

    def __init__(self, name_p):
        self.name = name_p
        self.set_initial_state()

    def set_initial_state(self):
        self.state ="TASK_AVAILABLE"

    def is_available(self):
        if self.task.time_task == 0:
            self.state = "TASK_FINISHED"
        return self.state == "TASK_AVAILABLE"

    def set_state(self, state):
        self.state = state

    def __str__(self):
        return f"(Name: {self.name}, state: {self.state})"
