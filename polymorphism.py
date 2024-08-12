class animal:
    def speak():  #abstract method which will be overwritten
        pass

class Dog(animal):
    def speak(self):
        print("barks")



class Cat(animal):
    def speak(self):
        print("meow") 



class Cow(animal):
    def speak(self):
        print("mooo")


dog=Dog()  
cat=Cat()
cow=Cow()

dog.speak()
cat.speak()
cow.speak()