def soma(x: int, y: int, z: float) -> float:
    return x + y + z

print(soma(1, 2, 3))

def teste(x: int, y: float | None = 0) -> float:
    return x + y

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self) -> str:
        return f'{self.firstname} {self.lastname}'
    
def say_my_name(person: Person) -> str:
    return person.full_name

pessoa = Person('Daniel', 'Figueiredo')
print(say_my_name(pessoa))