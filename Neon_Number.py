n=int(input());
s=0;
sq=n*n;
while sq!=0:
    m=sq%10;
    s=s+m;
    sq=sq//10
if(s==n):
    print("Neon Number");
else:
    print("Not Neon Number");