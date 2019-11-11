FillerList1 = ["all", "no", "some"]
FillerList2 = ["are", "are not", "have", "have no", "is", "is not"]

def FindType(In1, In2, S1, S2): #Both have to be split!
    if In1[S1] == "all":
        if In2[S2] == "some" or In2[S2] == "no":
            Word_List[0] = 2
        else:
            Word_List[0] = 0 #CAN BE 2 as well

    elif In1[S1] == "no":
        Word_List[0] = 2 #Can be 1 as well

    elif In1[S1] == "some":
        Word_List[0] = 2

    if In1[(S1 + 2)] == "are":
        if In2[(S2 + 2)] == "are not" or In[S1] == "no":
            Word_List[1] = 1
        else:
            Word_List[1] = 0

    elif In1[(S1 + 2)] == "have":
        if In2[(S2 + 2)] == "have":
            Word_List[1] = 1
        elif In2[(S2 + 2)] == "are":
            Word_List[1] = 3
        else:
            Word_List[1] = 2

    elif In1[(S1 + 2)] == "is":
        Word_List[1] = 5

    elif In1[(S1 + 2)] == "have no":
        Word_List[1] = 3
