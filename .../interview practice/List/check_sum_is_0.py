#The function f_sum_zero(l) checks if there are two numbers in the list l that sum up to zero.

def f_sum_zero(l):
    if len(l) < 2:
        return False
    l1 = set(l)
    print(l)
    print(l1)
    for i in l:
        if -i in l1:
            return True
    return False

input_list = [-1,2,3,1,1,3]
print(f_sum_zero(input_list))