s1 = raw_input("Sentence 1 >>> ")
s2 = raw_input("Sentence 2 >>> ")
ss1 = int(raw_input("What is the subject in S1 (1, 2, 3, 4, 5...) >>> "))
vs2 = int(raw_input("What is the verb in S2 (1, 2, 3, 4, 5...) >>> "))
ps2 = int(raw_input("What is the predicate in S2 (1, 2, 3, 4, 5...) >>> "))
ss1 = ss1 - 1
ps2 = ps2 - 1
vs2 = vs2 - 1
sentence1 = s1.split(" ")
sentence2 = s2.split(" ")
print sentence1[ss1]
print sentence2[vs2]
print sentence2[ps2]

