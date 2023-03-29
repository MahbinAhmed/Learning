#include <iostream>
using namespace std;

class Student
{
    int id;
    static int counter;

public:
    void set_data()
    {
        cout << "Enter your ID no. ";
        cin >> id;
        counter++;
        cout << "Student no. " << counter << endl;
    }

    static void get_count();
};

int Student::counter; // This line must be written outside the class

void Student::get_count()
{
    cout << "Total student count is " << counter << endl;
}

int main()
{
    Student s1;
    s1.set_data();
    Student::get_count();

    Student s2;
    s2.set_data();
    Student::get_count();

    Student s3;
    s3.set_data();
    Student::get_count();
    return 0;
}