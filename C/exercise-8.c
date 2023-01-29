#include<stdio.h>
#include<stdlib.h>

int main(){
    int len,i=0;
    char *ptr;
    // for(int i=0;i<3;i++){
    for(i;i<3;i++)
    {
        printf("Enter the UserId length of Employee %d \n",i+1);
        scanf("%d", &len);
        // getchar();
        ptr = (char*) malloc((len+1)*sizeof(char));
        printf("Enter the UserID of Employee %d :- ",i+1);
        scanf("%s", ptr);
        // getchar();
        printf("UserId of Employee %d :- %s\n\n",i+1,ptr);
        free(ptr);
        i = i+1;
    }
}