

#Q. recursive program which disply  pattern( eg. input=5 output= * * * * *)

def Display(No):
    if (No > 0):
        print("*",end="  ")
        No = No - 1
        Display(No)

Display(5)
