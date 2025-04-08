
class Tamagotchi:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.happiness_level = 50
        self.hunger_level = 50
        self.energy_level = 50
        
    def feed (self): 
        self.hunger_level += 10 
        self.energy_level -= 5 
        return f' FEED! {self.name}: hunger = {self.hunger_level}, Energy = {self.energy_level}'
    
    def rest (self):
        """Método que debe ser implementado por cada subclase"""
        raise NotImplementedError("Cada subclase debe implementar su propio método rest()")

        
    
class dog (Tamagotchi):
    
    def __init__(self, name):
        super().__init__(name, 'dog')

    def bark (self): 
        self.happiness_level += 5
        self.energy_level -= 5
        return f'BARK! {self.name}: Happiness = {self.happiness_level}, Energy= {self.energy_level}'
    
    def rest(self):
        self.energy_level += 25
        self.hunger_level -= 15
        return f'REST! {self.name}: Energy = {self.energy_level}, Hunger = {self.hunger_level}'
        
class cat (Tamagotchi):
    
    def __init__(self, name):
        super().__init__(name, 'cat')
        
    def meow (self): 
        self.happiness_level += 3 
        self.energy_level -= 8
        return f'MEOW! {self.name}: Happiness = {self.happiness_level}, Energy = {self.energy_level}'
    
    def rest(self):
        self.energy_level += 15
        self.hunger_level -= 15

class mouse (Tamagotchi):
    
    def __init__(self, name):
        super().__init__(name, 'mouse')
        
    def squeak (self): 
        self.happiness_level += 2
        self.energy_level -= 3
        return f'Squeak! {self.name}: Happiness = {self.happiness_level}, Energy = {self.energy_level}'
    
    def rest(self):
        self.energy_level += 20
        self.hunger_level -= 15
        return f'REST! {self.name}: Energy = {self.energy_level}, Hunger = {self.hunger_level}: '    

def create_tamagotchi():
        name = input("\nNombre del Tamagotchi: ").capitalize().strip()
        species = input("Especie (dog/cat/mouse): ").lower().strip()
        
        if species == "dog":
            pet = dog(name, species)
        elif species == "cat":
            pet = cat(name, species)
        elif species == "mouse":
            pet = mouse(name, species)
        else:
            print("Especie inválida")
        
        self.tamagotchis.append(pet)
        print(f"{pet.name} creado!")

def show_status(pet):
        print(f"\nEstado de {pet.name}, {pet.species}")
        print(f"- Felicidad: {pet.happiness_level}")
        print(f"- Hambre: {pet.hunger_level}")
        print(f"- Energía: {pet.energy_level}")
        
create_tamagotchi()