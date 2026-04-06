# A B Problem 0000
def A_B(a, b):
    result = (a + b)
    print(f"sum is {result}")

#A_B(int(input("Enter A : ")), int(input("Enter B : ")))


# Grading 0001
def Grading():
    col = int(input())
    mid = int(input())
    final = int(input())
    result = (col + mid + final)

    if (result >= 80) and (result <= 100):
        print("A")
    elif (result >= 75) and (result <= 79):
        print("B+")
    elif (result >= 70) and (result <= 74):
        print("B")
    elif (result >= 65) and (result <= 69):
        print("C+")
    elif (result >= 60) and (result <= 64):
        print("C")
    elif (result >= 55) and (result <= 59):
        print("D+")
    elif (result >= 50) and (result <= 54):
        print("D")
    else:
        print("F")



# min max 0002
def min_max():
    n = int(input())
    num = []
    for i in range(n):
        data = int(input())
        num.append(data)
    
    print(min(num))
    print(max(num))
   

min_max()



