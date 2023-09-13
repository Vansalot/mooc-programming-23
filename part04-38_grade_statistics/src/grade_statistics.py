def input_grades():
    # Asks the user for grades and returns two lists of grades
    exam_points_list = []
    exercises_list = []

    while True:
        grades = input("Exam points and exercises completed(0-20 0-100): ")
        if grades == '':
            break
        gradeslist = grades.split()
        exam_points_list.append(int(gradeslist[0]))
        exercises_list.append(int(gradeslist[1]))

    return exam_points_list, exercises_list

def exercises_to_points(exercises_list):
    exercises_points_list = []
    for number in exercises_list:
        exercises_points_list.append(number // 10) 
    
    return exercises_points_list

def print_statistics(exam_points_list, exercises_points_list):
    # Gets lists of exam points and exercises and prints stats.
    points_average = (sum(exam_points_list) + sum(exercises_points_list)) / len(exam_points_list)
    grade_distribution = check_grade_distribution(exam_points_list, exercises_points_list)
    pass_percentage = (sum(grade_distribution) - grade_distribution[-1]) / sum(grade_distribution) * 100

    print("Statistics: ")
    print(f"Points average: {points_average}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    
    print_grade_distribution(grade_distribution)

def check_grade_distribution(exam_points_list, exercises_points_list):
    # loop through points and assign grade
    # return a list of grades (yes, dict would be better...)
    grade_5 = 0
    grade_4 = 0
    grade_3 = 0
    grade_2 = 0
    grade_1 = 0
    grade_0 = 0

    for index in range(0, len(exam_points_list)):
        if exam_points_list[index] < 10:
            grade_0 += 1
            continue
        elif exam_points_list[index] + exercises_points_list[index] < 15:
            grade_0 += 1
            continue
        elif exam_points_list[index] + exercises_points_list[index] < 18:
            grade_1 += 1
            continue
        elif exam_points_list[index] + exercises_points_list[index] < 21:
            grade_2 += 1
            continue
        elif exam_points_list[index] + exercises_points_list[index] < 24:
            grade_3 += 1
            continue
        elif exam_points_list[index] + exercises_points_list[index] < 28:
            grade_4 += 1
            continue
        elif exam_points_list[index] + exercises_points_list[index] < 31:
            grade_5 += 1
            continue

    gradelist = [grade_5, grade_4, grade_3, grade_2, grade_1, grade_0]
    return gradelist

def print_grade_distribution(grade_distribution):
    # Prints grade distribution chart based on the grades.
    print("Grade distribution: ")
    printgrade = 5
    for grade in grade_distribution:
        currentgrade = '  ' +  str(printgrade) + ': ' + '*' * grade
        printgrade -= 1
        print(currentgrade)

def main():
    exam_points_list, exerciselist = input_grades()
    exercises_points_list = exercises_to_points(exerciselist)
    print_statistics(exam_points_list, exercises_points_list)


main()
