#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main()
{
    // string inp1;
    // inp1 = "Hello World!\nThis is a line written by tut62.cpp program file.\nThis was written by C++ program.\nThis file has multiple text line.";
    // ofstream fout;
    // fout.open("tut62.txt");
    // fout<<inp1;
    // fout.close();

    string inp2;
    ifstream fin;
    fin.open("tut62.txt");
    while (fin.eof() == 0)
    {
        getline(fin, inp2);
        cout << inp2 << endl;
    }

    return 0;
}