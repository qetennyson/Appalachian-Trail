import time
from random import random, randint, choice

FAVORABLE_CONDITIONS = ['light rain', 'overcast', 'chilly', 'still air']
UNFAVORABLE_CONDITIONS = ['windy', 'heavy rain', 'thunderstorm', 'foggy', 'heat wave']
CONDITIONS = FAVORABLE_CONDITIONS + UNFAVORABLE_CONDITIONS

DELAY = 2

def advance_day(position, terrain,
                hunger, pace, stamina, rations):
    """
    With abstraction, advance_day() begins to look far more like the
    "game event" function it was meant to be!
    """
    rations -= int(food_consumed(hunger, rations))
    position += int(miles_walked_today(pace, terrain, stamina)) # type: ignore
    
    return position, rations
        
def food_consumed(pace, hunger):
    return pace * hunger

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

def get_hunt_success(luck, condition):
    """
    Randomly determines the success of a hunt, 
    based on conditions.

    Returns True if luck >= .8
    """
    if condition == 'mild' and luck >= .8:
        return True
    
    elif condition in FAVORABLE_CONDITIONS:
        luck += .2
    elif condition in UNFAVORABLE_CONDITIONS:
        luck -= .4

    return luck >= .8

def get_gather_success(luck, condition):
    """
    Randomly determines the success of gathering, 
    based on conditions.

    Returns:
    True if luck >= .4
    """
    if condition == 'mild' and luck >= .4:
        return True
    
    elif condition in FAVORABLE_CONDITIONS:
        luck += .2
    elif condition in UNFAVORABLE_CONDITIONS:
        luck -= .4

    return luck >= .4
    
def get_hiker_choice(day, condition):
    VALID_RESPONSES = ['no', 'n', 'hunt', 'gather']

    print("It is day " + str(day))
    print("Conditions: " + condition.upper())

    while True:
        print("\nWill you hunt or gather before hiking today?")

        response = input("[hunt/gather/no] > ")

        if response.lower() not in VALID_RESPONSES:
            print("Enter a valid choice.")
            continue

        return response
    
def hunt(luck, condition):
    """
    Returns 15 rations on a successful hunt.
    """
    print("You go out for a hunt.")

    if get_hunt_success(luck, condition):
        print("By the grace of the trail, you snare some game.")
        return 15
    else:
        print("No luck today.")
        return 0
    

def gather(luck, condition):
    """
    Return 8 rations on a successful gathering.
    """
    print("You try to gather food in a nearby area.")
    if get_gather_success(luck, condition):
        print("You gather some edible looking items.")
        return 8
    else:
        print("You find nothing edible.")
        return 0

def check_injury(luck, condition):
    luck = random()
    if luck < .15 or (condition in UNFAVORABLE_CONDITIONS and luck < .25):
        print("You feel illness setting in...")
        return randint(3,8)

    return 0

def check_illness(luck, condition):
    luck = random()
    if luck < .2 or (condition in UNFAVORABLE_CONDITIONS and luck < .4):
        print("You injured yourself while out and about.")
        return random() - .2
    
    return 0

def get_todays_luck():
    return random()

def display_hike():
    print("\nYou trudge along for another day.\n")


def main():

    # days
    days_required = 5
    days_hiked = 0

    # hiker stats
    trail_position = 0
    rations = 10
    hunger = .5
    stamina = 1.0
    pace = 10

    # negative hiker conditions
    injury = 0
    illness = 0.0

    while days_hiked < days_required:
        
        time.sleep(DELAY)

        base_stamina = 1.0
        base_pace = 10

        terrain = 'easy'
        conditions = choice(CONDITIONS + (['mild'] * 5))
        luck = get_todays_luck()

        # hiker variables
        hikers_choice = get_hiker_choice(days_hiked, conditions).lower()
        if hikers_choice == 'hunt':
            rations += hunt(luck, conditions)
        elif hikers_choice == 'gather':
            rations += gather(luck, conditions)

        if not(injury or illness):
            injury = check_injury(luck,conditions)
            illness = check_illness(luck, conditions)

        todays_pace = base_pace - injury
        todays_stamina = base_stamina - illness
        
        display_hike()
        trail_position, rations = advance_day(trail_position, terrain, 
                                            hunger, todays_pace, todays_stamina, rations)
        days_hiked += 1
        print("Position", trail_position)
        print("Rations", rations)
        print("Stamina", stamina)


        

main()