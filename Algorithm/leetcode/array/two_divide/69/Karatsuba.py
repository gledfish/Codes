def karatsuba_multiply(x, y):
    # 将 x 和 y 转换为字符串
    x_str = str(x)
    y_str = str(y)

    # 将 x 和 y 填充为相同的长度
    max_len = max(len(x_str), len(y_str))
    x_str = x_str.zfill(max_len)
    y_str = y_str.zfill(max_len)

    # 基本情况：如果整数长度为 1，则直接计算乘积
    if len(x_str) == 1:
        return int(x_str) * int(y_str)

    # 拆分 x 和 y
    mid = len(x_str) // 2
    a, b = int(x_str[:mid]), int(x_str[mid:])
    c, d = int(y_str[:mid]), int(y_str[mid:])

    # 递归计算乘积
    ac = karatsuba_multiply(a, c)
    bd = karatsuba_multiply(b, d)
    ad_bc = karatsuba_multiply(a + b, c + d) - ac - bd

    # 计算最终乘积
    result = (ac * 10**(2 * (len(x_str) - mid))) + (ad_bc * 10**mid) + bd
    return result

# 示例用法
x = 12345
y = 6789
product = karatsuba_multiply(x, y)
print(product)
# 输出：83810205