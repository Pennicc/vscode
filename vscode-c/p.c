#include <stdio.h>

int main(int argc, char const *argv[])
{
    int a[] = {1,2,3,4,5,6};
    int *p , i;
    p=a;
    printf("%p\n", &p[i]);
    printf("%p\n", &p[1]);
    printf("%p\n", &p[2]);

    
    printf("%p\n", &a);
    printf("%p\n", &a[1]);
    printf("%p\n", &a[2]);

    // printf("%p\n", &p);
    // printf("%p\n", &a);




    return 0;
}
