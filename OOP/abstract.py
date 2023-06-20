from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self, name) -> None:
        self.name = name
        self.sec = sec 


    @abstractmethod
    def test():
        pass
    
    @staticmethod
    def func():
        return 1


class Male(Human):
    def __init__(self, name) -> None:
        super().__init__(name)

    def test(self):
        print('i am')

    def __str__(self) -> str:
        return self.name
    
    


# h = Human()

m = Male('Vasya')
print(m)