class Human:

    # ATTRIBUTES 

    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        print("x")
        
    # METHODS

    def walk(self):
        print(f"{self.name} is walking")

    def study(self):
        print(f"{self.name} is studying in class {self.grade}")

# OBJECTS

yashu = Human("yashu",13)
liki = Human("liki",7)
havi = Human("havi",1)

# CALLING

# yashu.study()
# havi.walk()