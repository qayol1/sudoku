solution = []
solution.append(["1","5","8","9","2","3","6","4","7"])
solution.append(["2","3","4","5","7","6","1","9","8"])
solution.append(["6","9","7","8","1","4","3","5","2"])
solution.append(["5","7","2","4","8","1","9","3","6"])
solution.append(["8","6","9","3","5","2","7","1","4"])
solution.append(["4","1","3","7","6","9","2","8","5"])
solution.append(["3","4","6","2","9","5","8","7","1"])
solution.append(["9","8","1","6","4","7","5","2","3"])
solution.append(["7","2","5","1","3","8","4","6","9"])

template = []
template.append([" "," ","8"," ","2"," "," "," "," "])
template.append([" "," ","4"," "," ","6"," ","9","8"])
template.append([" "," "," "," "," "," ","3"," "," "])
template.append(["5"," "," ","4"," ","1"," ","3"," "])
template.append([" ","6","9","3"," ","2","7","1"," "])
template.append([" ","1"," ","7"," ","9"," "," ","5"])
template.append([" "," ","6"," "," "," "," "," "," "])
template.append(["9","8"," ","6"," "," ","5"," "," "])
template.append([" "," "," "," ","3"," ","4"," "," "])

def show():
    print("    1     2     3      4     5     6      7     8     9")
    print("===========================================================")
    for i in range(9):
        for j in range(9):
            if j%3 == 0:
                print("||", end ="")
                print (" ", template[i][j], " ", end="")
            else:
                print("|", end ="")
                print (" ", template[i][j], " ", end="")
        print("||", i+1,  end ="")
        if i%3 == 2:
            print("\n===========================================================")
        else:
            print("\n-----------------------------------------------------------")

def validation(line):
    valid = 0
    if len(line) == 5:
        if line[0].isdigit() == False or line[0] == "0" :
            print("The row must be 1...9")
        else:
            valid += 1
        if line[1] != " " or line[3] != " ":
            print("Please separate by 'space'")
        else:
            valid += 1
        if line[2].isdigit() == False or line[2] == "0" :
            print("The column must be 1...9")
        else:
            valid += 1
        if line[4].isdigit() == False or line[4] == "0" :
            print("The number must be 1...9")
        else:
            valid += 1
    else:
        print("Please enter the right format!")
    if valid == 4:
        return(True)
    else:
        return(False)

def check(solution,template):
    result = True
    for i in range(9):
        for j in range(9):
            if template[i][j] != solution[i][j]:
                result = False
    return result

show()
var = 1
filled_cells = 0
while var == 1 :
    line = input("Please enter column, row and number separated by 'space' or press 'x' to quit): ")
    if line == "x":
        break
    if validation(line) == True:
        column = int(line[0])-1
        row = int(line[2])-1
        number = line[4]
        if template[row][column] == " ":
            template[row][column]=number
            filled_cells += 1
            show()
        else:
            print("You can't change that cell!")
    if filled_cells == 53:
        if check(solution,template) == True:
            print("Your solution is correct!")
            print("You win!")
            print("Congratulations!")
            break
        else:
            print("Your solution is incorrect!")
            print("Try again!")  
            break