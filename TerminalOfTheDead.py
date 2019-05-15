from playsound import playsound
from multiprocessing import Process
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-1-items-and-enemies/

gameOver = False
processList = []
currentRoom = None
previousRoom = None

gameMap = np.random.randint(0,2,size=(10,10))
gameGraph = nx.path_graph(10)
nx.draw(gameGraph)

class Item():
    """The base class for all items"""
    def __init__(self,name,description,weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"{self.name}"

class Action():
    def __init__(self,method,name,hotkey,**kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str(self):
        return f"{self.hotkey}: {self.name}"

class Place(object):
    def __init__(self,name=""):
        self.name = f"Room {name}"
        self.connections = {}
        self.enemies = []
        self.items = []

    def move(self,connection):
        if connection in self.connections.keys:
            previousRoom = currentRoom
            currentRoom = connections[connection]

    def describe(self):
        print(f"""
        You are in {self.name}.
        You see the following items.
        You see the following enemies.
        You see the following possible paths.
        """)

    def __str__(self):
        return f"{self.name}"

def generateRandomPlaces(n=10):
    for i in range(0,n):
        room = Place(name=i)

def userHelp():
    print("""
    You have the following options:
      > "look around"
      > "map"
        """)

def plotMap():
    # plt.imshow(gameMap)
    # plt.show()
    nx.draw(gameGraph)
    plt.show()

class Room(object):
    def __init__(self):
        self.name = "Room 1"

    def lookAround(self):
        print("You see a laptop")

def makeSomeNoise():
    playsound("city.wav")

room = Room()
item = Item("Screwdriver","A small phillips head screwdriver","0.5")

print("Welcome to: Terminal of the Dead (Jupyter Version)")
print("As the infection spreads outside, you are safely locked inside the bunker.  Fortunate, you think, but not quite fortunate enough.")
print("As the infection spread, you were forced to make decisions.  And your wrong decisions are already catching up with you.")
print("A thud at the door.  Scratching, growling.  Why did you lock yourself in this room?  There's no food in here, no real weapons.  Just one exit.")
while gameOver == False:
    userInput  = input("> ")
    if userInput == "quit" or userInput == "exit":
        for process in processList:
            process.terminate()
        gameOver = True
    elif userInput == "help":
        userHelp()
    elif userInput == "look around":
        room.lookAround()
    elif userInput == "play sound":
        P= Process(name="makeSomeNoise",target=makeSomeNoise)
        processList.append(P)
        P.start()
    elif userInput == "map":
        plotMap()
    elif userInput == "inventory":
        print(item)
    else:
        print(userInput)
