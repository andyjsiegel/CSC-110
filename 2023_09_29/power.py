def power(base, exp):
    if exp == 0: return 1
    for i in range (0,exp-1):
        base = str(base) + f"*{exp}"

    return eval(str(base))

print(power(3,1)) # 27