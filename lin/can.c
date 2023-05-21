#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <syspes.h>
#include <unistd.h>
#include <sysat.h>
#include <fcntl.h>
#include <errno.h>

int main(int argc,char const *argv[])
{
int fd = open("./file.txt",O_RDWR | O_CREAT,0777);
if(fd<0)
{
    perror("open error");
    return -1;
}
char buf[1024] = "";

read(fd,buf,sizeof(nuf));
printf("%s\n",buf);
memset(buf,0,sizeof(buf));
close(fd);
return 0;

}
