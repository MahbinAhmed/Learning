#include <iostream>
using namespace std;

class Shop
{
    int item_ID;
    int item_price;

public:
    void set_data(int x, int y)
    {
        item_ID = x;
        item_price = y;
    }
    void get_data()
    {
        cout << "Item ID:- " << item_ID << endl;
        cout << "Item Price:- " << item_price << endl;
        cout << endl;
    }
};

int main()
{
    int size = 3;
    Shop *ptr = new Shop[size];
    Shop *ptr2 = ptr;
    int id, price;

    for (int i = 0; i < size; i++)
    {
        cout << "Item no. " << (i + 1) << endl;
        cout << "Enter ID of your item:- ";
        cin >> id;
        cout << "Enter Price of your item:- ";
        cin >> price;
        ptr += i;
        ptr->set_data(id, price);
        cout << endl;
    }
    cout << endl;
    cout << "Store Item List:- " << endl
         << endl;
    for (int i = 0; i < size; i++)
    {
        cout << "Item no. " << (i + 1) << endl;
        ptr2 += i;
        ptr2->get_data();
        cout << endl;
    }
    return 0;
}