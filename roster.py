#Person class
class Person:

    #constructor 
    def __init__(self, name, age): 
        self.name = name
        self.age = age 

    #get age 
    def get_age(self):
        return self.age
    
    #set age 
    def set_age(self, newAge):
        self.age = newAge
    

#Student class
class Student(Person):

    #constructor
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade 

    #get grade 
    def get_grade(self): 
        return self.grade
    
    #change grade
    def change_grade(self, newGrade):
        self.grade = newGrade
    

#Staff class
class Staff(Person):

    #constructor
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position 

    #getPosition
    def get_position(self):
        return self.position
    

    #change position
    def change_position(self, newPosition): 
        self.position = newPosition


#Roster class
class Roster: 
    
    #no arg constructor that creates an empty list
    def __init__(self):
        self.list = []

    #add someone to the internal list
    def add(self, person): 
        self.list.append(person)
        

    #get's the size of the internal list 
    def size(self):
        return len(self.list) 
    

    #remove a person from the list 
    #uses the object type, person's name, and age to
    #establish equality 
    def remove(self, personToDel):
        #try to find the person that should be removed
        for i in range(0, len(self.list)): 
            if type(self.list[i]) == type(personToDel) and self.list[i].name == personToDel.name and self.list[i].age == personToDel.age:
                #match found
                self.list.pop(i)
                return
        #no match found
        return
    
    def get_person(self, name): 
        #try to find the person that should be removed
        for i in range(0, len(self.list)): 
            if self.list[i].name == name:
                #match found
                return self.list[i]

        #else not found so return None
        return None
    #takes in a single lambda function and runs it on all the people in the internal list
    def map(self, lamduh): 
        
        for person in self.list: 
            lamduh(person)
    