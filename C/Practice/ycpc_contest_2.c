#include<stdio.h>
#include<math.h>

void arrayPrint2(int arr[], int arr_size)
{
    printf("{");
    for (int i = 0; i < arr_size; i++)
    {
        printf("%d", arr[i]);
        if (i != (arr_size - 1))
        {
            printf(",");
        }
    }
    printf("}\n");
}

int ascendReverse(int array[], int arr_len)
{
    int temp;
    for (int j = 0; j < arr_len; j++)
    {
        for (int i = 0; i < (arr_len-1); i++)
        {
            if (array[i] > array[i + 1])
            {
                temp = array[i + 1];
                array[i + 1] = array[i];
                array[i] = temp;
            }
        }
    }
}

int descendReverse(int array[], int arr_len){
    int temp;
    for (int j = 0; j < arr_len; j++)
    {
        for (int i = 0; i < (arr_len-1); i++)
        {
            if (array[i] < array[i + 1])
            {
                temp = array[i + 1];
                array[i + 1] = array[i];
                array[i] = temp;
            }
        }
    }
}

int series_checker(int arr[], int arr_len){
    for(int i=0;i<(arr_len-1);i++){
        if(arr[i]%2!=0 && arr[i+1]%2==0){
            return 1;
            break;
        }
    }
    return 0;
}

int main(){
     /*Question-1 | Word Done*/
    /*
    int test_cases;
    int x,d1,d2;
    scanf("%d",&test_cases);

    for(int i=0;i<test_cases;i++){
        scanf("%d %d %d", &x , &d1, &d2);
        int mul = x*d1;
        int result = (mul/d2)+((mul%d2)!=0);
        // int result2 = ceil(result);
        printf("%d", result);
        printf("\n");
    }
    */

    /*Question-3 | Lily Can Do It!*/
    /**/
    int array[] = {7, 19, 1, 21, 13};
    int arr_len = sizeof(array) / sizeof(array[0]);
    // printf("%d\n",arr_len);
    ascendReverse(array, arr_len);
    if(series_checker(array,arr_len)==1){
        printf("YES\n");
    }
    // arrayPrint2(array, arr_len);
    // descendReverse(array, arr_len);
    // else if(series_checker(array,arr_len)==1){
    //     printf("YES\n");
    // }
    else{
        descendReverse(array, arr_len);
        if (series_checker(array, arr_len)==1){
            printf("YES\n");
        }
        else{
        printf("NO\n");
        }
    }
    // arrayPrint2(array, arr_len);

    return 0;
}