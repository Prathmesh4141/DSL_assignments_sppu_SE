# List of students who play both cricket and badminton
# List of students who play either cricket or badminton but not both
# Number of students who play neither cricket nor badminton
# Number of students who play cricket and football but not badminton
# Number of students who do not play any game
# List of students who play at least one game
# List of students who play all three games

def students_playing_both(cricket, badminton):
    both = []
    for student in cricket:
        if student in badminton:
            both.append(student)
    return both

def students_playing_either_but_not_both(cricket, badminton):
    either_but_not_both = []
    for student in cricket:
        if student not in badminton:
            either_but_not_both.append(student)
    for student in badminton:
        if student not in cricket:
            either_but_not_both.append(student)
    return either_but_not_both

def students_playing_neither(cricket, badminton, total_students):
    neither = total_students[:]
    for student in cricket:
        if student in neither:
            neither.remove(student)
    for student in badminton:
        if student in neither:
            neither.remove(student)
    return len(neither)

def students_playing_cricket_and_football_but_not_badminton(cricket, football, badminton):
    cricket_and_football_but_not_badminton = []
    for student in cricket:
        if student in football and student not in badminton:
            cricket_and_football_but_not_badminton.append(student)
    return len(cricket_and_football_but_not_badminton)

def students_playing_no_game(cricket, badminton, football, total_students):
    no_game = total_students[:]
    for student in cricket:
        if student in no_game:
            no_game.remove(student)
    for student in badminton:
        if student in no_game:
            no_game.remove(student)
    for student in football:
        if student in no_game:
            no_game.remove(student)
    return len(no_game)

def students_playing_at_least_one_game(cricket, badminton, football):
    at_least_one_game = []
    for student in cricket:
        if student not in at_least_one_game:
            at_least_one_game.append(student)
    for student in badminton:
        if student not in at_least_one_game:
            at_least_one_game.append(student)
    for student in football:
        if student not in at_least_one_game:
            at_least_one_game.append(student)
    return at_least_one_game

def students_playing_all_three(cricket, badminton, football):
    all_three = []
    for student in cricket:
        if student in badminton and student in football:
            all_three.append(student)
    return all_three






total_students=[]
total1 = int(input("Enter total number of students:\t"))
for i in range(total1):
    k = int(input())
    total_students.append(k)

cricket= []
total2 = int(input("Total number of CRICKET players:\t"))
for i in range(total2):
    k = int(input(f"Roll number of player {i+1}:\t"))
    cricket.append(k)

badminton= []
total3 = int(input("Total number of BADMINTON players:\t"))
for i in range(total3):
    k = int(input(f"Roll number of player {i+1}:\t"))
    badminton.append(k)


football = []
total4 = int(input("Total number of FOOTBALL players:\t"))
for i in range(total4):
    k = int(input(f"Roll number of player {i+1}:\t"))
    football.append(k)



print("List of students who play both cricket and badminton:", students_playing_both(cricket, badminton))
print("List of students who play either cricket or badminton but not both:", students_playing_either_but_not_both(cricket, badminton))
print("Number of students who play neither cricket nor badminton:", students_playing_neither(cricket, badminton, total_students))
print("Number of students who play cricket and football but not badminton:", students_playing_cricket_and_football_but_not_badminton(cricket, football, badminton))
print("Number of students who do not play any game:", students_playing_no_game(cricket, badminton, football, total_students))
print("List of students who play at least one game:", students_playing_at_least_one_game(cricket, badminton, football))
print("List of students who play all three games:", students_playing_all_three(cricket, badminton, football))



