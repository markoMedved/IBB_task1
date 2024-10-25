import numpy as np

#first part - getting classes
result_location = "pcasys.out"

with open(result_location, "r") as file:
    lines = file.readlines()
file.close()

arch = []
lloop = []
rloop = []
scar = []
tented_arch = []
whorl = []



for line in lines:
    #parse through file to get filenames into lists of classes
    fingerprint_class = line[25:26] 
    if fingerprint_class == 'R':
        rloop.append(line[0:5])   

    elif fingerprint_class == 'A':
        arch.append(line[0:5])

    elif fingerprint_class == 'L':
        lloop.append(line[0:5])

    elif fingerprint_class == 'S':
        scar.append(line[0:5])

    elif fingerprint_class == 'T':
        tented_arch.append(line[0:5])

    elif fingerprint_class == 'W':
        whorl.append(line[0:5])



#reading comparisons
result_location = "bozorth_scores.txt"

with open(result_location, "r") as file:
    lines = file.readlines()

file.close()

#get lists of impostors and genuines bozorth scores from txt file and lists of files in class
def get_impostors_and_genuines(lines, fp_class_list):
    
    genuine = []
    impostors = []
    #already compared list
    already_compared = []

    current = ""

    #get the impostor and genuine comparisons
    for i in range(2, len(lines), 2):
        line = int(lines[i].replace("\n", ""))
        if lines[i-1][0:9] != current:
            already_compared.append(current)
            current = lines[i-1][0:9]

        #only use samples from the same class(names in the fp_class_list)
        if lines[i-1][0:5] in fp_class_list and lines[i-1][10:15] in fp_class_list:
        
            if not (lines[i-1][10:19] in already_compared or lines[i-1][10:19] == current):
                if lines[i-1][0:3] == lines[i-1][10:13]:
                    lineNum = int(line)
                    genuine.append(lineNum)
                else:
                    lineNum = int(line)
                    impostors.append(lineNum)
    return ( genuine,impostors)

#get scores(tuple) for all classes
lloop_impostors_genuines = get_impostors_and_genuines(lines, lloop)
rloop_impostors_genuines = get_impostors_and_genuines(lines, rloop)
arch_impostors_genuines = get_impostors_and_genuines(lines, arch) #empty
scar_impostors_genuines = get_impostors_and_genuines(lines, scar) #empty
tented_arch_impostors_genuines = get_impostors_and_genuines(lines, tented_arch) #empty
whorl_impostors_genuines = get_impostors_and_genuines(lines, whorl)





#finding the best treshold, by searching trough 
def get_treshold_and_acc(impostors_and_genuines):
    classification_acc = []
    x = 10
    for treshold in range(x,50):
        correctly_classified = 0
        for el in impostors_and_genuines[0]:
            if el >=treshold:
                correctly_classified+=1

        for el in impostors_and_genuines[1]:
            if el < treshold:
                correctly_classified+=1

        classification_acc.append(correctly_classified/(len(impostors_and_genuines[0]) + len(impostors_and_genuines[1])))

    best_treshold = x + classification_acc.index(max(classification_acc))

    print("treshold is: " + str(best_treshold))
    #return the 
    print("accuracy is : " + str(max(classification_acc)))
    return (best_treshold, max(classification_acc))

(trsh1, acc1) = get_treshold_and_acc(lloop_impostors_genuines)

(trsh2, acc2) =get_treshold_and_acc(rloop_impostors_genuines)

(trsh3, acc3) = get_treshold_and_acc(whorl_impostors_genuines)

#count impostors and genuines from all classes
comparison_cnt = len(lloop_impostors_genuines[0]) + len(lloop_impostors_genuines[1]) +len(rloop_impostors_genuines[0]) + len(rloop_impostors_genuines[1]) +len(whorl_impostors_genuines[0]) + len(whorl_impostors_genuines[1])

#weight based on amount of comparisons
upper =  (len(lloop_impostors_genuines[0]) + len(lloop_impostors_genuines[1]))*acc1 +(len(rloop_impostors_genuines[0]) + len(rloop_impostors_genuines[1]))*acc2 +(len(whorl_impostors_genuines[0]) + len(whorl_impostors_genuines[1]))*acc3

probabilities = np.array([(len(lloop_impostors_genuines[0]) + len(lloop_impostors_genuines[1]))/comparison_cnt,
       (len(rloop_impostors_genuines[0]) + len(rloop_impostors_genuines[1]))/comparison_cnt,
           (len(whorl_impostors_genuines[0]) + len(whorl_impostors_genuines[1]))/comparison_cnt ])

values_acc = [acc1, acc2, acc3]


#total accuracy
acc = np.sum(probabilities*values_acc)
variance = np.sum(probabilities*(values_acc - acc)**2)
std_dev = np.sqrt(variance)


values_tresh = [trsh1, trsh2, trsh3]
tresh = np.sum(probabilities*values_tresh)
tresh_var = np.sum(probabilities*(values_tresh - tresh)**2)
tresh_std_dev = np.sqrt(tresh_var)

print(tresh, tresh_std_dev, acc, std_dev)

