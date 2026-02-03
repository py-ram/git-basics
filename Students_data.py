Student_name=input("Enter student name")

Marks_Maths  = int(input("Marks in Maths"))
Marks_Science = int(input("Marks in Science"))
Marks_English = int(input("Marks in English"))

if Marks_Maths < 0 :
    print("invalid marks entered")
    if Marks_Science < 0 :
        print("invalid marks entered")
    if Marks_English < 0 :
        print("invalid marks entered")
    if Marks_Maths >100:
        print("invalid marks entered")
    if Marks_Science >100:
        print("invalid marks entered")
    if Marks_English >100:
        print("invalid marks entered")
    else:
        print("Go ahead and enter your marks")   

Total_marks = Marks_Maths + Marks_Science + Marks_English
print(Total_marks)

Average_marks = Total_marks / 3
print(Average_marks)

Status = ""
if (Marks_Maths >= 40) and (Marks_Science >= 40) and (Marks_English >= 40):
    Status = "Pass"
else:
    Status = "Fail"
print(Status)
Grade = ""
if Average_marks > 75:
    Grade = "Grade A"
elif Average_marks >= 60  and Average_marks <75:
    Grade = "Grade B"
elif Average_marks >= 40 and Average_marks <60:
    Grade = "Grade C"
print(Grade)
print("="*45)
print(f"Student Name:{Student_name}")
print(f"Enter Maths marks: {Marks_Maths}")
print(f"Enter Science marks: {Marks_Science}")
print(f"Enter English marks: {Marks_English}")
print(f"Total_marks: {Total_marks}")
print(f"Average_marks: {Average_marks}")
print(f"Status: {Status}")
print(f"Grade: {Grade}")
print("="*45)
