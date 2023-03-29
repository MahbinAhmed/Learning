#include <iostream>
using namespace std;

class Student
{
    int id;
    int grade;
    int admission_year;

public:
    Student(int x, int y, int z = 2023)
    {
        id = x;
        grade = y;
        admission_year = z;
    }
    void get_data()
    {
        cout << "Student ID: " << id << endl;
        cout << "Student Grade: " << grade << endl;
        cout << "Admission Year: " << admission_year << endl;
        cout << endl;
    }
};

int main()
{
    Student s1(1961206, 10, 2019), s2(1961207, 10);
    s1.get_data();
    s2.get_data();
    return 0;
}