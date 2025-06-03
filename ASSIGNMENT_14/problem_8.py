# Create a class Vehicle with method start(). Derive class Car and override the
# method start() with additional behavior. Show method overriding.

class Vehicle:
    def __init__(self):
        pass

    def start(self):
        print("Inside Vehicle class")

class Car(Vehicle):
    def __init__(self):
        pass

    def start(self):
        print("Inside car class ")

def main():
    Obj1 = Car()
    Obj2 = Vehicle()

    Obj1.start()
    Obj2.start()

if __name__ == "__main__":
    main()
