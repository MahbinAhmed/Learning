#include<stdio.h>

int main(){
    char ch[50] = "This line was written by file_io.c program! ";
    char ch2[50];
    FILE *ptr = NULL;
    ptr = fopen("test.txt","r");
    
    // READING A FILE USING FILE I/O
    fscanf(ptr,"%s", ch);
    fscanf(ptr,"%s", ch2);
    printf("%s\n",ch);
    printf("%s\n",ch2);

    // WRITING A FILE USING FILE I/O
    // ptr = fopen("test.txt","w");
    // Appending a file with "Append" mode
    // ptr = fopen("test.txt","a");
    // fprintf(ptr,"%s", ch);
    // fclose(ptr);

    // More file i/o functions:- 
    // fgetc()
    // fgets()
    // fgetw()
    // fread()
    // ------
    // fputc()
    // fputs()
    // fputw()
    // fwrite()
}