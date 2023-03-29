#include <iostream>
#include <map>
#include <string>
using namespace std;

int main()
{
    map<string, int> o1;
    o1["John"] = 34;
    o1["Alex"] = 20;
    o1["Sam"] = 65;
    o1.insert({{"Rock", 67}, {"Henry", 56}});
    map<string, int>::iterator itr;
    for (itr = o1.begin(); itr != o1.end(); itr++)
    {
        cout << (*itr).first << " = " << (*itr).second << endl;
    }
    cout << o1.size() << endl;
    cout << o1.max_size() << endl;
    ;
    cout << o1.empty() << endl;
    return 0;
}