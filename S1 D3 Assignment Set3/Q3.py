list=[2, 17, 7, 15]
t = 9
dict={}
x=0;
for i in list:
    if len(dict)==0:
        dict[i]=x
    if dict.get(t-i,"NA")!="NA":
        print(dict.get(t-i),x);
        break;
    else:
        x=x+1