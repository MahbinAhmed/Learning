#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main()
{
    // Writing to a file using ofstream class
    // string txt = "Hey there! This line is written using tut60.cpp program.";
    // ofstream out("tut60.txt");
    // out << txt;

    // Reading from a file using ifstream class
    string str;
    ifstream in("tut60.txt");
    // in>>str; // This will take only the first word of the file as an input
    getline(in, str); // This will take a line of the file as an input
    cout << str;
    return 0;
}