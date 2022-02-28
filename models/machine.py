class Machine:
    name: str
    state: str

    def __init__(self, name_p):
        self.name = name_p
        self.set_initial_state()

    def set_initial_state(self):
        # States: MACHINE_AVAILABLE, MACHINE_BUSY
        super()

    def set_state(self, state_p):
        super()

    def is_available(self):
        super()

    def __str__(self):
        return f"(Name: {self.name}, state: {self.state})"
