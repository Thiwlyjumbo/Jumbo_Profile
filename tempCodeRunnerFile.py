# นับเลขคู่และเลขคี่ A1-026
def Even_odd():
    num = [int(input("Enter Number 1 : ")), 
           int(input("Enter Number 2 : ")),
             int(input("Enter Number 3 : "))]
    even = 0
    odd = 0

    for i in num:
        if (i % 2) == 0:
            even += 1
        else:
            odd += 1

    print(f"even {even}")
    print(f"odd {odd}")
        
Even_odd()