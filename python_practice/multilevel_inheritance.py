class School:
    def display_school(self):
        print("This is a school")

class UG(School):
    def display_UG(self):
        print("This is a UG")

class PG(UG):
    def display_PG(self):
        print("This is a PG")

def main():
    school = School()
    school.display_school()
    ug = UG()
    ug.display_school()
    ug.display_UG()
    pg = PG()
    pg.display_school()
    pg.display_UG()
    pg.display_PG()

main()