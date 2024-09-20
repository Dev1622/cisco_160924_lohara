class Bird:
    def fly(self):
        return 'bird is flying'
class Crow(Bird):
    def fly(self):
        return 'crow is flying'
class Parrot(Bird):
    def fly(self):
        return 'parrot is flying'
class Eagle(Bird):
    def fly(self):
        return 'Eagle is flying'
    
def test_fly(Bird):
    print(Bird.fly())

crow1 = Crow()
parrot1 = Parrot()
parrot2 = Parrot()
Eagle = Eagle()

test_fly(crow1)
test_fly(parrot1)
test_fly(parrot2)
test_fly(Eagle)
