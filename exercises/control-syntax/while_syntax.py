# ユークリッドの互除法
a, b = map(int, input().split())

r = a % b
while r != 0:
    a = b
    b = r
    r = a % b
print(f"{b} が最大公約数")