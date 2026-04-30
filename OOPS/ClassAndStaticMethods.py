
class Student:
    school_name="XYZ school"
    pass_mark=50
    def __init__(self, name, roll_no):
        self.name=name
        self.roll_no=roll_no

    def getname(self):
        return self.name

    @classmethod
    def change_school_name(cls, school_name):
        cls.school_name=school_name

    @classmethod
    def add_new_student(cls, detail):
        name, roll_no=detail.split("-")
        return cls(name, roll_no)

    @staticmethod
    def about_school():
        print("School is a place that teach education")

    @staticmethod
    def is_pass(score):
        if score >= Student.pass_mark:
            return "pass"
        else:
            return "Fali"


s1=Student.add_new_student("ranjith-206")
s2=Student("ram", "303")
s1.about_school()
print(s2.school_name)
s1.change_school_name("IIT")
print(s2.school_name)
print(Student.is_pass(30))