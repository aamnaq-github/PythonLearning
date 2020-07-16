from StudentClass.Student import StudentClass

student1 = StudentClass("Jim", "Business", 3.4, False)
student2 = StudentClass("Pam", "Art", 3.1, True)

print(student1.name + " " + str(student1.age()) + " " + str(student1.on_honor_roll()))
print(student2.name + " " + str(student2.age()) + " " + str(student2.on_honor_roll()))