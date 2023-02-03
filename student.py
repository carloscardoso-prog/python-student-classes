from classStudent import Student # from file, import the class

student1 = Student("Jim", "Business", 3.1, False) 
student2 = Student("Jim12312312321312", "Business", 3.9, False)

print(student1.name)
print(student2.name)

print(student1.on_honor_roll())

print(student2.on_honor_roll())