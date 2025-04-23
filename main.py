import os
import time

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
        return f'REST! {self.name}: Energy = {self.energy_level}, Hunger = {self.hunger_level}'

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
        return f'REST! {self.name}: Energy = {self.energy_level}, Hunger = {self.hunger_level}'    

def create_tamagotchi():
    os.system('clear')
    name = input("\nNombre del Tamagotchi: ").capitalize().strip()
    species = input("Especie (dog/cat/mouse): ").lower().strip()
    
    if species == "dog":
        pet = dog(name)
    elif species == "cat":
        pet = cat(name)
    elif species == "mouse":
        pet = mouse(name)
    else:
        print("Especie inválida")
        return None
    
    print(f"{pet.name} creado!")
    return pet

def show_status(pet):
        os.system('clear')
        print(f"\nEstado de {pet.name}, {pet.species}")
        print(f"- Felicidad: {pet.happiness_level}")
        print(f"- Hambre: {pet.hunger_level}")
        print(f"- Energía: {pet.energy_level}")
        
def interact_with_pet(pet):
    while True:
        os.system('clear')
        print(f"\n--- Interactuando con {pet.name} ({pet.species}) ---")
        print("1. Alimentar")
        print("2. Hacer ruido")
        print("3. Descansar")
        print("4. Ver estado")
        print("5. Volver al menú principal")
        
        choice = input("Elige una opción: ")
        
        if choice == "1":
            print(pet.feed())
        elif choice == "2":
            if isinstance(pet, dog):
                print(pet.bark())
            elif isinstance(pet, cat):
                print(pet.meow())
            elif isinstance(pet, mouse):
                print(pet.squeak())
        elif choice == "3":
            print(pet.rest())
        elif choice == "4":
            show_status(pet)
        elif choice == "5":
            break
        else:
            print("Opción inválida")
        time.sleep(3)

def main():
    pets = []
    
    while True:
        os.system('clear')
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear nuevo Tamagotchi")
        print("2. Interactuar con Tamagotchi")
        print("3. Salir")
        
        choice = input("Elige una opción: ")
        
        if choice == "1":
            pet = create_tamagotchi()
            if pet:
                pets.append(pet)
        elif choice == "2":
            if not pets:
                print("No hay Tamagotchis creados!")
                time.sleep(2)
                continue
                
            print("\nTamagotchis disponibles:")
            for i, pet in enumerate(pets, 1):
                print(f"{i}. {pet.name} ({pet.species})")
                
            pet_choice = input("Elige un Tamagotchi (número): ")
            try:
                selected_pet = pets[int(pet_choice)-1]
                interact_with_pet(selected_pet)
            except (ValueError, IndexError):
                print("Opción inválida")
        elif choice == "3":
            print("¡Adiós! NO VUELVAS A MOLESTARME")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()

