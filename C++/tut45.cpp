#include <iostream>
using namespace std;

class Student
{
protected:
    int roll;

public:
    void set_roll(int r)
    {
        roll = r;
    }

    void get_roll()
    {
        cout << "Student roll:- " << roll << endl;
    }
};

class Exam : virtual public Student
{
protected:
    int math;
    int english;

public:
    void set_marks(int x, int y)
    {
        math = x;
        english = y;
    }

    void get_marks()
    {
        cout << "Math marks:- " << math << endl;
        cout << "English marks:- " << english << endl;
    }
};

class Sports : virtual public Student
{
protected:
    int cricket;

public:
    void set_score(int x)
    {
        cricket = x;
    }

    void get_score()
    {
        cout << "Score in Cricket:- " << cricket << endl;
    }
};

class Result : public Exam, public Sports
{
protected:
    int total_score;

public:
    void get_result()
    {
        total_score = math + english + cricket;
        get_roll();
        get_marks();
        get_score();
        cout << "Your total score:- " << total_score << endl;
    }
};

int main()
{
    Result o1;
    o1.set_roll(1961206);
    o1.set_marks(90, 94);
    o1.set_score(54);
    o1.get_result();
    return 0;
}