import math

def advance_day(position, supplies, terrain,
                party_size, pace, stamina, ration_level):
    """
    With abstraction, advance_day() begins to look far more like the
    "game event" function it was meant to be!
    """
    supplies -= food_consumed(ration_level, party_size)
    position += miles_walked_today(pace, terrain, stamina)
    
    return position, supplies
        
def food_consumed(ration_level, party_size):
    return ration_level * party_size

def miles_walked_today(pace, terrain, stamina):
    """
    It's likely (certain?) that this game mechanic
    could become a subject for debate.
    
    Is pace modified directly as a result of terrain,
    or can the party handle tough terrain provided it has
    enough stamina resulting in a decrement of stamina on
    tougher terrain?
    
    No matter what, a question ripe for complexity means we need
    abstraction to help us."""

    if terrain == 'easy':
        return pace * stamina
    elif terrain == 'moderate':
        return (pace * .75) * stamina
    elif terrain == 'hard':
        return (pace * .5) * stamina

def main():
    days = 3

    trail_position = 0
    supplies = 10
    terrain = 'easy'
    
    party_size = 2
    pace = 10
    stamina = 1.0
    ration_level = 1.0

    while days:
        trail_position, supplies = advance_day(trail_position, supplies, terrain, party_size, pace, stamina, ration_level)

        days -= 1
        print("Position", trail_position)
        print("Supplies", supplies)
        print("Stamina", stamina)


main()