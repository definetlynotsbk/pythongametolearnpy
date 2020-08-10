print ("Welcome to my game!")
name = input("What is your name? ").title()
age = int(input(f"Hi {name} What is your age? "))
health = 10
if age >=18:
    print("You are old enough!")
    wants_to_play = input("Do you want to play?")
    if wants_to_play == "yes":
        print("Lets GO!")
        print("you have", health, "health")
        choice1 = input('You are stranded... which direction do you want to head to? (left/right)')
        if choice1 == "left":
            choice2 = input("So you head left and reach a river... what do you do? do you swim across or go around? (across/around)")
            if choice2 == "across":
                print("you were hurt by a sharp rock and lost 5 health! But you got across the river!")
                health -= 5
                print("You now have", health, "health remaining!")
                choice3 = input('you see a small hut in the distance and you see a cave... where do you decide to go? (house/cave)')
                if choice3 == "house":
                    print('you decide to go to the house and you see its abandoned but you found an apple!')
                    print('You ate the apple and feel ill')
                    health -= 5
                    if health == 0:
                        print('you have', health, 'health! You Died')
                    else:
                        print('you survived!')
                else:
                    print('there was a bear in the cave and it killed you!')
            elif choice2 == "around":
                print('you found a log lying across the river and cross the river safely!')
                choice3 = input('you see a small hut in the distance and you see a cave... where do you decide to go? (house/cave)')
                if choice3 == "house":
                    print('you decide to go to the house and you see its abandoned but you found an apple!')
                    print('You ate the apple and feel ill')
                    health -= 5
                    if health == 0:
                        print('you have', health, 'health! You Died')
                    else:
                        print('you survived!')
                else:
                    print('there was a bear in the cave and it killed you!')
            else:
                print("you died of starvation!")
        else:
            print("you slipped into the cavern!")

    else:
        print ("ok then")
else:
    print("You are not old enough!")