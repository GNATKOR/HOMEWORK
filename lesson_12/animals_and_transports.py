from lesson_12.type import Animal, Transport


class Duck(Animal):
    def voice(self):
        print('quack, quack')

    def move(self):
        print('swims')


class Tiger(Animal):
    def voice(self):
        print('roar!')

    def move(self):
        print('running')


class Car(Transport):
    status = "Not Started"

    def launch(self):
        print('Starting the engine')
        Car.status = "Started"

    def move(self):
        if Car.status == "Started":
            print("Ride")
        else:
            print("Cannot ride, launch first")




