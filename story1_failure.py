def advance_day(position, supplies):
    position -= 1
    supplies -= 1

def main():
    days = 3

    trail_position = 0
    supplies = 10

    # fails completely.
    # parameters of advance_day have nothing to do with
    # our desired state change.
    while days:
        advance_day(trail_position, supplies)
        days -= 1
        print("Position", trail_position)
        print("Supplies", supplies)


main()