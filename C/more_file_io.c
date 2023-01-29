#include<stdio.h>

int main(){
    FILE *ptr;
    ptr = fopen("test2.txt","a");
    // Reading a file using fgetc() and fgets() method
    // char ch = fgetc(ptr);
    // char ch[20];
    // fgets(ch, 20,ptr);
    // printf("Result : %s\n",ch);

    // Writting a file using fputc() and fgets() method
    char ch = 'H';
    char str[50] = "Hello world! This line is written by %s file ";
    // fputc(ch, ptr);
    fputs(str,ptr);
    // printf(str, __FILE__);
}