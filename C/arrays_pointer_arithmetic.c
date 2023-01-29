#include<stdio.h>
int main()
{
    int arr[]={1,3,5,455,5,43};
    int *arp = arr;
    
    printf("%d\n", arp[0]);
    arp++;
    arp++;
    printf("%d\n",&arr[0]);
    printf("%d\n",&arp[0]);
    // printf("%d\n", arr);
    // printf("%d", &arr[0]);
}