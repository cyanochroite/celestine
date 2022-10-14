command = input("What are you doing next? ")
match command.split():
    case [action]:
        print(action)
    case [action, obj]:
        print(F"{action} + {obj}")
