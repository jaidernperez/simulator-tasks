class Machine:
    name: str
    state: str

    def __init__(self, name_p):
        self.name = name_p
        self.set_initial_state()

    def set_initial_state(self):
        # States: MACHINE_AVAILABLE, MACHINE_BUSY
        self.state = "MACHINE_AVAILABLE"

    def set_state(self, state_p):
        self.state = state_p

    def is_available(self):
        return self.state == "MACHINE_AVAILABLE"

    def __str__(self):
        return f"(Name: {self.name}, state: {self.state})"

