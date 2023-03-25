#include <stdio.h>

int main(void){

	int j;    

    unsigned int i;
	char *finally[128]={0};//拼接完成的数组,,f1是最高位，f2是次高位
	char finally_1[12754]={0};
	char *a[10]={"0030","0031","0032","0033","0034","0035","0036","0037","0038","0039"};//字库
	
	char longitude[12]={6,6,6,6,6,6,6,6,6,6,6,6};
	
	for(j=0;j<=1;j++)
	{
		finally[j]= a[(longitude[j]-40)];
	}//这里实现纬度转码
	
	sprintf(finally_1,"%s%s",finally[0],finally[1]);
	//这里实现转码后的拼接
    printf("%s",finally_1);

}
