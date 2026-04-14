#writing program for finging prime numbers in range givev
#the assumptions that might be from strating or any order in the range

def finding_prime_numbers(start,end):
    prime_numbers=[]
    #giving the range for as user input
    for i in range(start,end+1):
        for j in range(2,i):
            #checking by divisibility of the number by all the numbers less than it
            if i%j==0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers

finding_prime_numbers(1,27)
print(finding_prime_numbers(1,27))