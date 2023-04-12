import os
import csv 
file_load=os.path.join("C:/Users/macag/OneDrive/Desktop/Databook_camp/Week3python/Python_challange/Starter_Code/PyPoll/Resources/election_data.csv")
file_output=os.path.join("C:/Users/macag/OneDrive/Desktop/Databook_camp/Week3python/Python_challange/Starter_Code/PyPoll/Resources/election_results.csv")

Totalvotes=0

#OPens the input file to read
file= open (file_load,"r")
reader=csv.reader(file)

# reading the header
header = []
header = next (reader)

# moving records into an array
Candidate=[]

rows=[]
for row in reader:
    Candidate.append(row[2])
    rows.append(row)
    Totalvotes+=1
   


# closing the file
file.close()
print(Totalvotes)


# Loop to get the data
i=int (0)
Name=""
J=int(-1)
CandidateName=[]
CandidateVotes=[]

for Name in Candidate:
    if Name not in CandidateName:
        CandidateName.append(Name)
        CandidateVotes.append(1)
    else:
        CandidateIndex = CandidateName.index(Name)
        CandidateVotes[CandidateIndex] += 1



print (CandidateName)
print (CandidateVotes)

print (CandidateName[0],CandidateVotes[0])
print (CandidateName[1],CandidateVotes[1])
print (CandidateName[2],CandidateVotes[2])


# writting the report
with open (file_output,"w") as outfile:
    Highvote=0
    Winner=""
    outfile.write ("Election Results\n")
    outfile.write ("-------------------------------------\n")
    outfile.write (f"Total votes: {Totalvotes}\n")
    outfile.write ("-------------------------------------\n")
    for i in range(len(CandidateVotes)):
        VotePorcentage=CandidateVotes[i]/Totalvotes
        outfile.write (f"{CandidateName[i]}: {VotePorcentage}% ({CandidateVotes[i]})\n")
        if CandidateVotes[i]>Highvote:
            Winner=CandidateName[i]
    outfile.write ("-------------------------------------\n")
    outfile.write (f"Winner: {Winner}\n")
    outfile.write ("-------------------------------------\n")    






