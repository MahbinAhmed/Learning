#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main()
{
    // Taking input from the user and writing to a file
    // string user_input;
    // ofstream fout("tut61.txt");
    // cout<<"Enter a text to be written:- "<<endl;
    // cin>>user_input;
    // fout<<"\"" + user_input + "\" The quoted text was entered by user through tut61.cpp program file.";

    // Taking input from the "tut61.txt" file and writing it to the console
    string file_input;
    ifstream fin("tut61.txt");
    // fin>>file_input; // It will take first word as an input
    getline(fin, file_input); // It wil take a line as an input
    cout << file_input;
    return 0;
}