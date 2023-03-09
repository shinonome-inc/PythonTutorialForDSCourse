# 関数は x**2とする
min_x, max_x = map(float, input().split())  # 定義域の与え方どうしよう
width_list = (0.1, 0.01, 0.001, 0.0001)
total_area_list = []  # 近似精度があがっていくのを確認する用
for width in width_list:
    x = min_x
    total_area = 0

    while x < max_x:
        left_height = x**2
        right_height = (x + width) ** 2
        total_area += (left_height + right_height) * width / 2
        x += width

    total_area_list.append(total_area)

print(total_area_list)
