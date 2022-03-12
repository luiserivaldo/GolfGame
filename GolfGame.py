def main():
    print("Welcome to Tropical Golf!", "\n")
    user_name = str(input("Please enter your name: "))  # Asks user name
    if user_name == "":  # Loops the request if name is blank
        print("Name must be filled.")
        user_name = str(input("Please enter your name: "))
    get_par = str(input("Please enter the number of pars for the game (3-5): ")).isdigit()  # Asks no. of par for game
    if get_par is False:  # Checks if the input is an number
        print("Please input a valid value.")
        get_par = str(input("Please enter the number of pars for the game (3-5): ")).isdigit()
    if get_par not in range(3, 6):  # Loops the request for input of input does not reach requirement
        print("Par must be between 3 to 5.")
        get_par = int(input("Please enter the number of pars for the game (3-5): "))
    get_distance_to_hole = str(input("Please insert the distance to the hole (195-250): ")).isdigit()
    if get_distance_to_hole is False:  # Checks if the input is an number
        print("Please input a valid value.")
        get_distance_to_hole = str(input("Please insert the distance to the hole (195-250): ")).isdigit()
    if get_distance_to_hole not in range(195, 251):  # Loops the request for input of input does not reach
        # requirement
        print("Distance must be between 195 to 250.")
        get_distance_to_hole = int(input("Please insert the distance to the hole (195-250): "))
    show_menu(user_name, get_distance_to_hole, get_par)  # Starts the menu function


def show_menu(user_name, get_distance_to_hole, get_par):
    print("Welcome", user_name, ".", "\n", "(I)nstructions", "\n", "(P)lay", "\n", "(Q)uit", "\n")  # Shows menu
    menu_input = str(input("What would you like to do? ")).lower()  # Asks for user input based on menu
    menu_loop = 0
    while menu_loop < 1:  # Loops the menu if "Instructions" is selected
        if menu_input == "i":
            print("This is a simple golf game in which each hole is", get_distance_to_hole, "m game away with par",
                  get_par, ".",  "\n", "You are able to choose from 3 clubs: the Driver, Iron or Putter.", "\n",
                  "The Driver will hit around 100m, the Iron around 30m and the Putter around 10m. The putter is best",
                  "used very close to the hole.", "\n")
            menu_input = str(input("What would you like to do? ")).lower()
        elif menu_input == "p":  # Starts the game function
            game_play(user_name, get_distance_to_hole, get_par)
        elif menu_input == "q":  # Exits the program
            print("Farewell and thanks for playing, ", user_name, ".")
            exit()
        else:
            print("Please enter a valid value.")  # Requests input if previous input is invalid
            menu_input = str(input("What would you like to do? ")).lower()


def game_play(user_name, get_distance_to_hole, get_par):
    distance_left = get_distance_to_hole
    score = 0  # Default score value; reverts back to default if user replays the game
    print("Distance left is", distance_left, "m.", "\n")
    while distance_left != 0:  # Loops the game if distance left is not 0
        club_input = str(input("Choose your club: (D)river, (I)ron, (P)utter: ")).lower()
        if club_input == "d":
            import random
            driver = random.randint(80, 120)  # Random distance around 20% from 100
            if distance_left < 0:
                distance_left = -distance_left  # Deducts distance shot from distance left
            distance_left = distance_left - driver  # Loops the distance if it goes over 0
            score += 1  # Adds score to the game
            print("The ball flung", driver, "m. Distance left is", abs(distance_left), "m. Shot", score, ".", "\n")

        elif club_input == "i":
            import random
            iron = random.randint(24, 36)  # Random distance around 20% from 30
            if distance_left < 0:
                distance_left = -distance_left
            distance_left = distance_left - iron  # Loops the distance if it goes over 0
            score += 1    # Adds score to the game
            print("The ball flung", iron, "m. Distance left is", abs(distance_left), "m. Shot", score, ".", "\n")

        elif club_input == "p":
            if distance_left > 10:  # Putter distance value is determined depending on distance left
                import random
                putter = random.randint(8, 12)  # Random distance around 20% from 10
                if distance_left < 0:
                    distance_left = -distance_left  # Loops the distance if it goes over 0
                distance_left = distance_left - putter
                score += 1    # Adds score to the game
                print("The ball flung", putter, "m. Distance left is", abs(distance_left), "m. Shot", score, ".", "\n")

            elif distance_left <= 10:  # Changes putter value if distance left is below or equal to 10
                import random
                putter = random.randint(abs(round(distance_left*0.8)), abs(round(distance_left*1.2)))  # Random distance
                # around 20% from current distance left
                if putter <= 0:  # Ensures shot distance is at least 1
                    putter = 1
                if distance_left < 0:
                    distance_left = -distance_left  # Loops the distance if it goes over 0
                distance_left = distance_left - putter
                score += 1    # Adds score to the game
                print("The ball flung", putter, "m. Distance left is", abs(distance_left), "m. Shot", score, ".", "\n")
        else:
            score += 1    # Adds score to the game
            print("It was an air swing! The ball flung 0 m. Distance left is", abs(distance_left), "m. Shot", score, ".",
                  "\n")  # invalid input treats distance shot as 0

    if score > get_par:  # Display this message of score is over par
        game_score = score - get_par
        print("Clunk... After", score, "hits, the ball is in the hole! Disappointing. You are", game_score, "over par.",
              "\n")
    elif score == get_par:  # Display this message of score is equal to par
        print("Clunk... After", score, "hits, the ball is in the hole! And that’s par.", "\n")
    elif score < get_par:    # Display this message of score is under par
        game_score = get_par - score
        print("Clunk... After", score, "hits, the ball is in the hole! Congratulations, you are", game_score,
              "under par.", "\n")
    get_retry = str(input("Try again? [Y/N]")).lower()  # Requests input to restart the game
    print("")
    if get_retry == "y":  # Shows the menu
        show_menu(user_name, get_distance_to_hole, get_par)
    if get_retry == "n":  # Quits the program
        print("Farewell and thanks for playing, ", user_name, ".")
        exit()
    else:
        print("Please enter a valid value.")  # Requests input if previous input is invalid
        get_retry = str(input("Try again? [Y/N]")).lower()


main()
