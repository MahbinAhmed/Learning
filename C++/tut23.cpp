#include<iostream>
using namespace std;

class shop{
    public:
    int itemId[100];
    int itemPrice[100];
    int counter=0;
    void set_price();
    void get_price();
};

void shop :: set_price(){
    int inp_quan;
    cout<<"Enter product quantity to add :- ";
    cin>>inp_quan;
    for(int i=0;i<inp_quan;i++){
        cout<<"Enter product ID of item :- "<<counter+1<<endl;
        cin>>itemId[counter];
        cout<<"Enter price for prodcut :- "<<counter+1<<endl;
        cin>>itemPrice[counter];
        counter++;
    }
    cout<<endl;
}

void shop :: get_price(){
    for(int i=0;i<counter;i++){
        cout<<i+1<<". Product ID: "<<itemId[i]<<" Product Price: "<<itemPrice[i]<<endl;
    }
}

int main(){
    shop shop1;
    shop1.set_price();
    shop1.get_price();
    return 0;
}