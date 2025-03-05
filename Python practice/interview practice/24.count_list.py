def count_list(input_list):
    
    count = 0
    if not input_list:
        return 0 
    for i in input_list:
        count = count + 1
    return count

print(count_list([1,2,3,4, 0 ]))
print(count_list([]))