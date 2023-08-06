s1 = "Aults"
s2 = "Kelly"
i=0;
ans="";
for char in s1:
    if(i==int(len(s1)/2)):
       ans+=s2
       ans+=char
       i=i+1
    else:
        ans+=char
        i=i+1

print(ans)