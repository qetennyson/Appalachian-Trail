import math

def advance_day(position, supplies, terrain,
                party_size, pace, stamina, ration_level):
    """
    For all of its fun, this function is now certifiably
    doing way more than one job.
    
    Proficient students end up writing code like this
    as they get in the weeds, and if we can catch them
    early we can help them really get ahead!
    """

    if terrain == 'easy':
        position += pace

    elif terrain == 'moderate':
        position += pace * .75
        # hmm what happens to stamina?
        stamina -= .1

    elif terrain == 'hard':
        position += pace * .5
        stamina -= .2

    return position, supplies - (ration_level * party_size), stamina
        
             

def main():
    days = 3

    trail_position = 0
    supplies = 10
    terrain = 'moderate'
    
    party_size = 2
    pace = 10
    stamina = 1.0
    ration_level = 1.0

    while days:
        trail_position, supplies, stamina = advance_day(trail_position, supplies, terrain, party_size, pace, stamina, ration_level)
        days -= 1
        print("Position", trail_position)
        print("Supplies", supplies)
        print("Stamina", stamina)


main()