#include<iostream>
using namespace std;

int main(){
    int user_inp;
    cin>>user_inp;

    // If-else ladder and Switch case are the main mechanisms of Selection structure

    // If-else ladder
    // if(user_inp<10){
    //     cout<<"You entered a number less than 10\n";
    // }
    // else if(user_inp<20){
    //     cout<<"You entered a number less than 20\n";
    // }
    // else if(user_inp<50){
    //     cout<<"You entered a number less than 50\n";
    // }
    // else{
    //     cout<<"You entered a number greater than 50\n";
    // }

    // Switch case
    switch (user_inp)
    {
    case 10:
        cout<<"You entered 10\n";
        break;

    case 20:
        cout<<"You entered 20\n";

    default:
        cout<<"You entered a number other than 10 and 20\n";
        break;
    }
}