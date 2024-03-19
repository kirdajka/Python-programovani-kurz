class Faculty:
    def __init__(self, faculty_name, contact_address):
        self.faculty_name = faculty_name
        self.contact_address = contact_address
        self.students = []
    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print("Metodě add_student musí být dán objekt třídy Student.")
    def get_students(self):
        for item in self.students:
            print(item)
class Student:
    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty
    def __str__(self):
        return self.name
fakulta_ekonomicka = Faculty("Fakulta ekonomická", "Hradební 95, Praha")
fakulta_lekarska = Faculty("Fakulta lékařská", "Palachova 130, Praha")
student_1 = Student("Hedvika Novotná", fakulta_ekonomicka)
student_2 = Student("Josef Navrátil", fakulta_ekonomicka)
student_3 = Student("Andrea Malá", fakulta_lekarska)
fakulta_ekonomicka.add_student(student_1)
fakulta_ekonomicka.add_student(student_2)
fakulta_lekarska.add_student(student_3)
address = getattr(student_1, "contact_address", "Adresa neznámá")
print(address)



class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
frantisek = Employee("František Novák", "konstruktér", 25)
attr_name = "name"
print(getattr(frantisek, attr_name, "Unknown Attribute"))