#include<stdio.h>
#define devi 10.5
#define device 100

// These two lines don't work in gcc compiler
// #pragma startup start
// #pragma exit end

#pragma warn -rvl // No return value
#pragma warn -par // Parameter not used
#pragma warn -rch // Unreachable code

// Prototype
void __attribute__((constructor)) start();
void __attribute__((destructor)) end();

int function(){
    printf("This is inside function which was called by main function\n");
}

int main(){
    // #ifdef device
    // printf("Device is defined!\n");
    // #else
    // printf("Device is not defined!\n");
    // #endif
    #undef device
    #if device <=10
    printf("Number is less than 10\n");
    #elif device >= 15
    printf("Number is great than 15\n");
    #else
    printf("Number is between 10 and 15\n");
    #endif
    // #ifndef device
    // printf("Device is not defined!\n");
    // #else
    // printf("Device is defined!\n");
    // #endif
    printf("The file name is %s\n",__FILE__);
    printf("Today's date is %s\n",__DATE__);
    printf("Current time is %s\n",__TIME__);
    printf("Line number is %d\n",__LINE__);
    printf("ANSI: %d\n",__STDC__);
    function();
}

// for #pragma preprocessor
void __attribute__((constructor)) start(){
// void start(){
    printf("We're inside of start function\n");
}

// for #pragma preprocessor
void __attribute__((destructor)) end(){
// void end(){
    printf("We're inside of end function\n");
}