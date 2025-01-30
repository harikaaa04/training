class Student:
    def __init__(self, name):
        self._name = name 
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        self._name = value 

def main():
    s1 = Student("harika")
    s2 = Student("mahitha")
    s3 = Student("hima")
    
    l1 = [s1, s2, s3]
    print(f"Objects: {l1}")
    l2 = [s1.name, s2.name, s3.name]
    print(f"Names: {l2}")

main()