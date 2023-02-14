#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	srand (time(0));
	int number=rand()%100+1;
	int a,count=0;
	scanf("%d",&a);

	do{
		count++;
		if(a>number){
			printf("你输入的数大了\n");
		}
		else if(a<number){
			printf("你输入的数小了\n");
		}
	}

	while(a!=number);
		printf("你用了%d次猜出了答案\n",count);
    
	return 0;
}