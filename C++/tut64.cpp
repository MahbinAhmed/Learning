#include <iostream>
using namespace std;

template <class T>
class vector
{
public:
    int size;
    T *arr;
    vector(int x)
    {
        size = x;
        arr = new T[size];
    }

    T dot_product(vector a)
    {
        T count = 0;
        for (int i = 0; i < size; i++)
        {
            count += arr[i] * a.arr[i];
        }
        return count;
    }
};

int main()
{
    // vector <int>o1(3);
    // vector <int>o2(3);
    // o1.arr[0] = 5;
    // o1.arr[1] = 2;
    // o1.arr[2] = 6;

    // o2.arr[0] = 3;
    // o2.arr[1] = 4;
    // o2.arr[2] = 7;
    // int result = o1.dot_product(o2);
    // cout<<result<<endl;
    vector<float> o1(3);
    vector<float> o2(3);
    o1.arr[0] = 5.2;
    o1.arr[1] = 2.3;
    o1.arr[2] = 6.9;

    o2.arr[0] = 3.2;
    o2.arr[1] = 4.3;
    o2.arr[2] = 7.7;
    float result = o1.dot_product(o2);
    cout << result << endl;

    return 0;
}