#include<iostream>
#include<string>
using std::cout;
using std::cin;
using std::endl;
using std::string;

class Employee{
    private:
    int salary;
    // friend int get_salary(Employee); // Friend function
    protected:
    string name;
    int age;
    public:

    Employee(){}
    Employee(string name, int age, int salary){
        this->name = name; // this pointer
        this->age = age;
        this->salary = salary;
    }
    void set_name(string ename){
        name = ename;
    }

    string get_name(){
        return name;
    }

    int get_age(){
        return age;
    }
    virtual void work(){
        cout<<name<<" is writing email."<<endl;
    }
    virtual void pure_virtual_function()=0;
};

class Programmer: public Employee{
    private:
    string fav_lang;
    int project_done;
    friend int get_project_done(Programmer);
    public:
    Programmer(){}
    Programmer(string name, int age, int salary, string fav_lang, int project_done): Employee(name, age, salary){
        this->fav_lang = fav_lang;
        this->project_done = project_done;
    }

    void work(){
        cout<<name<<" is making software with "<<fav_lang<<endl;
    }

    void pure_virtual_function(){
        int a = 5;
    }

    void work_demo(){
        cout<<"Hello World"<<endl;
    }

};

// int get_salary(Employee a){ // Friend function of Employee class || Friend function can't be made of Abstract class
//     return a.age;
// }

int get_project_done(Programmer a){ // Friend function of Programmer class
    return a.project_done;
}

int main(){
    // Employee o1; // Object can't be made from Abstract class
    // o1 = Employee("Alex", 25, 50000);
    // cout<<o1.get_age()<<endl;
    // cout<<get_salary(o1)<<endl;
    
    Programmer o2;
    o2 = Programmer("John", 30, 60000, "C++", 20);
    cout<<o2.get_name()<<endl;
    cout<<get_project_done(o2)<<endl;
    
    Employee *ptr = &o2; // Base class pointer pointing to Derived class object
    // ptr->work_demo(); // Derived class's functions can't be accessed with Base class pointer
    ptr->work(); // work() function of Base class will be run as the pointer is of Base class
    return 0;
}