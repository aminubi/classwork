class theclass():
    def __init__(self, name, age, gender):
        self.name =name
        self.age = age
        self.gender = gender

    def callName(self):
        print("I am: "+self.name )
    def getAge(self):
        print("My Age is:  "+ self.age)

    def getGender(self):
         print("Your gender:  "+ self.gender)

        
thisclass = theclass('Aminu', '35', 'Male')
thisclass.callName()
thisclass.getAge()
thisclass.getGender()
print("=================================")
thisclass1 = theclass('Fatima', '36', 'Female')
thisclass1.callName()
thisclass1.getAge()
thisclass1.getGender()
print("=================================")
thisclass2 = theclass('Umar', '32', 'Male')
thisclass2.callName()
thisclass2.getAge()
thisclass2.getGender()