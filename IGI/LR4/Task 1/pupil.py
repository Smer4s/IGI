class Pupil:
    def __init__(self, surname: str, age: int) -> None:
        self.surname = surname
        self.age = age
        
    def determine_age_category(self):
        """
        Determines age_category of a Pupil (junior, middle, senior)
        """    
        if self.age <= 10:
            return "junior"
        if self.age >=11 and self.age <= 15:
            return "middle"
        if self.age >=16:
            return "senior"
        
    @staticmethod
    def create_pupils_from_dict(data: dict[str,int]):
        """
        Creates Pupil objects from a dictionary.
        """
        products = []
        for name, age in data.items():
            products.append(Pupil(name, age))
            
        return products
    
    
    def __repr__(self) -> str:
        return f"Surname: {self.surname}, age: {self.age}"
        
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Pupil):
            return (self.age == other.age and
                    self.surname == other.surname)
        return False