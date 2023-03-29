#include <iostream>
#include <vector>
using namespace std;

template <class T>
void display(vector<T> &vec)
{
    for (int i = 0; i < vec.size(); i++)
    {
        cout << vec.at(i) << ", ";
    }
    cout << endl;
}

int main()
{
    vector<int> vec1;       // Zero size vector
    vector<char> vec2(4);   // Vector with 4 element
    vector<int> vec3(4, 3); // Vector with 4 3s
    vector<int> vec4(vec3); // Same as vec3
    // vector<int>
    // int user_inp,size;
    // cout<<"What will be the size of the vector:- ";
    // cin>>size;
    // for(int i=0;i<size;i++){
    //     cout<<"Enter value for "<<i+1<<"th index:- ";
    //     cin>>user_inp;
    //     vec1.push_back(user_inp);
    // }
    // display(vec1);
    // cout<<"Inserting a random number..."<<endl;
    // vector<int>:: iterator itr = vec1.begin();
    // vec1.insert(itr, 53);
    // display(vec1);
    // vector<char>:: iterator itr2 = vec2.begin();
    // vec2.insert(itr2+2, '5');
    // display(vec2);
    // display(vec3);
    display(vec4);
    return 0;
}