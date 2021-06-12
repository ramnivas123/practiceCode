# input1 = ("enter the sentence").split()
# count = 0
# for x in input1:
    # count = count+1
# print("word is :",count)

input2 =input("enter a sentence" )
word = input("enter the word") 
areBaapRe = []
areBaapRe = input2.split()
count = 0
for x in range(0,len(areBaapRe)):
    if word == areBaapRe[x]:
        count = count+1
print("number of  a word",count)
