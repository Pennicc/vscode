#include <stdio.h>
#include <string.h>
int main()
{

	
	char longitude[12] = {2, 3, 5, 7, 8, 2, 3, 4, 4, 5, 6, 6};
	
	char *a[10] = {"0030", "0031", "0032", "0033", "0034", "0035", "0036", "0037", "0038", "0039"}; // 字库
	char *b[12];

	int j;
	for (j = 0; j <=12; j++)
	{
		b[j] = a[longitude[j]];
	} // 这里实现纬度转码


	// sprintf(finally_1, "%s%s", finally[0], finally[1]);
	// 这里实现转码后的拼接
	// printf("%s ", b);
	for (j = 0; j <12; j++)
	{
		printf("%s ", b[j]);
	}
}
