class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        print(f"Creating pet: {self.name}")

    def eat(self):
        print(f"{self.name} is eating now...")
        if self.hunger > 0:
            self.hunger -= 3
            if self.hunger < 0:
                self.hunger = 0
            self.happiness += 1
            if self.happiness > 10:
                self.happiness = 10

    def sleep(self):
        print(f"{self.name} is sleeping...")
        if self.energy < 10:
            self.energy += 5
            if self.energy > 10:
                self.energy = 10

    def play(self):
        print(f"{self.name} is playing...")
        if self.energy >= 2:
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1
            if self.happiness > 10:
                self.happiness = 10
            if self.hunger > 10:
                self.hunger = 10

    def teach_trick(self, trick):
        self.tricks.append(trick)
    
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} doesn't know any tricks yet!")


    def get_status(self):
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks}")



my_pet = Pet("Max")
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.teach_trick("sit down")
my_pet.teach_trick("play dead")
my_pet.get_status()
