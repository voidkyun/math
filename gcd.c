#include<stdio.h>

int ab,bc,ca;

int gcm(int a1,int b1,int c1){
    int a=a1,b=b1,c=c1,tmp;
    while(a%b!=0){
        tmp=a%b;
        a=b;
        b=tmp;
    }
    ab=b;
    a=a1;b=b1;
    while(b%c!=0){
        tmp=b%c;
        b=c;
        c=tmp;
    }
    bc=c;
    b=b1;c=c1;
    while(c%a!=0){
        tmp=c%a;
        c=a;
        a=tmp;
    }
    ca=a;
    return 0;
}

int main(void){
    int k,ans=0;
    scanf("%d",&k);
    for(int i=1;i<=k;i++){
        for(int i2=1;i2<=k;i2++){
            for(int i3=1;i3<=k;i3++){
                ab=i;bc=i2;ca=i3;
                while(!(ab==bc && bc==ca)){
                    gcm(ab,bc,ca);
                }
                ans+=ab;
            }
        }
    }
    printf("%d",ans);
    return 0;
}


