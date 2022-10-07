def prime_checker(number):
    is_prime=True
    for i in range(2,number):
        if number % i ==0:
            is_prime = False
    if is_prime:
        print("Prime")
    else:
        print("Not a prime Number")


n = int(input("Check a number: \n"))
prime_checker(number=n)