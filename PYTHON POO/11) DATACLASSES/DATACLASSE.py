from dataclasses import dataclass, field
    
@dataclass
class Person:
    name: str
    lastname: str
    active: bool = False
    addresses: list = field(default_factory=list)
    full_name: str = field(default='MISSING', init=True, compare=True)
    
    def __pos_init__(self):
        self.full_name = f'{self.name} {self.lastname}'
        
if __name__ == '__main__':
    john = Person('John', 'Doe', True, ['R1'], 'JONH DOE')
    MARA = Person('MARA', "MO", True, ['R2'])
    print(john)
    print(MARA)
    print(repr(MARA))
    print(MARA == john)