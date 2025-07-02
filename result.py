while True:
    print("---student grading system---")
    print("enter for all subjects")
    print("each subject carry 50 marks")

    urdu = int(input("urdu marks: "))
    english = int(input("english marks: "))
    science = int(input("science marks: "))
    comp = int(input("comp marks: "))
    maths = int(input("maths marks: "))

    total = urdu + english + science + comp + maths
    percentage = (total / 250) * 100
    grade = ""

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60: 
        grade = "D"
    else:
        grade = "fail"
    
    print("total: ",total)
    print("grade: ",grade)
    print("percentage: ",percentage)