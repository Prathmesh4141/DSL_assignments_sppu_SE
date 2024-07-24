# Option 1 = Average score
def average_marks():
    sum = 0
    for i in marks:
        if (i >= 0):
            sum=sum+i
    average_calc = sum/ no_of_students
    print("Average score of students is:",average_calc)

# Option 2 = High and low marks
def high_low_marks():
    maxi = marks[0] 
    mini = marks[0] 
    for i in range(len(marks)):
        if (maxi < marks[i] and marks[i] > -1):
            maxi = marks[i]
    for j in range(len(marks)):
        if (mini > marks[j] and marks[j] > -1):
            mini = marks[j]
    print(f"Highest score is: {maxi}\nLowest score is: {mini}")

# Option 3 = Absent count
def absent():
    absent_count = 0
    for i in marks:
        if (i < 0):
            absent_count+=1
    print(f"Total absent students are: {absent_count}")

# Option 4 = Highest frequency
def high_freq():
    freq_count = 0 
    fre_marks=0
    for i in range(len(marks)): 
        if (marks[i] >= 0): 
            count = 0
            for j in range(len(marks)):
                if (marks[i] == marks[j]):
                    count+=1
                    
            if (freq_count < count): 
                freq_count = count 
                fre_marks=marks[i]

    print(f"Highest frequency marks is:{fre_marks} with frequency {freq_count}")

#inputs------------------------------------------------------
no_of_students = int(input("enter total number of students in class: "))
marks = []
for i in range(no_of_students):
    k = int(input(f"Enter marks for student {i+1}: "))
    marks.append(k)

#function calling-----------
average_marks()
high_low_marks()
absent()
high_freq()
