"""
    Calculate the average grade for each student.

    Parameters:
    student_data (list): A list of tuples, where each tuple contains a student's name (str)
                         and a list of their grades (list of int).

    Returns:
    dict: A dictionary mapping student names to their average grade (float).
    
    [       ("Alice", [85, 90, 88]),
            ("Bob", [70, 75, 80]), 
            ("Charlie", [65, 70, 75])
    ]

"""

def calculate_average_grades(input_list):
    
    output_dict = {}

    for name, marks in (input_list):
        if not input_list:
            return None
        elif marks:
            avg = sum(marks)/len(marks)
            output_dict[name] = avg
        else:
             output_dict[name] = 0
    return output_dict


students = [("Alice", [85, 90, 88]),
            ("Bob", [70, 75, 80]), 
            ("Charlie", [65, 70, 75])]

averages = calculate_average_grades(students)
print(averages)

