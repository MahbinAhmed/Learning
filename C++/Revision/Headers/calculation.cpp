#include<iostream>
#include"calculation.h"

int add(int x, int y){
    return x+y;
}

int sub(int x, int y){
    if(x<y){
        return y-x;
    }
    else return x-y;
}