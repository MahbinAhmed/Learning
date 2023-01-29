#include<stdio.h>
#include<string.h>

int main()
{
    char s1[] = "Hello";
    char s2[] = "World";
    // printf(strcat(s1,s2));
    // printf("\n");
    // puts(strcat(s1,s2));
    // printf("The len of first string is %d",strlen(s1));
    // printf("The reverse of first string is %s", strrev(s1));
    char s3[50];
    // strcpy(s3, strrev(s1));
    // puts(s3);
    // printf("Result of strcmp() for s1,s2 : %d",strcmp(s1,s2));
    // Quiz
    char inp1[100],inp2[100], text[]=" is a friend of ";
    printf("Enter first text:- ");
    gets(inp1);
    printf("Enter second text:- ");
    gets(inp2);
    strcat(inp1,text);
    printf(strcat(inp1,inp2));
}