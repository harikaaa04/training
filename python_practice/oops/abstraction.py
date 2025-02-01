from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass 

    @abstractmethod
    def set_pancard(self):
        pass

    def show(self):
        print("Concrete method")

class Son(Father):
    def disp(self):
        print("Son's implementation of method")

    def set_pancard(self, pancard):
        self.pancard = pancard 
        

class Daughter(Father):
    def disp(self):
        print("Daughter's implementation of method")
    
    def set_pancard(self, pancard):
        self.pancard = pancard 

class Relative(Father):
    pass 


def main():
    son = Son()
    son.disp()
    son.show()
    son.set_pancard(123)
    print(f"Son's pancard: {son.pancard}")
    
    daughter = Daughter()
    daughter.disp()
    daughter.show()
    daughter.set_pancard(456)
    print(f"Daughter's pancard: {daughter.pancard}")

    # relative = Relative() 

 
main()