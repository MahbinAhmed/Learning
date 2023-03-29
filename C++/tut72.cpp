#include <iostream>
#include <list>
using namespace std;

void display(list<int> ls)
{
    list<int>::iterator itr = ls.begin();
    for (itr; itr != ls.end(); itr++)
    {
        cout << *itr << ", ";
    }
    cout << endl;
}

int main()
{
    list<int> ls1;    // List with zero elements
    list<int> ls2(3); // List with 3 empty elements

    ls1.push_back(4);
    ls1.push_back(7);
    ls1.push_back(43);
    ls1.push_back(12);
    ls1.push_back(5);
    ls1.push_back(9);
    display(ls1);
    ls1.pop_back();
    ls1.pop_front();
    ls1.remove(12);
    display(ls1);

    list<int>::iterator itr = ls2.begin();
    *itr = 34;
    itr++;
    *itr = 96;
    itr++;
    *itr = 53;
    itr++;
    *itr = 74;
    display(ls2);
    ls1.reverse();
    display(ls1);
    return 0;
}