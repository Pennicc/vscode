#include <stdio.h>
int main(){




    return 0;
}













/**********shui xian hua shu*****************
int main(){
    int i =100;
    for(i ; i<1000 ; i++){
        int a = i/100 , b = i/10%10 , c = i%10;
        if(a*a*a+b*b*b+c*c*c == i)
            printf("%d\n",i);
    }
    return 0;
}

/**********************************************************************************************
int scf(int inp);
int main() {
    int i , j ,k, a;
    for(i=0 ; i<10 ; i++){
        for(j=0 ; j<10 ; j++){
            for(k=0 ; k<10 ; k++){
                if(scf(i)+scf(j)+scf(k) == i*100+j*10+k && i*100+j*10+k!=0 && i*100+j*10+k!=1)
                    printf("%d is \n",i*100+j*10+k);
            }
        }
    }

    return 0;
}

int scf(int inp){
    int resu = 1;
    for(int i=1 ; i<4 ; i++){
           resu *= inp;
     }
    return resu;
}
*/