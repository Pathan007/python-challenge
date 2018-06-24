import os
import csv

names = []
candidates = {}
vote_count = 0

budget_data ='c:\\temp\\election_data.csv'

file_path = os.path.join('c:\\temp\\election_data.csv')

with open(file_path,newline='') as csvfile:
   
   
    reader = csv.reader(csvfile)

    header = next(reader)
    
    for row in reader:
        vote_count = vote_count + 1
        candidates_name = row[2]
        if candidates_name not in names:
            names.append(candidates_name)
            candidates[candidates_name] = 0
    
        candidates[candidates_name] = candidates[candidates_name] + 1

#for key, value in candidates.items():
#    candidates_percent[key] = round((value/vote_count) * 100, 2

#for key in candidates:

    #if candidates[key] > winner_count:

        #winner = key

       # winner_count = candidates[key]

        #print("Election Results")

print("-------------------------------------")

print("Total Votes: " + str(vote_count))

print("-------------------------------------")

for key in candidates:
    print(key + ": " + str(candidates[key]))
    print(key + ": " + str(candidates[key]/vote_count*100))
    if len(dict[maxVote])>1:
        print(dict[maxVote])[0]
        if __name__ == "__main__":
#for key, value in candidates.items():

#    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")

print("-------------------------------------")

print("Winner: " + winner)

print("-------------------------------------")

new_file = open("results.txt", "w")

ew_file.write("Election Results \n")

new_file.write("------------------------------------- \n")

new_file.write("Total Votes: " + str(vote_count) + "\n")

new_file.write("------------------------------------- \n")

for key, value in candidates.items():

    new_file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")

new_file.write("------------------------------------- \n")

new_file.write("Winner: " + winner + "\n")

new_file.write("------------------------------------- \n")
