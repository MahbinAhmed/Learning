#include<stdio.h>

int main(){
    //Why pointer type is important
    int a=1025;
    int *p = &a;
    printf("Size of integer:- %d\n", sizeof(int));
    printf("Address %d has a value of %d\n", p, *p);
    printf("Address %d has a value of %d\n", p+1, *(p+1));
    printf("\n");
    char *p0 = (char*)&a; //Typecasting integer pointer into char pointer
    printf("Size of char:- %d\n", sizeof(char));
    printf("Address %d has a value of %d\n", p0, *p0); //It will print 1 as char data type only required 1 byte and the byte is already equipped a=1025=00000000 00000000 00000100 00000001
    printf("Address %d has a value of %d\n", p0+1, *(p0+1)); //It will print 1 as char data type only required 1 byte and the byte is already equipped a=1025=00000000 00000000 00000100 00000001

    // There is something called genric pointer which's data type is void
    return 0;
}