numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if i > 1:
        is_primes = True
        for j in range(2,i - 1):
            prov = i % j
            if prov == 0:
                is_primes = False
                break
        if is_primes == True:
            primes.append(i)
        else:
            not_primes.append(i)
print(primes)
print(not_primes)



