for _ in range(10):
    name = input("What's your name? ")
    match name:
        case "harry" | "her" | "ron":
            print("aye, nice")
        case "Draco":
            print("fuck")
        case _:
            print("who")
