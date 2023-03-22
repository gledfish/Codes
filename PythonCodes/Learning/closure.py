def multiplier(x):
    def multiply(y):
        return x * y
    return multiply

multipliers = []
for i in range(1, 4):
    multipliers.append(lambda x: i * x)

m1, m2, m3 = multipliers

print(m1(10)) # 30
print(m2(10)) # 30 
print(m3(10)) # 30

# multipliers = []
# for i in range(1, 4):
#     multipliers.append(lambda x: i * x)
