
#1. Tuple and list - find out which student got highest marks

def highest_get(input_list:list):
    if len(input_list) ==0 :
        return []
    max_marks = max(marks for name, marks in input_list)

    return [(name, marks) for name, marks in input_list if marks == max_marks ]
    
students = [('David',46),('Sam',45), ('Rita', 20)]
t = highest_get(students)
print(t)
