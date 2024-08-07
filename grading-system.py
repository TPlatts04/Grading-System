def introFunc():
    print("\nWelcome to Tom's Grading System CLI Application")
    print("Let's get started!")
    try:
        numOfClassMembers = int(input("Enter the total amount of class members you are inputting: "))
    except ValueError:
        print("Please enter a number...")
        introFunc()

if __name__ == "__main__":
    introFunc()