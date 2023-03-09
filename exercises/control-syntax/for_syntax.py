# nが素数か判定せよ。
n = int(input())
max_num = int(n ** (1 / 2))  # floor

is_prime = True
for m in range(2, max_num + 1):
    r = n % m
    if r == 0:
        is_prime = False
        break
if is_prime:
    print("素数")
else:
    print("素数じゃない")
