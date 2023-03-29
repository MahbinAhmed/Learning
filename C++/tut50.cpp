#include <iostream>
using namespace std;

int main()
{
    // int a = 50;
    // int *ptr = &a;
    // cout<<"The address of a is:- "<<ptr<<endl;
    // cout<<"The value of a is:- "<<*ptr<<endl;

    // int *ptr2 = new int(50);
    // cout<<"The address of b is:- "<<ptr2<<endl;
    // cout<<"The value of b is:- "<<*ptr2<<endl;

    int *arr = new int[5];
    arr[0] = 45;
    arr[1] = 5;
    arr[02] = 87;
    *(arr + 3) = 65;
    *(arr + 4) = 62;
    for (int i = 0; i < 5; i++)
    {
        cout << "arr[" << i << "]"
             << " = " << arr[i] << endl;
    }
    cout << endl;
    delete[] arr;

    for (int i = 0; i < 5; i++)
    {
        cout << "arr[" << i << "]"
             << " = " << arr[i] << endl;
    }
    return 0;
}