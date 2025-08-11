#include<stdio.h>
#include<stdlib.h>
int main(){
    int T;
    scanf("%d", &T);

    while(T--){
        long long A, B, X;
        scanf("%ld","%ld","%ld",&A,&B,&X);

        if ((A+B)%2 !=0){
            printf("no\n");
        }
        else if (llabs(A-B) % (2*X)==0){
            printf("yes\n");
        }
        else{
            printf("no\n");
        }
    }
    return 0;

}
