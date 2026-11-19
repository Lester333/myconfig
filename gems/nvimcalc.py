def printer():
    try:
        answ = input('You want Y or N? Y/N: ')
        if answ == "Y":
            print("Y")
        elif answ == "N":
            print("N")
        else:
            print("Try again.")
            try: printer()
            except RecursionError:
                print("Тычо делаешь?")
    except KeyboardInterrupt:
        print(" Interrupted by user.")
        pass

printer()
