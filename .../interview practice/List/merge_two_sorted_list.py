# def merge_lists(list1,list2):
#     return sorted(list1+list2)

# print(merge_lists([1,2,3],[12,2,3]))
# # ➡️ Total Time Complexity: O((n + m) * log(n + m))
# # ➡️ Total Space Complexity: O(n + m)

def merge_list(test_input_list1, test_input_list2):
    merged = []
    i = 0 
    j = 0 

    while i < len(test_input_list1) and j < len(test_input_list2):
        if test_input_list1[i] < test_input_list2[j]:
            merged.append(test_input_list1[i])
            i = i + 1
        else:
            merged.append(test_input_list2[j])
            j = j + 1
    
    #append any remaining elements

    merged.extend(test_input_list1[i:])
    merged.extend(test_input_list2[j:])
    
    return merged

# ➡️ Total Time: O(n + m)
# ➡️ Space: O(n + m) (new merged list)