import os, string

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
template.append([" "," ","8 "," ","2 "," "," "," "," "])
template.append([" "," ","4 "," "," ","6 "," ","9 ","8 "])
template.append([" "," "," "," "," "," ","3 "," "," "])
template.append(["5 "," "," ","4 "," ","1 "," ","3 "," "])
template.append([" ","6 ","9 ","3 "," ","2 ","7 ","1 "," "])
template.append([" ","1 "," ","7 "," ","9 "," "," ","5 "])
template.append([" "," ","6 "," "," "," "," "," "," "])
template.append(["9 ","8 "," ","6 "," "," ","5 "," "," "])
template.append([" "," "," "," ","3 "," ","4 "," "," "])

var = 1
filled_cells = 0
steps = 0

def find_repetition_column(row, column, number): 
    """finds if we have more than one from the same number in a column"""
    row_double = 0
    for i in range(9):
        if template[i][column][0] == number:
            row_double +=1
    if row_double > 1:
        return True
    else:
        return False

def find_repetition_row(row, column, number): 
    """finds if we have more than one from the same number in a row"""
    column_double = 0
    for i in range(9):
        if template[row][i][0] == number:
            column_double +=1
    if column_double > 1:
        return True
    else:
        return False

def find_repetition_grid(row, column, number): 
    """finds if we have more than one from the same number in 3*3 grid"""
    grid_double = 0
    row_from = (row//3)*3
    row_to = row_from + 3
    column_from = (column//3)*3
    column_to = column_from + 3
    for i in range(row_from,row_to):
        for j in range(column_from,column_to):
            if template[i][j][0] == number:
                grid_double += 1
    if grid_double > 1:
        return True
    else:
        return False

def show():
    """Prints the sudoku table"""
    global steps
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Number of steps: ",steps, "\n")
    print("\033[1;37;40m    A     B     C      D     E     F      G     H     I")
    print("===========================================================")
    for i in range(9):
        for j in range(9):
            if j%3 == 0:
                print("||", end ="")
                if len(template[i][j]) == 1:
                    print ("\033[1;37;40m ", template[i][j][0], "\033[1;37;40m ", end="")
                else:
                    print ("\033[1;31;40m ", template[i][j][0], "\033[1;37;40m ", end="")
            else:
                print("|", end ="")
                if len(template[i][j]) == 1:
                    print ("\033[1;37;40m ", template[i][j][0], "\033[1;37;40m ", end="")
                else:
                    print ("\033[1;31;40m ", template[i][j][0], "\033[1;37;40m ", end="")
        print("||", i+1,  end ="")
        if i%3 == 2:
            print("\n===========================================================")
        else:
            print("\n-----------------------------------------------------------")

def validation(line):
    """Checks if the given argumens are in the correct syntax"""
    valid = 0
    if len(line) == 5:
        if line[0] not in "abcdefghiABCDEFGHI":
            print("The row must be A...I")
        else: valid += 1
        if line[1] != " " or line[3] != " ":
            print("Please separate by 'space'")
        else:
            valid += 1
        if line[2].isdigit() == False or line[2] == "0" :
            print("The column must be 1...9")
        else:
            valid += 1
        if line[4].isdigit() == False:
            print("The number must be 1...9 or '0' to delete")
        else:
            valid += 1
    else:
        print("Please enter the right format!")
    if valid == 4:
        return(True)
    else:
        return(False)

def check(solution,template):
    """Checks the filled sudoku table"""
    result = True
    for i in range(9):
        for j in range(9):
            if template[i][j][0] != solution[i][j]:
                result = False
    return result

def fill_cell(line):
    """Insert the given number to the sudoku table or delete"""
    global steps
    global filled_cells
    string_lower = "abcdefghi"
    string_upper = "ABCDEFGHI"
    if string_lower.find(line[0]) == -1:
        column = string_upper.find(line[0])
    else:
        column = string_lower.find(line[0])
    row = int(line[2])-1
    if line[4] != "0": 
        number = line[4]
        steps += 1 # clear a cell doesn't count as a step
    else:
        number = " "
        filled_cells = filled_cells-1
    if len(template[row][column]) == 1: #the initial numbers in the template are two char long and can't be change'
        if template[row][column] == " ":
            filled_cells += 1
        template[row][column]=number
        show()
        if number !=" ": # check repetition in the row, column or in the 3*3 grid if we don't delete
            if find_repetition_row(row, column, number) == True :
                print("This number already exists in this row!")
            if find_repetition_column(row, column, number) == True:
                print("This number already exists in this column!")
            if find_repetition_grid(row, column, number) == True:
                print("This number already exists in this grid!")
    else:
        print("You can't change that cell!")

def congratulate(steps):
    print("Your solution is correct!")
    print("You win!")
    print("Congratulations!")
    print("You made it in ", steps, " steps.")

def failed():
    print("Your solution is incorrect!")
    print("Please try again!")  

show()
print("")
while var == 1 :
    line = input("Please enter column, row and a number (0 to delete) separated by 'space' or press 'x' to quit): ")
    if line == "x":
        break
    if validation(line) == True:
        fill_cell(line)
    if filled_cells == 53:
        if check(solution,template) == True:
            congratulate(steps)
            break
        else:
            failed()
            break