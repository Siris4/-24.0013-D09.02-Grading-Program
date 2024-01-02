'''
programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.",
"Function": "A piece of code that you can easily call over and over again.",
}

programming_dictionary["Loop"] = "The action of doing something over and over again.",

print(programming_dictionary)
'''

'''
Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"
'''

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
# student_scores = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    # print(key)
    # print(student_scores[key])
    score = student_scores[key]
    if score >= 91:
        student_scores[key] = "Outstanding"
    elif student_scores[key] >= 81:
        student_scores[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_scores[key] = "Acceptable"
    elif score <= 70:
        student_scores[key] = "Fail"
print(student_scores)

# 🚨 Don't change the code below 👇
# print(student_grades)