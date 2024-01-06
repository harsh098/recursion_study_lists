def f(i: int, sum: int = 0):
    if i==0:
        return sum
    else:
        return f(i-1, sum+i)

if __name__ == '__main__':
    print(f(10, 0))