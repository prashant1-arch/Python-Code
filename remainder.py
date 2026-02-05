hindi=int(input("Enter Hindi Marks: "))
english=int(input("Enter English Marks: "))
maths=int(input("Enter Maths Marks: "))
total_marks=hindi+english+maths
print("Total Marks:",total_marks)
percentage=(total_marks/300)*100
print("Percentage:",percentage)
if percentage>=90:
    print("Grade: A")
elif percentage>=80:
    print("Grade: B")
elif percentage>=70:
    print("Grade: C")
elif percentage>=60:
    print("Grade: D")
else:
    print("fail")
    
    