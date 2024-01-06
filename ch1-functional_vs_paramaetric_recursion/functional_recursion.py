def f(i: int):
    return 0 if i==0 else i+f(i-1)

print(f(10))