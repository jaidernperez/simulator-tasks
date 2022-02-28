from models.task import Task


class Work:
    name: str
    tasks: list[Task]
    state: str

    def __init__(self, name_p, tasks_p):
        self.name = name_p
        self.tasks = tasks_p
        self.set_initial_state()

    def set_initial_state(self):
        # States: WORK_AVAILABLE, WORK_DOING, WORK_FINISHED
        super()

    def is_available(self):
        super()

    def is_finished(self):
        super()

    def _is_tasks_already_finished(self):
        super()

    def do_task_available(self, time):
        super()

    def __str__(self):
        return f"(Name: {self.name}, tasks: {[task.__str__() for task in self.tasks]}, state: {self.state})"
