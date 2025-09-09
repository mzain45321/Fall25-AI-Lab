import csv
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

with open("model_base_agent_log.csv", mode= "w", newline= "") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Room", "Current Temperature", "Action", "Previous Action"])
    for room , temp in rooms.items():
       agent.sensor(temp)
       action=agent.actuator()
       print(f" {room}: {temp} => {action}")
       csv_writer.writerow([room, temp, action, agent.previous_action])
