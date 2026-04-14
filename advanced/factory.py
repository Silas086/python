class person:
    pass
class student(person):
    pass
class teacher(person):
    pass
class worker(person):
    pass
class factory():
    def get_person(self,type):
        if type == 'w':
            return worker()
        elif type == 't':
            return teacher()
        else:
            return student()

p1 = factory()
p1.get_person('w')