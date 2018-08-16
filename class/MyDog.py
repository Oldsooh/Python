from dog import Dog

class MyDog(Dog):
    def __init__(self, name, age):
        super().__init__( name, age)

    def sit(self):
        print(self.name + ' has already sit down!')

    def play_ball(self):
        print(self.name.title() + ' is playing ball.')