"""
A = 1
while A:
    print("meow")
    i = input("Do you wish to continue meowing? \n y = yes, n = no ")
    if i == "y":
        print("meow")
    elif i == "n":
        print("bitch")
        A = 0
    else:
        print("you dumbass")
"""


def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            break
    return n

def meow(iterations, printLol):
    for _ in range(iterations):
        print("meow")
        if (printLol):
            print("lol")

def main():
    number = get_number()
    meow(number, number % 2 == 0)

main()