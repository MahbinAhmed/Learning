#include <stdio.h>
#include <string.h>

void print_string(char str[]){
    int i=0;
    while (str[i]!='\0')
    {
        printf("%c",str[i]);
        i++;
    }
    printf("\n");
}
int main(){
    char greet[7] = {'H','e','l','l','o',' ','\0'};
    // // char greet[6] = "Hello";
    char demo[50];
    // gets(demo);
    // // print_string(greet);
    // print_string(demo);
    // printf("Using printf: %s\n",demo);
    // printf("Using puts: ");
    // puts(demo);
    printf("Enter a string:- \n");
    // scanf("%s",demo);
    gets(demo);
    print_string(demo);
    // char copy[50];
    // strcpy(copy, strcat(greet,demo));
    // strcat(copy," !");
    // printf("The le1ngth is %d\n",strlen(copy));
    // puts(strrev(copy));
    // printf("Result of strcmp:- %d\n",strcmp(greet,demo));
}