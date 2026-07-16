"""
We don't necessarily want to jump into an object on Story 1, 
but if you did it might begin here.
"""

class Expedition:

    def __init__(self, name="Ford", trail_pos=0, supplies=10):
        self.name = name
        self.trail_pos = trail_pos
        self.supplies = supplies
    
    
    def advance_day(self):
        self.trail_pos += 1
        self.supplies -= 1

    def __str__(self):
        return f'{self.name}\nSupplies: {self.supplies}\n \
        Trail Position: {self.trail_pos}'
        

    

def main():
    ford_expedition = Expedition()
    print(ford_expedition)

    ford_expedition.advance_day()

    print(ford_expedition)

main()