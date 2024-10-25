import matplotlib.pyplot as plt
import seaborn as sns


#open bozoroth scores with names of file above the scores
result_location = "bozorth_scores.txt"

with open(result_location, "r") as file:
    lines = file.readlines()

file.close()

#genuines and impostors frequency plot
genuine = []
impostors = []

#gather genuines and impostors from txt files
for i in range(1, len(lines), 2):
    line = lines[i+1].replace("\n", "")
    
    #if first number is the same it is the same fingerprint - genuine
    if lines[i][0:3] == lines[i][10:13]:
        lineNum = int(line)
        genuine.append(lineNum)
    #else it is an impostor
    else:
        lineNum = int(line)
        impostors.append(lineNum)



genuine_frequency= []
genuine_count = []


impostors_frequency= []
impostors_count = []

#create frequency and count
for i in range(0, max(genuine)+1):
    #calculate share (frequency) of genuines with each bozoroth scores 
    genuine_frequency.append(genuine.count(i)/len(genuine))
    genuine_count.append(i)

    #same for impostors
for i in range(0, max(impostors)+1):
    impostors_frequency.append(impostors.count(i)/len(impostors))
    impostors_count.append(i)

plt.plot(genuine_count, genuine_frequency,label="genuines")
plt.plot(impostors_count, impostors_frequency, label="impostors")
plt.xlim(-5,200)
plt.title('Bozoroth scores')
plt.xlabel('Bozoroth score')
plt.ylabel('Share of samples with the same bozoroth score')
plt.legend()



#similarity matrix plot, limit
similarity_matrix_list = []
tmp = []

#create similarity matrix from txt file
current = ""
for i in range(2, len(lines), 2):
    #create integer scores
    line = int(lines[i].replace("\n", ""))
    #when the first file changes change current, and append tmp(list of scores), new row in matrix
    if lines[i-1][0:9] != current:
        current = lines[i-1][0:9]
        
        if i > 3: 
            similarity_matrix_list.append(tmp)
        tmp = []
    tmp.append(line)

similarity_matrix_list.append(tmp)

plt.figure()

#plot similarity matrix
sm_mat = sns.heatmap(similarity_matrix_list,cmap='coolwarm', square=True, cbar_kws={'label': 'Bozoroth score'})

#set ticks to be less frequent
sm_mat.set_xticks(sm_mat.get_xticks()[::2])

sm_mat.set_yticks(sm_mat.get_yticks()[::2])


plt.title('Similarity Matrix')
plt.xlabel('Image sample number')
plt.ylabel('Image sample number')




#quality of images plot
quality_result_location = "quality.txt"
with open(quality_result_location, "r") as file:
    lines = file.readlines()

file.close()

quality_list = []

#each line contains one quality score
for i in range(0, len(lines)):
    line = lines[i].replace("\n", "")
    lineNum = int(line)
    quality_list.append(lineNum)

quality_frequency= []
quality_count = []

#caculate share of samples with a certain quality
for i in range(0, max(quality_list)+1):
    quality_frequency.append(quality_list.count(i)/len(quality_list))
    quality_count.append(i)

plt.figure()


plt.bar(quality_count, quality_frequency)
plt.xticks([0,1,2,3,4,5])
plt.xlabel('Quality')
plt.ylabel('Number of samples with quality')

plt.show()