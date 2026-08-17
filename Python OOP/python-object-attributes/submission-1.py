class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes

attributes = f"{whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}"
print("Initial Attributes: " + attributes)
# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
#  - Increase energy by 2

whiskers.hunger = whiskers.hunger - 3
whiskers.energy = whiskers.energy + 2
attributes = f"{whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}"

# TODO: Print Whiskers' modified attributes
print("Modified Attributes: " + attributes)
