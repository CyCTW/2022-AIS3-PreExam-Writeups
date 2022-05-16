#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <fcntl.h>

// 0000000000401216
void get_the_flag()
{
    char buf[0x30] = {0};
    int fd = open("/home/bof2win/flag", O_RDONLY);
    read(fd, buf, 0x30);
    write(1, buf, 0x30);
    close(fd);
}

int main()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    char buf[0x10];
    
    puts("What's your name?");
    gets(buf);
    
    printf("Hello, %s!\n", buf);
    return 0;
}
/*
1 15b
1 1c
1 3 a
3 1 a
3 14
3 0
3 1
1 2 abcdefg
3 2 7
4 0
4 2




*/