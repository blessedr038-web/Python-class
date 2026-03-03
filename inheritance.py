
class Animal:
    def sound(self):
        print("Animal is making a sound")


#Child/Derived/Sub Class
class Cat(Animal):
    def climb(self):
        print("Cat is climbing a tree")

class Cow(Animal):
    def chew(self):
        print("Cow is chewing grass")

a = Animal()
a.sound()


mycat = Cat()
mycat.climb()
mycat.sound()


mycow = Cow()