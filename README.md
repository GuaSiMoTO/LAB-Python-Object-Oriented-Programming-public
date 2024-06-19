# LAB-Python-Object-Oriented-Programming

![](https://user-images.githubusercontent.com/970858/63474771-d6734700-c469-11e9-83bb-9429da563909.png)

## Introduction

> ***Note:*** _This can be a pair programming activity or done independently._

In this exercise, you will create a Tamagotchi life simulator using object-oriented programming in Python. The goal is to design a program that allows interaction with different types of virtual pets, such as dogs, cats, and mice.

![](https://cdn.computerhoy.com/sites/navi.axelspringer.es/public/media/image/2017/10/264903-tamagotchi.jpg?tf=3840x)

Each Tamagotchi will have a name, a species, and various attributes, such as happiness level, hunger level, and energy level. Tamagotchis will be able to perform actions like eating, playing, and resting, which will affect their attributes and mood.

Remember to use the concepts of object-oriented programming, such as classes, inheritance, and methods, to create a modular and reusable solution.

Ready?

## Requirements

- [Learn how to fork this repo](https://guides.github.com/activities/forking/)
- Clone this repo into your `code/labs` folder

---

## Iteration 1

Create a base class called `Tamagotchi` with common attributes and methods for all pets (name, species, happiness level, hunger level, energy level).

## Iteration 2

Create subclasses for each Tamagotchi species (dog, cat, and mouse) that inherit from the base class `Tamagotchi`. Each subclass will have species-specific methods and attributes.

## Iteration 3

Implement methods in the classes to interact with the Tamagotchis, such as feeding, talk (bark, meow or squeak), and resting. These methods should modify the Tamagotchi's attributes and display informative messages.
- **Feed**: increase +10 hunger level, decrease energy level -5 (all species)
- **Bark** (Dogs): increase +5 happiness level, decrease -5 energy level
- **Meow** (Cats): increase +3 happiness level, decrease -8 energy level
- **Squeak** (Mice): increase +2 happiness level, decrease -3 energy level
- **Rest**:
    - Dogs: increase +25 energy level, decrease -15 hunger level
    - Cats: increase +15 energy level, decrease -10 hunger level
    - Mice: increase +20 energy level, decrease -15 hunger level

## Iteration 4

Allow the user to create new Tamagotchis, select an existing Tamagotchi to interact with, and view the current state of a Tamagotchi.

## Iteration 5

Display a menu of options to the user and allow them to choose actions to perform with the Tamagotchis. Implement a main loop that prompts the user for input and executes the corresponding actions until the user decides to exit the program.

## BONUS Iterations

### Iteration 6: Decay Over Time

Implement a feature where the stats of each Tamagotchi gradually decrease over time. For example, every minute, the energy level drops, the hunger level increases, and the happiness level decreases. This should happen even if the user is not interacting with the Tamagotchi.

### Iteration 7: Alerts

Add alerts that notify the user whenever one of the Tamagotchi's levels (happiness, hunger, or energy) drops below 20. This can prompt the user to take immediate action to care for their Tamagotchi.

### Iteration 8: Enhanced Interactions

Introduce new actions such as:
- **Play**: Increase happiness significantly but decrease energy.
- **Clean**: Clean the Tamagotchi, improving a new "cleanliness" attribute.
- **Health Check**: Show the Tamagotchi's overall health status based on its current attributes.

## Súper Bonus

### Iteration 9: Enhanced Interactions

Create a graphical user interface (GUI) for the Tamagotchi simulator.

---

## Submission

Upon completion, run the following commands:

