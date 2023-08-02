from itertools import combinations


def gcd(a: int, b: int) -> int:
    # if a < b: a, b = b, a
    while b:
        a, b = b, a % b
    return a


def calculate_e(pi: int) -> list:
    temp = []
    for i in range(1, pi-1):
        if gcd(pi, i) == 1: temp.append(i)
    return temp


def calculate_d(pi: int, lst: list) -> list:
    temp = []
    for i in lst:
        for j in range(1, pi - 1):
            if (i * j) % pi == 1:
                temp.append(j)
                break
    return temp


def getPrimeList(num):
    primes = []
    if num < 2:
        return primes
    for i in range(2, num+1):
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
            elif j > i**0.5:
                break
        if isPrime:
            primes.append(i)
    return primes


# for i, j in combinations(getPrimeList(30),2):
# 두 소수 A와 B
PRIME_NUMBER_A = 2027
PRIME_NUMBER_B = 757

# n = A*B
n = PRIME_NUMBER_A*PRIME_NUMBER_B

# PI(n) = (A-1)*(B-1)
PI_N = (PRIME_NUMBER_A-1)*(PRIME_NUMBER_B-1)

# PI(n)과 서로소의 리스트 <- e가 될 수 있는 값
can_be_e_list = calculate_e(PI_N)

# e 값에 대한 d 값
can_be_d_list = calculate_d(PI_N, can_be_e_list)
print('------------------------------------------------')
print("n :", n)
print("PI_N :", PI_N)
for i, j in zip(can_be_e_list, can_be_d_list):
    print("e :",i,", d :",j)
# 2^n-1 값으로 된 d, e 찾기
# two_pow_n_minus_one = []
# for i, j in zip(can_be_e_list, can_be_d_list):
#    print("e :", i, ", d :", j)
#     if i in (3,7,15,31,63,127,255,511,1023,2047,4095):
#         if j in (3,7,15,31,63,127,255,511,1023,2047,4095):
#             two_pow_n_minus_one.append((i,j))
#
# if two_pow_n_minus_one:
#     print('------------------------------------------------')
#     print("n :", n)
#     print("PI_N :", PI_N)
#     for i, j in two_pow_n_minus_one:
#         print("e :",i,", d :",j)

# 3 7 31 127 8191은 메르헨 소수