#include <stdio.h>
int main(){
    int a[]={1,2,3,4}, *p=a, b=a[2];
//    int **p;
    printf("%p\n", p);
    printf("%p\n", a);
    printf("%d\n", p[1]);
    printf("%d\n", a[1]);


    printf("awdadad\n");

    return 0;


}













/*************fei bo na qie******************
int main(){
    int target = 3, result;
    int a=1, b=1 , c;
    for(int i=2 ; i < target ; ++i){
        c = a+b;
        a = b;
        b = c;
    }
    result = c;
    printf("%d" , result);
    return 0;
}
*/
/**************cheng fa biao*****************
int main(){
    int i , j ;
    for(i=1 ; i<10 ; i++){
        for(j=1 ; j<10 ;j++){
            if(i<j) break;
            printf("%d x %d = %-2d  ",i,j,i*j);
        }
        printf("\n");
    }
    return 0;
}
*/
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
*/
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