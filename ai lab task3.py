class ModelBasedReflexAgent:
    def __init__(self, temp):
        self.fixed_temp = temp
        self.previous_action = None
        self.current_temp = None
    def sensor(self, temp):
        self.current_temp = temp
    def performance(self):
        if self.current_temp> self.fixed_temp:
            action = "Turn on the AC"
        else:
            action = "Turn off the AC"
        if action == self.previous_action:
            action = "No change"
        else:
            self.previous_action = action
        return action
    def actuator(self):
        action = self.performance()
        print(self.current_temp, "=> Action:" , action)
rooms = {
    "Living room": 20,
    "Drawing room": 22,
    "Kitchen room": 34,
    "Bed room": 34,

}
agent = ModelBasedReflexAgent(16)
for room , temp in rooms.items():
    print(room, end=" :\t")
    agent.sensor(temp)
    agent.actuator()
    