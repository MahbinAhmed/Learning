#include <stdio.h>

int main(int argc, char const *argv[])
{
    printf("Total input:- %d\n",argc-1);
    if(argc>=2){
        for(int i=1;i<argc;i++){
            printf("Input %d:- %s\n",i, argv[i]);
        }
    }
    return 0;
}
