class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery 

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged. Battery: {self.battery}%")

    def info(self):
        print(f"📱 {self.brand} {self.model} | Battery: {self.battery}%")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, cooling_system):
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.battery > 10:
            print(f"{self.brand} {self.model} is playing {game} 🎮")
            self.battery -= 10
        else:
            print("Battery too low to play games!")

    def info(self):
        print(f"🎮 {self.brand} {self.model} | Cooling: {self.cooling_system} | Battery: {self.battery}%")

