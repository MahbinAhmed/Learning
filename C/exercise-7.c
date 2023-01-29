#include <stdio.h>
#include <string.h>

struct Driver
{
    char name[50];
    char DLno[50];
    char route[50];
    char kms[];
};
void main()
{
    struct Driver d1, d2, d3;
    printf("For Driver 1:- \n");
    printf("\tName:- ");
    gets(d1.name);
    printf("\tDLno:- ");
    gets(d1.DLno);
    printf("\tRoute:- ");
    gets(d1.route);
    printf("\tTotal kms:- ");
    gets(d1.kms);

    printf("For Driver 2:- \n");
    printf("\tName:- ");
    gets(d2.name);
    printf("\tDLno:- ");
    gets(d2.DLno);
    printf("\tRoute:- ");
    gets(d2.route);
    printf("\tTotal kms:- ");
    gets(d2.kms);

    printf("For Driver 3:- \n");
    printf("\tName:- ");
    gets(d3.name);
    printf("\tDLno:- ");
    gets(d3.DLno);
    printf("\tRoute:- ");
    gets(d3.route);
    printf("\tTotal kms:- ");
    gets(d3.kms);

    printf("\n\n");
    
    printf("Information of all the drivers:- \n");

    printf("For Driver 1:- \n");
    printf("\tName:- ");
    printf("%s\n",d1.name);
    printf("\tDLno:- ");
    printf("%s\n",d1.DLno);
    printf("\tRoute:- ");
    printf("%s\n",d1.route);
    printf("\tTotal kms:- ");
    printf("%s\n",d1.kms);

    printf("For Driver 2:- \n");
    printf("\tName:- ");
    printf("%s\n",d2.name);
    printf("\tDLno:- ");
    printf("%s\n",d2.DLno);
    printf("\tRoute:- ");
    printf("%s\n",d2.route);
    printf("\tTotal kms:- ");
    printf("%s\n",d2.kms);

    printf("For Driver 3:- \n");
    printf("\tName:- ");
    printf("%s\n",d3.name);
    printf("\tDLno:- ");
    printf("%s\n",d3.DLno);
    printf("\tRoute:- ");
    printf("%s\n",d3.route);
    printf("\tTotal kms:- ");
    printf("%s\n",d3.kms);
}