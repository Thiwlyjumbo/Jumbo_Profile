import re

# สวัสดี: ชื่อ A1-001
def Hello_Name():
    name = str(input("Enter your name: "))
    surname = str(input("Enter your surname: "))
    print(f"Hello {name} {surname}")
    print(f"{name[:2]} {surname[:2]}")



# แลกเปลี่ยนเงฺฺิน A1-002
def Money_Exchange():
    coin = int(input("Enter Number of cions: "))

    c10 = coin // 10
    coin %= 10
    c5 = coin // 5
    coin %= 5
    c2 = coin // 2
    coin %= 2
    c1 = coin // 1
    coin %= 1
    print(f"10 = {c10}")
    print(f"5 = {c5}")
    print(f"2 = {c2}")
    print(f"1 = {c1}")



# ค่าสูงสุด A1-003
def Maximum_Value():
    num1 = int(input("Enter a Number 1:"))
    num2 = int(input("Enter a Number 2:"))
    num3 = int(input("Enter a Number 3:"))
    result = max(num1, num2, num3)
    print(result)



# ผมการสอบ A1-004
def Exam_Result():
    s1 = int(input("Enter a Score 1:"))
    s2 = int(input("Enter a Score 2:"))
    s3 = int(input("Enter a Score 3:"))

    ful_s1 = 10 / 2
    ful_s2 = 40 / 2
    ful_s3 = 50 / 2
    if s1 > ful_s1 or s2 > ful_s2 or s3 > ful_s3:
        print("Num Errer")
    elif s1 < ful_s1 or s2 < ful_s2 or s3 < ful_s3:
        print("fail")
    else:
        print("pass")



# ฤดูกาล A1-005
def Season():
    month = int(input("Enter a Month : "))
    day = int(input("Enter day of month : "))
    season = "None"
    if month < 1 or month > 12:
        print("Month Error.....")
        return
    if day < 1 or day > 31:
        print("Day Error")
        return
    elif month in [1, 2, 3]:
        if month % 3 == 0 and day >= 21:
            season = "spring"
        else:
            season = "winter"
    elif month in [4, 5, 6]:
        if month % 3 == 0 and day >= 21:
            season = "summer"
        else:
            season = "spring"
    elif month in [7, 8, 9]:
        if month % 3 == 0 and day >= 21:
            season = "fall"
        else:
            season = "summer"
    elif month in [10, 11, 12]:
        if month % 3 == 0 and day >= 21:
            season = "winter"
        else:
            season = "fall"
    print(season)




# หารลงตัว A1-006
def Divisible():
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    if num2 == 0:
        print("Error: connot divisible by zero")
    elif num1 % num2 == 0:
        print("yes")
    else:
        print("no")



# ตรวจสอบสระ A1-007
def Check_Vowel():
    string = input("Enter some word : ").lower()

    if string in ["a", "e", "i", "o", "u"]:
        print("yes")
    else:
        print("no")



# การตรวจสอบบัตรประชาชน A1-008
def ID_Card():
    id = input("Enter a number : ")
    if len(id) == 13 and id.isdigit():
        print("yes")
    else:
        print("no")



# ผ่าน/ไม่ผ่าน A1-009
def passed_failed():
    midterm = int(input("Enter midterm score : "))
    final = int(input("Enter final score : "))
    result = midterm + final
    print(result)

    if (midterm + final) >= 50:
        print("pass")
    else:
        print("fail")
        



# ค่าตั๋ว A1-010
def ticket_cost():
    age = int(input("Enter Age : "))
    stat = str(input("Enter Stat : "))

    if (age <= 18 and age >= 0) or (stat in ["s", "S"]):
        print("20")
    else:
        print("50")



# THEOS A1-011
def Theos():
    text = str(input("Enter Text : "))
    result = ""
    word = text[:1] 
    count = 1
    if not text:
        return
    for i in text[1:]:
        if i == word:
            count += 1
        else:
            result += (f"{count}{word}")
            word = i
            count = 1

    print(result + F"{count}{word}")



