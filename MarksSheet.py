# First Statement

# Marks Sheet Grade
# Transcript data

courses = {
    "Computer Fundamentals": 20,
    "Internet & WWW Fundamentals": 40,
    "Word Processing Fundamentals": 20,
    "Spreadsheet Fundamentals": 30,
    "Presentation Fundamentals": 30,
    "Database Fundamentals": 40,
    "Digital Media Fundamentals": 25,
    "Web Design Fundamentals": 35,
}

# Marks obtained by the student
marks_obtained = {
    "Computer Fundamentals": 18,
    "Internet & WWW Fundamentals": 35,
    "Word Processing Fundamentals": 19,
    "Spreadsheet Fundamentals": 28,
    "Presentation Fundamentals": 29,
    "Database Fundamentals": 36,
    "Digital Media Fundamentals": 22,
    "Web Design Fundamentals": 30,
}

# Calculate total marks and percentage
total_max_marks = sum(courses.values())
total_obtained_marks = sum(marks_obtained.values())
percentage = (total_obtained_marks / total_max_marks) * 100

# Determine grade
if percentage >= 90:
    grade = "A1"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Determine pass/fail status
pass_status = all(
    marks_obtained[course] >= (0.5 * max_marks)
    for course, max_marks in courses.items()
)

# Print the result
print("Transcript of Marks")
print("Student Name: Mohammad Fahad Ahmed")
print("Program: Microsoft Unlimited Potential Curriculum")
print(f"Total Marks Obtained: {total_obtained_marks} / {total_max_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Status: {'Pass' if pass_status else 'Fail'}")

# Second Statements

# ٹرانسکرپٹ ڈیٹا

courses = {
    "کمپیوٹر کے بنیادی اصول": 20,
     "انٹرنیٹ اور ڈبلیو ڈبلیو ڈبلیو کے بنیادی اصول": 40,
     "ورڈ پروسیسنگ کے بنیادی اصول": 20,
     "اسپریڈشیٹ کے بنیادی اصول": 30,
     "پریزنٹیشن کے بنیادی اصول": 30,
     "ڈیٹا بیس کے بنیادی اصول": 40,
     "ڈیجیٹل میڈیا کے بنیادی اصول": 25,
     "ویب ڈیزائن کے بنیادی اصول": 35,
 }

 # طالب علم کے حاصل کردہ نمبر
marks_obtained = {
     "کمپیوٹر کے بنیادی اصول": 18,
     "انٹرنیٹ اور ڈبلیو ڈبلیو ڈبلیو کے بنیادی اصول": 35,
     "ورڈ پروسیسنگ کے بنیادی اصول": 19,
     "اسپریڈشیٹ کے بنیادی اصول": 28,
     "پریزنٹیشن کے بنیادی اصول": 29,
     "ڈیٹا بیس کے بنیادی اصول": 36,
     "ڈیجیٹل میڈیا کے بنیادی اصول": 22,
     "ویب ڈیزائن کے بنیادی اصول": 30,
 }

 # کل نمبروں اور فیصد کا حساب لگائیں۔
total_max_marks = sum(courses.values())
total_obtained_marks = sum(marks_obtained.values())
percentage = (total_obtained_marks / total_max_marks) * 100

 # گریڈ کا تعین کریں۔
if percentage >= 90:
     گریڈ = "A1"
elif percentage >= 80:
     گریڈ = "A"
elif percentage >= 70:
     گریڈ = "B"
elif percentage >= 60:
     گریڈ = "C"
elif percentage >= 50:
     گریڈ = "D"
else:
     گریڈ = "F"

# پاس/فیل کی حیثیت کا تعین کریں۔
# پاس_سٹیٹس = تمام (حاصل کردہ نمبر[کورس] >= (0.5 * زیادہ سے زیادہ_نمبر) # type: ignore
#    کورس کے لیے، courses.items() میں max_marks)

pass_status = all(
    marks_obtained[course] >= (0.5 * max_marks)
    for course, max_marks in courses.items()
)

