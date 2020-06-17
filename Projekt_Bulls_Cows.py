import random
from timeit import default_timer as timer
oddelovac = "-" * 40

def main():
    gen_cislo = random.sample(range(10), 4)
    vitac()
    pokusy = 0
    start = timer()
    while True:
        hadane_cislo = hadani()
        bulls, pokusy = porovnani(gen_cislo, hadane_cislo, pokusy)
        vysledek = vyhodnoceni(bulls,pokusy)
        if not vysledek:
            break
    end = timer()
    print(f"It took you {end - start:.0f} seconds to guess right number.")
    print(oddelovac)
    hraci_kolo()

def vitac():
    print("""
Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game. 
""")

def hadani():
    hada = input("Enter a number: ")
    while test_hadani(hada):
        hada = input("Enter a number: ")
    hada_list = [int(x) for x in str(hada)]
    return hada_list

def test_hadani(hadane_c):
    while len(hadane_c) != 4 or not hadane_c.isnumeric():
        print("Wrong number input, try again!")
        return True
    else:
        return False

def porovnani(c_list,hadane_cislo,pokus):
    bulls = 0
    cows = 0
    pokus += 1
    for index,cislo in enumerate(c_list):
            if c_list[index] == hadane_cislo[index]:
                bulls += 1
            elif cislo in hadane_cislo:
                cows += 1
    print(bulls, "bull" if bulls == 1 else "bulls",",", cows, "cow" if cows == 1 else "cows")
    return bulls, pokus

def vyhodnoceni(bull, pokus):
    if bull == 4:
        print(oddelovac)
        print(f"Correct, you've guessed the right number in {pokus} guesses!")
        if pokus < 4:
            print("That's amazing!")
        elif pokus >= 4 and pokus < 8:
            print("That's average!")
        elif pokus >= 8 and pokus < 12:
            print("That's not so good!")
        else:
            print("Are you even trying?!")
        print(oddelovac)
        return False
    else:
       return True

def hraci_kolo():
    hrat = input("Do you want to play again y/n: ")
    while test2_hraci_kolo(hrat):
        hrat = input("Do you want to play again y/n: ")
    if hrat == "y":
        main()
    elif hrat == "n":
        print("Thanks for playing!")
        exit()

def test2_hraci_kolo(hrani):
    if hrani == "y" or hrani == "n":
        return False
    else:
        print("Type", "y", "or", "n")
        return True

main()
