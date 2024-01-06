def f(s: str, i: int) -> bool:
    if i>=len(s)//2:
        return True
    if s[i]!=s[len(s)-i-1]:
        return False
    
    return f(s,i+1)

print(f("MADAM", 0))