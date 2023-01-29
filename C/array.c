#include<stdio.h>
int main()
{
    // int marks[5];
    // for (int i=0; i<5;i++){
    //     printf("Enter mark for the student of roll %d :- ", i+1);
    //     scanf("%d", &marks[i]);
    // }
    // marks[4]=90;
    // printf("\n\n");
    // for (int i=0; i<5;i++){
    //     printf("The mark of the student with roll no. %d is %d\n",i,marks[i]);
    // }
    int marks[5][3];
    printf("Subject 1 = Bangla(101)\nSubject 2 = English(107)\nSubject 3 = Mathmatics(109)\n\n");
    for (int i=0;i<5;i++){
        for(int j=0;j<3;j++){
            printf("Enter mark for student (Roll no:- %d) in subject %d:- ",i+1,j+1);
            scanf("%d",&marks[i][j]);
        }
    }
    printf("\n\n");
    for (int i=0;i<5;i++){
        for (int j=0;j<3;j++){
            printf("Showing mark for student(Roll no:- %d) in subject %d:- %d\n",i+1,j+1,marks[i][j]);
        }
    }
}