

#grades = ['B', 'C', 'A', 'B', 'B', 'A']

def count_grades(grades):

    counts = {}

    for grade in grades:
        
        if grade not in counts:
            counts[grade] = 1
        else:
            counts[grade] = counts[grade] + 1

    return counts


def process_grades(filename):

    f = open(filename, 'r')
    lines = f.readlines()

    strip_lines = lines[0].strip('\n')
    rem = strip_lines.split(" ")

    grade_counts = count_grades(rem)

    grades = grade_counts.keys()

    for grade in grades:
        num = grade_counts[grade]
        print(str(grade) + ' -- ' + str(num))

    return grade_counts