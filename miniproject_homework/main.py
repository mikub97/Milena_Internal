print("Welcome to my first game")
name = input("What is your name?")
age = int(input("What is your age?"))

print(" Hello", name," you are", age, "years old")

health = 10

if age >= 18:
    print("you are old enough")


    wants_to_play = input("Would you like to play ").lower()
    if wants_to_play == "yes":
        print("you are starting with", health, " health")
        print("let's play")

        left_or_right = input("choose between 'left' or 'right'(left/right)")
        if left_or_right == "left":
            ans = input("good choice, you follow the path and reach a mountain... Do you climb it or go around it? (climb/ go around) ")

            if ans == "go around":
                print("you went over it and reached the other side of the mountain")
            elif ans == "climb":
                print("you managed to climb it but got tired and lost 5 health")
                health -= 5

            ans = input("you notice a house and a river, which one do you go to? (house/river)")
            if ans == "house":
                print("you go to the house, and get greeted by the owner... he doesn't like you and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("you now have 0 health and you lose the game..")
                else:
                    print("you have survived")

            else:
                print("you fell in the river and lost...")

        else:
            print("wrong choice! you lost")
    else:
        print("bye")
else:
    print("you are not old enough to play")