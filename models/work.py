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
        self.state = "WORK_AVAILABLE"

    def is_available(self):
        return self.state == "WORK_AVAILABLE"

    def is_finished(self):
        self._is_tasks_already_finished()
        return self.state == "WORK_FINISHED"

    def _is_tasks_already_finished(self):
        for task in self.tasks:
            if not task.is_finished():
                return
        self.state = "WORK_FINISHED"

    def do_task_available(self, time):
        for task in self.tasks:
            if task.is_available() and self.is_available() and task.do_task(time):
                self.state = "WORK_DOING"
                return
            if task.is_doing() and task.change_state_if_has_finished(time):
                self.state = "WORK_AVAILABLE"
                self.is_finished()
                return True
        self.is_finished()

    def __str__(self):
        return f"(Name: {self.name}, tasks: {[task.__str__() for task in self.tasks]}, state: {self.state})"
