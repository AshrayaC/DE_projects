def rep_char(input_str, n):
    output_str = ""

    for j in input_str:  # Loop through each character
        output_str = output_str+ (j * n)  # Repeat each character `n` times
    
    return output_str

print(rep_char('sferr', 2))  # Expected output: 'ssffeererr'