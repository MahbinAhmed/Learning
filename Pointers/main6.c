#include<stdio.h>

void print(char *c){
    while (*c!='\0')
    {
        printf("%c", *c);
        c++;
    }
    printf("\n");
}

int main(){
    // char ch_arr[3] = "HI";
    // char ch_arr[10] = {'H','i'};
    // printf("%s\n", ch_arr);
    char ch_arr[6] = "Hello";
    char *ch = "Hey";
    print(ch_arr);
    printf("%s\n",ch);
    printf("%c\n", ch[2]);
    return 0;
}