# نتیجہ پرنٹ کریں۔
print ("نشانات کی نقل")
print ("طالب علم کا نام: محمد فہد احمد")
print ("پروگرام: مائیکروسافٹ لامحدود ممکنہ نصاب")
print (f"کل حاصل کردہ نمبر: {total_obtained_marks} / {total_max_marks}")
print (f"فی صد: {percentage:.2f}%")
print (f"گریڈ: {گریڈ}")
print (f"سٹیٹس: {'Pass' if pass_status else 'Fail'}")

# Third Statement

def generate_transcript(obtained_score):
    transcript = """
    Microsoft Unlimited Potential Curriculum Transcript of Marks
    
    Transcript No.: CTLC-13/08/01183
    Name of Student: Mohammad Fahad Ahmed
    Student/Batch ID: 08-UP-13510
    Program: Microsoft Unlimited Potential Curriculum
    Study Period: October 08 to January 09
    Issue Date: February 16, 2009
    
    Course ID       Course Title                      Max Score
    MSUP001         Computer Fundamentals             20
    MSUP002         Internet & WWW Fundamentals       40
    MSUP003         Word Processing Fundamentals      20
    MSUP004         Spreadsheet Fundamentals         30
    MSUP005         Presentation Fundamentals        30
    MSUP006         Database Fundamentals            40
    MSUP007         Digital Media Fundamentals        25
    MSUP008         Web Design Fundamentals          35
    
    Total Score: 240
    Percentage: 32%
    
    Academic Head, CTLC
    """
    return transcript

# Print the transcript
print(generate_transcript(200))

# Fourth Statement

def generate_transcript():
    # Transcript data
    max_score = 240  # Total maximum score
    obtained_score = 77  # Example obtained score (آپ اسے تبدیل کر سکتے ہیں)

    # Calculate percentage
    percentage = (obtained_score / max_score) * 100

    # Determine grade based on percentage
    if percentage >= 90:
        grade = "A1"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Transcript text
    transcript = f"""
    Microsoft Unlimited Potential Curriculum Transcript of Marks
    
    Transcript No.: CTLC-13/08/01183
    Name of Student: Mohammad Fahad Ahmed
    Student/Batch ID: 08-UP-13510
    Program: Microsoft Unlimited Potential Curriculum
    Study Period: October 08 to January 09
    Issue Date: February 16, 2009
    
    Course ID       Course Title                      Max Score
    MSUP001         Computer Fundamentals             20
    MSUP002         Internet & WWW Fundamentals       40
    MSUP003         Word Processing Fundamentals      20
    MSUP004         Spreadsheet Fundamentals         30
    MSUP005         Presentation Fundamentals        30
    MSUP006         Database Fundamentals            40
    MSUP007         Digital Media Fundamentals        25
    MSUP008         Web Design Fundamentals          35
    
    Total Score: {max_score}
    Obtained Score: {obtained_score}
    Percentage: {percentage:.2f}%
    Grade: {grade}
    
    Academic Head, CTLC
    """
    return transcript

# Print the transcript
print(generate_transcript())

# Fifth Statement

def generate_transcript(obtained_score):
    # Transcript data
    max_score = 240  # Total maximum score

    # Calculate percentage
    percentage = (obtained_score / max_score) * 100

    # Determine grade based on percentage
    if percentage > 90:
        grade = "A1"
    elif percentage > 80:
        grade = "A"
    elif percentage > 70:
        grade = "B"
    elif percentage > 60:
        grade = "C"
    elif percentage > 50:
        grade = "D"
    else:
        grade = "F"

    # Transcript text
    transcript = f"""
    Microsoft Unlimited Potential Curriculum Transcript of Marks
    
    Obtained Score: {obtained_score}
    Total Score: {max_score}
    Percentage: {percentage:.2f}%
    Grade: {grade}
    """
    return transcript

# Loop to generate transcript for scores from 1 to 100
for score in range(1, 241):
    print(generate_transcript(score))