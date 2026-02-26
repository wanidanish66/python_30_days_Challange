# This code generates multiplication tables from 2 to 21 and saves each table in a separate text file 
# within a folder named "tables". Each file is named "table_n.txt", 
# where n is the number for which the multiplication table is generated.

def generateTable(n):     # created the function called generateTable
    table = ""            # defined the variable value as empty where the tables will be stored
    for i in range(1,11):       # use for loop from 1 to 11
        table += f"{n} x {i} = {n*i} \n"   # generates the table of a given number and stores that table into the txt file table
        file = open(f"tables/table_{n}","w")   # opens the tables folder in write mode and creates the new txt file for every table
        file.write(table)                      # writes the table in the txt files
        file.close()

for i in range(2,22):   # for loop to generate numbers from 2 to 21 whose table will be generated
    generateTable(i)    # calls the function which then generates the table from 2 to 21 and stores them in different txt files