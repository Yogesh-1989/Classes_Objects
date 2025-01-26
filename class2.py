class Animal():
  def __init__(self, name, pet, sound):
    self.name = name
    self.pet = pet
    self.sound = sound
    
  def speak(self):
    print(self.sound)
  
  def pet_info(self):
    print("My", self.pet, "has the name", self.name, "they make the sound", self.sound)
    
    
dog = Animal("champ", "Dog", "woof woof")
cat =Animal("toby", "cat", "meow meow")
      
    
dog.speak()
cat.speak()

dog.pet_info()
cat.pet_info()