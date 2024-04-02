"""This is example file to demonstrate pyinstaller usage"""

def talk():
    message = input("Say something: ")

    if not message:
        return talk()
    
    return message


def main():
    print("You said: " + talk())


if __name__ == "__main__":
    main()