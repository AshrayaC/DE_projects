def hide_email(input_str :str):
    initial_str = input_str.split('@')[0]
    domain_str  = input_str.split('@')[1]

    return initial_str[0] + (len(initial_str)- 2) *  '*' +  initial_str[-1] + '@' + domain_str


input_str = 'abadsfsdc@gmail.com'

t=hide_email(input_str)
print(t)