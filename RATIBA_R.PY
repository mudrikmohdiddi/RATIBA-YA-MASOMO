def ratiba(x):
    print(x*7)
    print("This is your timetable for lean your subject")
    print("\n____________________________________________________")
    print("*MON:BUSINESS MATHEMATICS   + DEVELOPMENT STUDY      *")
    print("*TUE:INFORMATION TACHNOLOGY + ACCOUNTING             *")
    print("*WED:COMPUTER AMBLICATION   + COMMUNICATION SKILLS   *")
    print("*THU:ECONOMICS              + ACCOUNTING             *")
    print("*FRI:BUSINESS MATHEMATICS   + COMMUNICATION SKILLS   *")
    print("*SAT:DEVELOPMENT STUDY      + ECONOMICS              *")
    print("*SUN:COMPUTER AMBLICATION   + INFORMATION TACHNOLOGY *")
    print("_____________________________________________________")
from datetime import datetime
import calendar
s=0
while(s==0):
    t=datetime.now()
    d=t.strftime('%A')
    if(d==calendar.day_name[5]):
        print("\nTo day is:",d," ",t)
        print("\nYOU need to learn:DEVELOPMENT STUDY      + ECONOMICS")
        print("\nsoma kwamaendeleo yako na familia yako")
        print("N.B:To lean PYTHON is every day ")
        print(" ")
        r=input("You need show all timetable: Y/N:")
        if(r=="y" or r=="Y" or r==" Y" or r==" y"):
            print(ratiba(1))
        elif(r=="n" or r=="N" or r==" N" or r==" n"):
            print("\n ok you don't need to see whole timetable but-> N.B: usiache kufuatilia masomo yako")
        else:
            print("\nYou enter wrong input")
            print(" ")
    elif(d==calendar.day_name[6]):
        print("\nTo day is:",d," ",t)
        print("\nYOU need to learn:COMPUTER AMBLICATION   + INFORMATION TACHNOLOGY")
        print("\nsoma kwamaendeleo yako na familia yako")
        print("N.B:To lean PYTHON is every day ")
        print(" ")
        r=input("You need show all timetable: Y/N:")
        if(r=="y" or r=="Y" or r==" Y" or r==" y"):
            print(ratiba(1))
        elif(r=="n" or r=="N" or r==" N" or r==" n"):
            print("\n ok you don't need to see whole timetable but-> N.B: usiache kufuatilia masomo yako")
        else:
            print("\nYou enter wrong input")
            print(" ")
    elif(d==calendar.day_name[0]):
        print("\nTo day is:",d," ",t)
        print("\nYOU need to learn:BUSINESS MATHEMATICS   + DEVELOPMENT STUDY")
        print("\nsoma kwamaendeleo yako na familia yako")
        print("N.B:To lean PYTHON is every day ")
        print(" ")
        r=input("You need show all timetable: Y/N:")
        if(r=="y" or r=="Y" or r==" Y" or r==" y"):
            print(ratiba(1))
        elif(r=="n" or r=="N" or r==" N" or r==" n"):
            print("\n ok you don't need to see whole timetable but-> N.B: usiache kufuatilia masomo yako")
        else:
            print("\nYou enter wrong input")
            print(" ")
    elif(d==calendar.day_name[1]):
        print("\nTo day is:",d," ",t)
        print("\nYOU need to learn:INFORMATION TACHNOLOGY + ACCOUNTING  ")
        print("\nsoma kwamaendeleo yako na familia yako")
        print("N.B:To lean PYTHON is every day ")
        print(" ")
        r=input("You need show all timetable: Y/N:")
        if(r=="y" or r=="Y" or r==" Y" or r==" y"):
            print(ratiba(1))
        elif(r=="n" or r=="N" or r==" N" or r==" n"):
            print("\n ok you don't need to see whole timetable but-> N.B: usiache kufuatilia masomo yako")
        else:
            print("\nYou enter wrong input")
            print(" ")
    elif(d==calendar.day_name[2]):
        print("\nTo day is:",d," ",t)
        print("\nYOU need to learn:COMPUTER AMBLICATION   + COMMUNICATION SKILLS")
        print("\nsoma kwamaendeleo yako na familia yako")
        print("N.B:To lean PYTHON is every day  ")
        print(" ")
        r=input("You need show all timetable: Y/N:")
        if(r=="y" or r=="Y" or r==" Y" or r==" y"):
            print(ratiba(1))
        elif(r=="n" or r=="N" or r==" N" or r==" n"):
            print("\n ok you don't need to see whole timetable but-> N.B: usiache kufuatilia masomo yako")
        else:
            print("\nYou enter wrong input")
            print(" ")
    elif(d==calendar.day_name[3]):
        print("\nTo day is:",d," ",t)
        print("\nYOU need to learn:ECONOMICS              + ACCOUNTING ")
        print("\nsoma kwamaendeleo yako na familia yako")
        print("N.B:To lean PYTHON is every day  ")
        print(" ")
        r=input("You need show all timetable: Y/N:")
        if(r=="y" or r=="Y" or r==" Y" or r==" y"):
            print(ratiba(1))
        elif(r=="n" or r=="N" or r==" N" or r==" n"):
            print("\n ok you don't need to see whole timetable but-> N.B: usiache kufuatilia masomo yako")
        else:
            print("\nYou enter wrong input")
            print(" ")
    elif(d==calendar.day_name[4]):
        print("\nTo day is:",d," ",t)
        print("\nYOU need to learn:BUSINESS MATHEMATICS   + COMMUNICATION SKILLS")
        print("\nsoma kwamaendeleo yako na familia yako")
        print("N.B:To lean PYTHON is every day  ")
        print(" ")
        r=input("You need show all timetable: Y/N:")
        if(r=="y" or r=="Y" or r==" Y" or r==" y"):
            print(ratiba(1))
        elif(r=="n" or r=="N" or r==" N" or r==" n"):
            print("\n ok you don't need to see whole timetable but-> N.B: usiache kufuatilia masomo yako")
        else:
            print("\nYou enter wrong input")
            print(" ")
    else:
        print("\nNot define ",*4)
        
        


