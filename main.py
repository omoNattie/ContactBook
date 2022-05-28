from time import sleep
# imports


def createcon():
    name = input("What's the name of your contact?\nYour contact's name:")
    sleep(0.3)
    print("processing...")
    sleep(1)

    number = int(input("Alright, now, what's the number of your contact?\nYour contact's number:"))
    sleep(0.3)
    print("processing...")
    sleep(1)

    print("Okay, done!\nSee you later!")

    createfile = open("contacts.txt", "a")  # open contacts file only as write
    createfile.write(f"name: {name}, number: {number}\n")  # write whatever person said
    createfile.close()  # close


def seecon():
    seefile = open("contacts.txt", "r")  # open contacts file only as read
    print(seefile.read())  # print contents
    seefile.close()  # close


choice = int(input("Hello! Welcome to your contact book!\nPress 1 to create a new contact!\n"
                   "Press 2 to see your existing contacts!\nYour choice: "))

if choice == 1:
    createcon()
elif choice == 2:
    seecon()
else:
    print("That's not a choice!")
