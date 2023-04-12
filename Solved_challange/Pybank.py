import os
import csv 


file_load=os.path.join("C:/Users/macag/OneDrive/Desktop/Databook_camp/Week3python/Python_challange/Starter_Code/PyBank/Resources/budget_data.csv")
file_output=os.path.join("C:/Users/macag/OneDrive/Desktop/Databook_camp/Week3python/Python_challange/Starter_Code/PyBank/Resources/analysis_data.csv")

Totalmonths=0
Totalnet=0
Change=0
Greatestincrease=0
Greatestincreasemonth=""
Greatestdecrease=0
Greatestdecreasemonth=""

#OPens the input file to read
file= open (file_load,"r")
reader=csv.reader(file)

# reading the header
header = []
header = next (reader)

# moving records into an array
rows=[]
for row in reader:
    rows.append(row)
    Totalmonths+=1

# closing the file
file.close()
print (rows)

# Loop to get the data
i=int (0)
for i in range(0,int(Totalmonths)):

    Totalnet+=int(rows[i][1])

    print(i, " ",Totalnet," ",int(rows[i][1])," ",rows[i][0])


    if int(rows[i][1]) > Greatestincrease:
        Greatestincrease=int(rows[i][1])
        Greatestdecreasemonth=rows[i][0]

    if int(rows[i][1]) < Greatestdecrease:
        Greatestdecrease=int(rows[i][1])
        Greatestincreasemonth=rows[i][0]

    print(int(rows[i][1])," ",Greatestincreasemonth, " ", Greatestincrease)
    print(int(rows[i][1])," ",Greatestdecreasemonth, " ", Greatestdecrease)

    Average = Totalnet / Totalmonths

# writting the report
with open (file_output,"w") as outfile:

    outfile.write ("Financial Analysis\n")
    outfile.write ("-------------------------------------\n")
    outfile.write (f"Total months: {Totalmonths}\n")
    outfile.write(f"Total: {Totalnet}\n")
    outfile.write(f"Average Change: ${Average}\n")
    outfile.write(f"Greatest Increase in Profits: {Greatestincreasemonth} (${Greatestincrease})\n")
    outfile.write(f"Greatest Decrease in Profits: {Greatestdecreasemonth} (${Greatestdecrease})\n")
