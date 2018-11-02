from sys import exit, argv

script, first = argv

# list of virtues

virtues = ["fairness","moderate downside risk","some upside risk"]

#function sad
def sad():
    print("Is it something in the past or in the future?")

    choice = input("> ")

    if choice == "past":
        print("then be grateful it is over")
    elif choice == "future":
        print("be grateful it has not happened yet")
    else:
        print("please answer by \'past\' or \'future\'")

#function stressed
def stressed():
    print("Have you tried preparation using something you have control over? Give an example")

    choice = input("> ")

    stuff = open(first).read()

    if choice in stuff:
        print("Well done, keep on doing it")
    elif choice not in stuff:
        print("Try something else")
    else:
        dead("Oh, nothing to see here then :)")

#function anxious
def anxious():
    print("is it something that has already happened?")

    choice = input("> ")

    if choice == "yes":
        print("then why do you worry about something that is not there anymore?")
    elif choice == "no":
        print("the fear of the future event is worse then the event itself.")
        print("if you feel stressed, then come back here and go the stress way")
    else:
        print("please answer by yes or no")

#function pain
def pain():
    print("is it unbearable?")

    choice = input("> ")

    if choice == "yes":
        print("then goo and buy some painkillers")
    elif choice == "no":
        print("then remember \"this too shall pass\"")
    else:
        print("please answer by yes or no")

#function boredom
def boredom():
    print("Have you tried doing something you have control over? Give an example")

    choice = input("> ")

    stuff = open(first).read()

    if choice in stuff:
        print("feeling a bit less bored already? Well done, keep on doing it")
    elif choice not in stuff:
        print("Try something else")
    else:
        dead("Oh, nothing to see here then :)")
#function confused
def confused():

    for virtue in virtues:
        print(f"Think about the option you seem to prefer. Is there {virtue}?")

        choice = input("> ")

        if choice == "no":
            print("Then don't")
        elif choice == "yes":
            print("No problem there")
        else:
            print("please answer by yes or no")

def dead(why):
  print (why, "May the force be with you")
  exit(0)

#start function
def start() :
    print("What is bothering you?")

    choice = input("> ")

    if choice == "sad":
        sad()
    elif choice == "stressed":
        stressed()
    elif choice == "anxious":
        anxious()
    elif choice == "pain":
        pain()
    elif choice == "boredom":
        boredom()
    elif choice == "confused":
        confused()
    else:
        dead("Oh, nothing to see here then :)")

start()
