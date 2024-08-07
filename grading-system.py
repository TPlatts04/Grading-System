import sys

def introFunc():
    print("\nWelcome to Tom's Grading System CLI Application")
    print("Let's get started!")
    try:
        numOfClassMembers = int(input("Enter the total amount of class members you are inputting: "))
        storeMembers(numOfClassMembers)
    except ValueError:
        print("Please enter a number...")
        introFunc()

parentDictionary = {
    "Members" : {},
    "Grade A" : {},
    "Grade B" : {},
    "Grade C" : {},
    "Grade D" : {},
    "Grade E" : {},
    "Grade F" : {}
}

GRADES_LIST = ["A", "B", "C", "D", "E", "F"]

def storeMembers(totalMembers):
    for i in range(0, totalMembers):
        memberID = i
        memberName = input("\nEnter the name of the current class member: ")
        parentDictionary["Members"].update({memberID: memberName})
    memberGrades()

def memberGrades():
    listOfMembers = []
    dictionaryIndex = 0
    for x in range(0, len(parentDictionary["Members"])):
        dictionaryIndex = parentDictionary["Members"][x]
        listOfMembers.append(dictionaryIndex)
    for y in range(0, len(listOfMembers)):
        memberGrade = input(f"\nWhat grade (A-F) has {listOfMembers[y]} recieved? ").upper()
        match memberGrade:
            case "A":
                parentDictionary["Grade A"].update({y: listOfMembers[y]})
            case "B":
                parentDictionary["Grade B"].update({y: listOfMembers[y]})
            case "C":
                parentDictionary["Grade C"].update({y: listOfMembers[y]})
            case "D":
                parentDictionary["Grade D"].update({y: listOfMembers[y]})
            case "E":
                parentDictionary["Grade E"].update({y: listOfMembers[y]})
            case "F":
                parentDictionary["Grade F"].update({y: listOfMembers[y]})
            case _:
                print(f"{memberGrade} is an invalid option, please try again...")
                for a in range (0, len(GRADES_LIST)):
                    parentDictionary[f"Grade {GRADES_LIST[a]}"].clear()
                memberGrades()
    viewGrades()

def viewGrades():
    gradeView = input("\nWhat grade would you like to see to view class members in that area (A-F): ")
    for b in range (0, len(GRADES_LIST)):
        if (gradeView == GRADES_LIST[b]):
            break;
        else:
            print("Invalid option, please try again...")
            viewGrades()
    print(f"\n{parentDictionary[f"Grade {gradeView}"]}, these people all got a grade of {gradeView}")
    print(f"{len(parentDictionary[f"Grade {gradeView}"])} people got a grade of {gradeView}")
    sys.exit()

if __name__ == "__main__":
    introFunc()
else:
    sys.exit()