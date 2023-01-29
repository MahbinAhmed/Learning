#include<stdio.h>
#define PI 3.1416

int main()
{
    // const int a = 5;
    // a = 5;
    // printf("%f", PI);
    // printf("Hey there! It's a windows error sound! \a");
    return 0;
}

#include <stdio.h>

int main(int argc, char* argv[])
{
    printf("Beep sound started\n");
    printf("\a"); // '\a' is used to make a beep sound
    printf("Beep sound stopped\n");

    return 0;
}