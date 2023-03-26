#include <stdio.h>

void mystrc(char* s, char* t);

int main() {
    char s[80], t[80];
    gets(s);
    gets(t);
    mystrc(s, t);
    puts(t);
    return 0;
}

void mystrc(char* s, char* t)
{
    printf("%p\n",s);
    // make the pointer to the end of str
    while(*t != 0) t++;
    while(*s != 0)
    {
        *t=*s;
        t++;
        s++;
    }
}
