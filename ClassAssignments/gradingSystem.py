def getNumberOfStudents():
   while True:
      try:
         numberofstudents = int(input("Enter the number of students you want to grade: "))
         if numberofstudents <= 0:
            print("Enter a valid number of students")
         else:
            return numberofstudents
            break
      except ValueError:
        print("Invalid Input")






def getNamesandScores():
    namesofstudents = []
    scoresofstudents = []
    for i in range(getNumberOfStudents()):
        nameinput = input("Enter the name of the student: ")
        while True:
            try:
                scoreinput = int(input("Enter the score of the student: "))
                if scoreinput < 0:
                    print("Enter a valid score")
                else:
                    break
            except ValueError:
                print("Invalid input")

        namesofstudents.append(nameinput.strip())
        scoresofstudents.append(scoreinput)
    return [namesofstudents,scoresofstudents]
def getGrade(score: int):
    match True:
        case _ if score >= 70:
            return "A"
        case _ if score >= 60:
            return "B"
        case _ if score >= 50:
            return "C"
        case _ if score >= 40:
            return "D"
        case _:
            return "F"


def outputResults(namesandscores):
    names,scores=namesandscores
    print(f"{'Name':<15}{'Score':<10}{'Grade'}")
    for i in range(len(names)):
        print(f"{names[i]:<15}{scores[i]:<10.2f}{getGrade(scores[i])}")


outputResults(getNamesandScores())


