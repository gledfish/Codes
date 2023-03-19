
# callables = []
# for i in (1, 2, 3):
#     callables.append(lambda: i)

# for f in callables:
#     print(f())

callables = []
for i in (1, 2, 3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())
