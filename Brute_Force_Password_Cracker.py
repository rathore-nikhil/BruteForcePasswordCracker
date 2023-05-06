# Importing Python Libraries
import itertools
import os
import time
from termcolor import colored
import pyautogui
import math
import sys

os.system('cls')

# Introducing the program
for x in colored("WELCOME TO THE BRUTE FORCE PASSWORD CRACKER", "magenta"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.05)

os.system('cls')

for x in colored(
        "This program typically runs faster on devices with higher system performance....",
        "white"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.05)

os.system('cls')

for x in colored(
        "It looks for lowercase letters, uppercase letters, numbers and common symbols that you use on your keyboard. So don't use special symbols like trademark, copyright, etc. Unless you want the program to never find your password.",
        "cyan"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.05)

time.sleep(1)

for x in colored(
        "\n\n\nRemember, long and/or complicated password can take several minutes to hours to be cracked....",
        "yellow"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.05)

os.system('cls')

for x in colored("So, without wasting much time. Let's get started....",
                 "green"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.05)

os.system('cls')


# Brute Force Function. Looping to guess many passwords untill one of them matches user password
def product_loop(password_1, chars):
    start = time.time()
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            millions = 0
            crores = 0
            guess = ''.join(guess)
            if attempts % 10000000 == 0:
                os.system('cls')
                print(colored("Attempting to crack password....", "yellow"))
                print()
                millions = attempts / 1000000
                millions = math.ceil(millions)
                crores = attempts / 10000000
                crores = math.ceil(crores)
                if attempts > 100000000:
                    print(colored("This may take a while", "red"))
                    print()

                # Printing, How many millions of password guesseed so far?
                print(
                    colored(
                        "%s million (OR %s crore) passwords guessed so far..." % (millions, crores),
                        "cyan"))

            if guess == password_1:
                end = time.time()
                distance = end - start
                return (attempts, distance)


# Initializing an empty string
String_Types = ""

String_Types += "abcdefghijklmnopqrstuvwxyz"
String_Types += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
String_Types += "1234567890"
String_Types += "~`!@#$%^&*()-_=+{[}]:;'\"|\<,>.?/"

print()

# Taking input from user
password = pyautogui.password("Enter your password")
time.sleep(1)

if password == "":
    print(
        colored("Don't even need to look at. You didn't specify any password\n\n\n\n",
                "blue"))
else:
    guesses, time_taken = product_loop(password, String_Types)
    time_taken1 = math.ceil(time_taken)
    if guesses == 1:
        guesses1 = "guess"
    else:
        guesses1 = "guesses"
    if time_taken1 == 1:
        time_in_seconds = "second"
    else:
        time_in_seconds = "seconds"
    print()
    os.system('cls')

    # Printing the matched password
    print(
        colored(
            "Cracked your password %s in %s %s and in %s %s...." %
            (password, guesses, guesses1, time_taken1, time_in_seconds),
            "green"))
    time.sleep(1)

    if time_taken == 0:
        print("")
    else:

        # To find approximate number of passwords guessed per second
        guesses = guesses / time_taken1
        guesses = math.ceil(guesses)

        # Printing approximate number of password guessed per second
        print(
            colored(
                "\n\nApproximately %s password guessed per second!\n\n\n\n" %
                (guesses), "magenta"))
