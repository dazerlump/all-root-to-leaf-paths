#include<stdio.h>
unsigned long long power(unsigned long long x,unsigned long long y,unsigned long long d)
{
    unsigned long long res=1;
    x=x%d;
    while(y>0)
    {
        if((y&1)==1)
            res=(res*x)%d;
        y=y/2;
        x=(x*x)%d;
    }
    return res;
}
void main()
{
   unsigned long long x,y,d;
    scanf("%llu %llu %llu",&x,&y,&d);
    printf("%llu ",power(x,y,d));
}
