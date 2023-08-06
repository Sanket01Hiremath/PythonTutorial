def divide(a,b):
    if b==0:
        return "not divisible"
    else:
        c=int(a/b)
        return f"{'ans: '}{c}"
    

print(divide(5,1))