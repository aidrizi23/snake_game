# this class is specifcally created to teach inheritance.

class Animal:
    def __init__(self):
        self.legs = 4
        self.race = 'all'

    def talk(self):
        print('animal is talking')


class Fish(Animal):
    def __init__(self):
        super().__init__()
        
    # i can now use every method and attribute of the parent class but there is something else  can do.
    # if i want to change the behaviour of a function i can do this by calling firstly the function of the parent class by the keyword super.
    
    def talk(self):
        super().talk()
        print('doing this underwater')
        # now this method will do everything the talk method of the animal can do but with added functionality
        