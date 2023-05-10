#include <iostream>
using namespace std;

// Unary Operator Overloading
// class A{
//     int val;
//     public:
//     A(int x){
//         val = x;
//     }

//     void operator ++(){
//         val += 1;
//     }

//     void get_data(){
//         cout<<"The value is: "<<val<<endl;
//     }
// };

// int main(){
//     A o1(5);
//     ++o1;
//     o1.get_data();
//     return 0;
// }

// Binary Operator Overloading
class complex
{
    int r;
    int i;

public:
    complex() {}
    complex(int x, int y)
    {
        r = x;
        i = y;
    }

    complex operator+(complex x)
    {
        complex result;
        result.r = r + x.r;
        result.i = i + x.i;
        return result;
    }

    void get_data()
    {
        cout << r << "+" << i << "i" << endl;
    }
};

int main()
{
    complex o1, o2, o3;
    o1 = complex(5, 4);
    o2 = complex(7, 9);
    o3 = o1 + o2;
    o3.get_data();
    return 0;
}