# สลับหมายเลข A1-012
def Swap_Numbers():
    number = int(input("Enter A number : "))
    revers = str(number)[::-1]
    if revers[:0] == "0":
        revers = revers[:1]
    mark = input("Enter mark : ")

    if mark == "+":
        print(f"{number} + {revers} = {int(number) + int(revers)}")
    if mark == "*":
        print(f"{number} * {revers} = {int(number) * int(revers)}")
    


# รหัสเซฟ A1-013
def Safe_Code():
    word = str(input("Enter word : "))
    num = int(input("Enter number : "))
    if word == "H" and num == 4567:
        print("safe unlocked")
    elif word == "H" and not num == 4567:
        print("safe locked - change digit")
    elif not word == "H" and num == 4567:
        print("safe locked - change char")
    else:
        print("safe locked")



# ค่าน้อยที่สุด A1-014
def Least_Value():
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    num3 = int(input("Enter number 3 : "))
    all = min(num1, num2, num3)
    print(all)



# รหัสผ่าน A1-015
def Pass_Word():
    First_Name = input("First name : ")
    Surname = input("Surname : ")
    age = int(input("Age : "))
    result = ""
    if len(First_Name) > 5 and len(Surname) > 5:
        result = First_Name[0:2] + Surname[:: -1][:1] + str(age % 10)
    else:
        result = First_Name[:1] + str(age) + Surname[:: -1][:1]
    print(result)



# การตรวจสอบบัตรนักศึกษา A1-016
def Student_ID():
    id = str(input("Enter ID : "))
    if id[2] in ["1", "6"] and id[3] in ["1", "6"]:
        print("yes")
    else:
        print("no")



# วันเกิด A1-017
def Birth_Day():
    print("***Firend 1 ***")
    firend1 = int(input("Enter Y : ")), int(input("Enter M : ")), int(input("Enter D : "))
    firend2 = int(input("Enter Y : ")), int(input("Enter M : ")), int(input("Enter D : "))
    result = "None"
    if firend1 < firend2:
        result = "1"
    elif firend1 > firend2:
        result = "2"
    elif firend1 == firend2:
        result = "0"
    print(result)



# ตัวเลขโรมันแบบง่าย A1-018
def Roman():
    num = int(input("Enter A Number : "))
    roman = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")
    if num < 0:
        print('Error : Please input positive number')
    elif (num == 0) or (num > 9):
        print('Error : Out of range')
    else:
        print(roman[(num -1)])



# เหมือนกันหมด A1-019
def All_Same():
    num1 = int(input("Number 1 : "))
    num2 = int(input("Number 2 : "))
    num3 = int(input("Number 3 : "))
    
    if num1 == num2 == num3:
        print("all the same")
    elif num1 != num2 and num1 != num3 and num2 != num3:
        print("all differrent")
    else:
        print("neither")



# การเพิ่ม/ลด A1-020
def up_douw():
    num1 = int(input("Enter A Number : "))
    num2 = int(input("Enter A Number : "))
    num3 = int(input("Enter A Number : "))
    if num1 == '' or num2 == '' or num3 == '':
        print("Number is None")
    elif (num1 < num2) and (num2 < num3):
        print("increasing")
    elif (num1 > num2) and (num2 > num3):
        print("decreasing")
    else:
        print("neither")


# ปีอธิกสุรทิน A1-021
def Leap_year():
    year = int(input("Enter Year : "))
    result = "None"

    if year < 1582:
        if (year % 4) == 0:
            result = "yes"
        else:
            result = "no"
    else:
        if (year % 400) == 0:
            result = "yes"
        elif (year % 100) == 0:
            result = "no"
        elif (year % 4) == 0:
            result = "yes"
        else:
            "no"
    print(result)


