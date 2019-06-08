'''
Student marskheet
Will calculate their percentage and also show their grades
'''
print("*********************************" )
print("percentage Calculator")
print("*********************************" )
print("Enter the marks of your subjects")
s1=float(input("Marks for English: "))
s2=float(input("Marks for Mathematics: "))
s3=float(input("Marks for Urdu: "))
s4=float(input("Marks for Science: "))
s5=float(input("Marks for islamiat: "))
mobt=s1+s2+s3+s4+s5
maxm=500.0
if mobt>500:
    print("Sorry, you have entered the marks wrong....")
elif mobt<=500:
    percentage=(mobt/maxm)*100
    print("Your Percentage is : " + str(percentage))
    if percentage<50:
      print("You have failed")
    elif percentage>=50 and percentage<60:
      print("You hav acquired C Grade !!!")
    elif percentage>=60 and percentage<70:
      print("You have acquired B Grade !!!")         
    elif percentage>=70 and percentage<80:
      print("You have acquired A Grade !!! ")
    elif percentage>=80 and percentage<=100:
      print(" You have acquired A-1 Grade !!!")




         




