"""sd="for customer compalints please write to consumer care cell at po box reliance retail"
w=len(sd.split())
a=sd.split()
c=len(a)
print(c)
print("no of words",w)

def wc(str):
    counts=dict()
    a=str.split()
    for word in a:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] =1
    return counts
print(wc('for customer compalints please write to consumer care cell at po box reliance retail'))

def wc(str):
    counts=dict()
    a=str.split()
    for word in a:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(wc("for kamal kamal kamal customer compalints please write to consumer care cell at po box reliance retail"))

#1 print("hello,World!")
a=10
if a>98:
    print("a is big")
else:
    print("not big")

#3 arth opera
a=10
b=23
c=a+b
d=b-a
w=b/a
print(c)
print(d)
print(w)

#4 Python division
w=b/a
print(w)
n=int(input("enter number"))
for i in range(n):
    print(i**2)
85
def cl(year):
    if(year%400==0):
        print("leap year")
    else:
        print("not leap")
year=int(input("entr number"))
cl(year)

#lambda argument:expression
w=lambda a,b:a+b
print(w(4,4))

s=lambda a:a%2==0
res=s(int(input("enter number")))
print(res)

if (res==True):
    print("even number")
else:
    print("odd number")


def ws(str):
    counts=dict()
    a=str.split()
    for word in a:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(ws('forcustomerkamalforkamaltootocompalintpleasewritetoconsumercarecellatpoboxrelianceretail'))"""

old="forcustomerkamalforkamaltootocompalintpleasewritetoconsumercarecellatpoboxrelianceretail"
new={}
for i in old:
    if i in new:
        new[i] += 1
    else:
        new[i] = 1
print("count all char: \n" +str(new))

