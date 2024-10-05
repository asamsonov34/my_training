nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
non_primes = []
for i in range(len(nums)):
    if nums[i] == 1:
        continue
    is_prime = True
    for j in range(2, nums[i]):
        if nums[i] % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(nums[i])
    else:
        non_primes.append(nums[i])
print('Primes: ' ,primes)
print('Non-Primes: ', non_primes)