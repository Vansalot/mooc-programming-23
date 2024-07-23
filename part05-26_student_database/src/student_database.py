def add_student(students: dict, name: str):
    students[name] = []
    return students

def print_student(students: dict, name: str):
    # name:
    # completed courses:
    # course, grade
    # avg grade, grade
    # name: No such person in the database
    if name not in students:
        print(f'{name}: no such person in the database')
        return
    else:
        print(f'{name}:')
    
    if len(students[name]) == 0:
        print(' no completed courses')

    elif name in students:
        print(f' {len(students[name])} completed courses:')
        average = 0
        for course in students[name]:
            average += course[1]
            print(f'  {course[0]} {course[1]}')
        if len(students[name]) > 1:
            print(f' average grade {average/len(students[name])}')
   


def add_course(students: dict, name: str, coursedata: tuple):
    # add course to existing student
    # grade 0 ignored
    # if course already in db, don't lower grade
    if coursedata[-1] != 0 or coursedata not in students[name]:
        students[name].append(coursedata)
    return students

def summary(students: dict):
    # total students
    # most courses completed, count, name
    # best average grade, grade, name
    
    pass

if __name__=='__main__':
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")


