#include<stdio.h>
void print_str(char str[])
{
    int i = 0;
    for (i;str[i]!='\0';i++){
        printf("%c",str[i]);
        // printf("\n");
        // printf("%d",i);
    }
    // while (i!='\0')
    // {
    //     printf("%s",str[i]);
    //     i++;
    // }
    
}
int main()
{
    // char str[] = {'h','e','l','l','o','\0'};
    // char str[] = "Hello";
    char str[10];
    gets(str);
    print_str(str);
    puts(str);
}