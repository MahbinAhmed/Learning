#include <iostream>
#include <cmath>
using namespace std;

class Graph
{
    int x;
    int y;

public:
    friend int graph_distance(Graph, Graph);
    Graph(int a, int b)
    {
        x = a;
        y = b;
    }

    void get_data()
    {
        cout << "x = " << x << " | y = " << y << endl;
    }
};

int graph_distance(Graph o1, Graph o2)
{
    int x_sub = (o2.x - o1.x);
    int y_sub = (o2.y - o1.y);
    int x_sqr = x_sub * x_sub;
    int y_sqr = y_sub * y_sub;
    int result = sqrt(x_sqr + y_sqr);
    return result;
}

int main()
{
    Graph first(1, 0), second = Graph(70, 0);
    cout << "Difference between two points = " << graph_distance(first, second) << endl;
    return 0;
}