# 1より大きい最小の数における小数部分を求める(machine epsilon)
# 指数部分を固定したうえでどれくらい小さいfloatを表現できるか求める
# したがって while a != 0 は不可

a = 1
while a + 1 != 1:
    a /= 2
print(a * 2)