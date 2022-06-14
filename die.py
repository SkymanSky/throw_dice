from random import choice, randint

class Die:
    """Tek bir zarı temsil eden bir sınıf."""
    def __init__(self,num_sides=6):
        """Altı yüzlü bir zar olduğunu varsayın."""
        self.num_sides=num_sides
    def roll(self):
        """1 ile zar yüzü arasında rastgele bir değer döndür."""
        return randint(1,self.num_sides)
