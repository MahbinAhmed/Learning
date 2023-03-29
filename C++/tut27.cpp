#include<iostream>
using namespace std;

class complex;

class calculator{
    public:
    // int add(complex o1, complex o2){
    //     return(o1.a+o2.a);
    // }
    int add(complex, complex);
    int addb(complex, complex);
    // int addb(complex o1, complex o2){
    //     return(o1.b+o2.b);
    // }
};

class complex{
    int a;
    int b;
    public:
    friend class calculator;
    // friend int calculator::add(complex o1, complex o2);
    int set_data(int x, int y){
        a = x;
        b = y;
    }

    int get_data(){
        cout<<"a = "<<a<<" | b = "<<b<<endl;
    }
};

int calculator::add(complex o1, complex o2){
    return(o1.a+o2.a);
}

int calculator::addb(complex o1,complex o2){
    return(o1.b+o2.b);
}

int main(){
    complex c1,c2;
    c1.set_data(1,4);
    c2.set_data(3,5);

    calculator a1;
    int result = a1.add(c1,c2); 
    cout<<"a(c1)+a(c2) = "<<result<<endl;
    int result2 = a1.addb(c1,c2);
    cout<<"b(c1)+b(c2) = "<<result2<<endl;

    return 0;
}

/*Things to note--->>>
If you are making member friend function then you have to make forward declaration of main class first. Then you have to declare the friend class but
you can't declare the friend function. You have to just initialize it and have to declare after the main class declaration. You have to declare the
main class after the friend class. If you are making friend class or friend function, just declare the main class first and then declare the friend
class or friend function.*/