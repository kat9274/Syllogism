import time
print("Type 'Help' at any time! (without quotes)")
Te = raw_input("What is your type? (A, E, I, or O)")
if Te == "O":
    Xa = raw_input("Is Your Input Type 1 or 2? >>> ")
    if Xa == "2":
        Ann = 1
        Qrr = 2
    elif Xa == "1":
        Ann = 3
        Qrr = 2
    elif Xa == "Help":
        print("Type 1 has 'is not' while type 2 has 'are not'. \n You will use type 1.")
        Ann = 3
        Qrr = 2
elif Te == "I":
    Ann = 2
    Qrr = 2
elif Te == "E":
    Ann = 2
    Qrr = 1
elif Te == "A":
    Ann = 0
    Qrr = 0
elif Te == "Help":
    print("A is in the format of (all a are b)\nWhile E is in the format of (no a are b)\nAnd I is in the format of (some a are b)\nO is in the format of (some a are not b/some a is not b). Now restart the program!")
    print("You will use A this time.")
    Ann = 0
    Qrr = 0
else:
    print("Your input is incorrect. You will use A type now.")
    Ann = 0
    Qrr = 0
S1 = raw_input("S1 >>> ")
S2 = raw_input("S2 >>> ")
Qr = ["All", "No", "Some"]
St = raw_input("What are the Subjects in S1? (DON'T include PNs!) >>> ")
Sv = raw_input("Are there Verbs in S2? (Y/N) >>> ")
if Sv == "Y":
    Vi = raw_input("What are they? >>> ")
elif Sv == "N":
    print("Ok")
else:
    print("Your input is incorrect. Reopen the program to retry.")
    time.sleep(5)
    exit()
Pe = raw_input("What are the Predicates in S2? >>> ")
An = ["are", "are not", "have", "is not"]
if Sv == "N":
    s = [Qr[Qrr], St, An[Ann], Pe]
if Sv == "Y":
    s = [St, Vi, Pe]
print(s)
