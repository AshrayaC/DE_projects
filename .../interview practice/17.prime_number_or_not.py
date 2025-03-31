def prime_number(n):

    if n ==1 or n ==0:
        return False
    elif n > 1 :
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
   
print(prime_number(0))