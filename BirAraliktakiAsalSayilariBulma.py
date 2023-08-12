def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
    return True
def find_prime_in_range(start,end):
    primes=[]
    for num in range(start,end+1):
        if is_prime(num):
            primes.append(num)
    return primes

start=int(input("Please enter a lower limit: "))
end=int(input("Please enter a upper limit: "))
prime_numbers = find_prime_in_range(start, end)
print("Prime numbers: ",prime_numbers)