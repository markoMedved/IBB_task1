result_location = "bozorth_scores.txt"

with open(result_location, "r") as file:
    lines = file.readlines()

file.close()


genuine = []
impostors = []

#already compared list
already_compared = []

current = ""


#get the impostor and genuine comparisons
current = ""
for i in range(2, len(lines), 2):
    #make integer scores
    line = int(lines[i].replace("\n", ""))
    #set current to the first file being compared 
    if lines[i-1][0:9] != current:
        already_compared.append(current)
        current = lines[i-1][0:9]
    #don't compare a sample with itself, and don't compare samples that have already been compared
    if not (lines[i-1][10:19] in already_compared or lines[i-1][10:19] == current):
        if lines[i-1][0:3] == lines[i-1][10:13]:
            lineNum = int(line)
            genuine.append(lineNum)
        else:
            lineNum = int(line)
            impostors.append(lineNum)
       


classification_acc = []

#finding the best treshold, by searching through logical possibilites
x = 5
for treshold in range(x,50):
    correctly_classified = 0
    #count number of correctly classified genuines
    for el in genuine:
        if el >=treshold:
            correctly_classified+=1
    #count number of correctly classified impostors
    for el in impostors:
        if el < treshold:
            correctly_classified+=1
    
    classification_acc.append(correctly_classified/(len(genuine) + len(impostors)))

best_treshold = x + classification_acc.index(max(classification_acc))


print("treshold is: " + str(best_treshold))
print("accuracy is : " + str(classification_acc[classification_acc.index(max(classification_acc))]))

