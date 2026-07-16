def advance_day(position, supplies):    
        """
        These rudimentary fixed values will become abstractions!

        This helps students understand that we can have an
        idea without immediately starting the coding process.
        
        We know we want to have trail progress be more interesting
        than a guarantee of "1".  However, we have to step back, and realize
        that putting all that in advance_day() is a bad idea.

        Help them see that 10 minutes of abstract thinking away
        from the code will save them hours of debugging a ridiculous function
        """
        return (position + 1, supplies - 1)

def main():
    days = 3

    trail_position = 0
    supplies = 10

    # fails completely.
    # parameters of advance_day have nothing to do with
    # our desired state change.
    while days:
        trail_position, supplies = advance_day(trail_position, supplies)
        days -= 1
        print("Position", trail_position)
        print("Supplies", supplies)


main()