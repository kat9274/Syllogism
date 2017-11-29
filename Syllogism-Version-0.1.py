s1 = raw_input("Sentence 1 >>> ")
s2 = raw_input("Sentence 2 >>> ")
#get sentences (for nothing)
ss1 = int(raw_input("What is the subject in S1 (1, 2, 3, 4, 5...) >>> "))
vs2 = int(raw_input("What is the verb in S2 (1, 2, 3, 4, 5...) >>> "))
ps2 = int(raw_input("What is the predicate in S2 (1, 2, 3, 4, 5...) >>> "))
#get the Syllogism words
ss1 = ss1 - 1
ps2 = ps2 - 1
vs2 = vs2 - 1
#make it User friendly by making it start at 1
sentence1 = s1.split(" ")
sentence2 = s2.split(" ")
#split the sentences
print sentence1[ss1]
print sentence2[vs2]
print sentence2[ps2]
#print them
#13 lines instead of 150!
