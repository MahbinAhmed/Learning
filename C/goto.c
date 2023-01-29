#include<stdio.h>
int main()
{
    // int a = 0;
    // label:
    //     printf("This line is under label\n");
    //     goto end;
    // printf("Hello World\n");
    // // goto label;
    
    // for(;a<10;a++){
    //     printf("%d",a);
    // }
    // goto label;
    // end:
    //     printf("This line is under end label\n");

    int i,j,input;
    for (i=0;i<2;i++)
    {
        printf("This is from main iteration %d\n", i);
        // goto end;
        for (j=0;j<2;j++)
        {
            printf("This is from sub iteration %d\n", j);
            printf("Enter 0 to exit:- \n");
            scanf("%d", &input);
            if (input==0)
            {
                goto end;
            }
        }
    }
    end:
        printf("This line is printed from end label");
}