# ราศี A1-022
def Zodiac():
    day = int(input("Enter Day :"))
    month = int(input("Enter Month : "))
    zodiac = ["capricorn", "aquarius", "pisces",
            "aries", "taurus", "gemini",
            "cancer", "leo", "virgo",
            "libra", "scorpio", "sagittarius"]
    result = "None"

    if ((month == 1) and (day >= 20)) or ((month == 2) and (day <= 18)):
        result = zodiac[1] #aquarius
    elif ((month == 2) and (day >= 19)) or ((month == 3) and (day <= 20)):
        result = zodiac[2] #pisces
    elif ((month == 3) and (day >= 21)) or ((month == 4) and (day <= 19)):
        result = zodiac[3] #aries
    elif ((month == 4) and (day >= 20)) or ((month == 5) and (day <= 20)):
        result = zodiac[4] #taurus
    elif ((month == 5) and (day >= 21)) or ((month == 6) and (day <= 21)):
        result = zodiac[5] #gemini
    elif ((month == 6) and (day >= 22)) or ((month == 7) and (day <= 22)):
        result = zodiac[6] #cancer
    elif ((month == 7) and (day >= 23)) or ((month == 8) and (day <= 22)):
        result = zodiac[7] #leo
    elif ((month == 8) and (day >= 23)) or ((month == 9) and (day <= 22)):
        result = zodiac[8] #virgo
    elif ((month == 9) and (day >= 23)) or ((month == 10) and (day <= 23)):
        result = zodiac[9] #libra
    elif ((month == 10) and (day >= 24)) or ((month == 11) and (day <= 21)):
        result = zodiac[10] #scorpio
    elif ((month == 11) and (day >= 22)) or ((month == 12) and (day <= 21)):
        result = zodiac[11] #sagittarius
    else:
        result = zodiac[0] #capricorn

    print(result)
    


# ราศี A1-022 V.2
def Zodiac_V2():
    day = int(input())
    month = int(input())
    
    # เก็บข้อมูลเป็น (เดือน, วันที่ตัดรอบ, ชื่อราศี)
    thresholds = [
        (1, 19, "capricorn"), (2, 18, "aquarius"), (3, 20, "pisces"),
        (4, 19, "aries"), (5, 20, "taurus"), (6, 21, "gemini"),
        (7, 22, "cancer"), (8, 22, "leo"), (9, 22, "virgo"),
        (10, 23, "libra"), (11, 21, "scorpio"), (12, 21, "sagittarius")
    ]
    
    # ถ้าวันที่เกิน "วันที่ตัดรอบ" ของเดือนนั้น ให้ขยับไปราศีถัดไป
    # มกราคม (1) ถ้า > 19 จะกลายเป็นราศีลำดับถัดไป (aquarius)
    index = month - 1
    if day > thresholds[index][1]:
        index = (index + 1) % 12
        
    print(thresholds[index][2])



# สถานะน้ำ A1-023
def Water_Status():
    temp = int(input("Enter Temperature : "))
    Unit = input("Enter Temperature Unit : ")
    status = "None"
    if not Unit in ["C", "c", "F", "f"]:
        status = "Can't calculate please enter unit as F or C "

    elif Unit in ["C", "c"]:
        if temp == 0:
            status = "solid"
        elif (temp > 0) and (temp < 100):
            status = "liquid"
        elif temp == 100:
            status = "gas"

    elif Unit in ["F", "f"]:
        if temp == 32:
            status = "solid"
        elif (temp > 32) and (temp < 212):
            status = "liquid"
        elif temp == 212:
            status = "gas"
    print(status)




# ภาษีรถยนต์ A1-024
def Car_Tax():
    year = int(input("AD year : "))
    cc = int(input("cc engine size : "))
    tax = "None"

    if (year <= 1990):
        if (cc <= 1500):
            tax = "1250"
        elif (cc > 1500) and (cc >= 2000):
            tax = "1400"
        elif (cc > 2000):
            tax = "2000"
    elif (year > 1990) and (year <= 1999):
        if (cc <= 1500):
            tax = "1100"
        elif (cc > 1500) and (cc <= 2000):
            tax = "1300"
        elif (cc > 2000):
            tax = "1700"
    elif (year >= 2000):
        if (cc <= 1500):
            tax = "1000"
        elif (cc > 1500) and (cc <= 2000):
            tax = "1200"
        elif (cc > 2000):
            tax = "1500"
    print(tax)




# ไฟ่ 44 ใบ
def Card():
    print("Hello World")

Card()