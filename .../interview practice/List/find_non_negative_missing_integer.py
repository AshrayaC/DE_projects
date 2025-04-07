
def find_missing_int(l):
    
    list_dict = {}
    
    for i in l:
        list_dict[i] = True
    
    for i in range(len(l)):
        if not list_dict.get(i):
            return i
    return None

l = [0,1,2,3,4,5,6,7,9]
print(find_missing_int(l))