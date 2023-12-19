def evenOrOdd():
    x = int(input("Feed me a number. "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0 


def main():
    A = True
    while A:
        evenOrOdd()
        v = input("Do you wish to continue? \ny = yes, n = no \n")
        if v == "y":
            A = True
        elif v == "n":
            A = False
        else:
            A = False

main()