s=[]
for i in range(1,100):
    if i%3==0 and i%5==0:
        s.append('FizzBuzz')
    elif i%3==0:
        s.append('Fizz')
    elif i%5==0:
        s.append('Buzz')
    else:
        s.append(i)

print(s)
