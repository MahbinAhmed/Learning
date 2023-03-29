#include<iostream>
using namespace std;

class Student{
    protected:
    int roll;
    public:
    void set_roll(int r){
        roll = r;
    }

    void get_roll(){
        cout<<"Roll number:- "<<roll<<endl;
        cout<<endl;
    }
};

class Exam: public Student{
    protected:
    float math_mark;
    float english_mark;
    public:
    void set_marks(float m, float e){
        math_mark = m;
        english_mark = e;
    }

    void get_marks(){
        cout<<"Math marks:- "<<math_mark<<endl;
        cout<<"English marks:- "<<english_mark<<endl;
        cout<<endl;
    }
};

class Result: public Exam{
    protected:
    float result;
    public:
    void get_result(){
        get_roll();
        get_marks();
        cout<<"Result Average:- "<<(math_mark+english_mark)/2<<endl;
        cout<<endl;
    }
};

int main(){
    Result o1;
    o1.set_roll(10);
    o1.set_marks(92.5,95.9);
    o1.get_result();
    return 0;
}