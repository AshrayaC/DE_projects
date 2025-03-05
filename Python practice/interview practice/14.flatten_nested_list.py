def flatten_list(input_list: list):
    output = []
    
    for i in input_list:
        if isinstance(i, list):  # Check if the element is a list
            output.extend(flatten_list(i))  # Recursively flatten the list
        else:
            output.append(i)  # Append non-list elements
    
    return output  # Return the flattened list after processing all elements

input_list = [1, 2, [7, 8], [1, 2, 3], 2, 4, [12, [2, 3]]]
t = flatten_list(input_list)
print(t)