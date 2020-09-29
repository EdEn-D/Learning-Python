class Enemy:

    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
bobsfog = Enemy(69)

jason.get_energy()
bobsfog.get_energy()