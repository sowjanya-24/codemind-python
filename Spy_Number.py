n=int(input());
prod=1;
s=0;
while n>0:
    rev=n%10;
    prod=prod*rev;
    s=s+rev;
    n=n//10;
if(s==prod):
    print("Spy Number");
else:
    print("Not Spy Number");
    