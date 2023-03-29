#include <iostream>
using namespace std;

class Bank
{
    int principal;
    int loan_period;
    float interest_rate;
    float return_amount;

public:
    Bank() {}
    Bank(int p, int n, float r)
    {
        principal = p;
        loan_period = n;
        interest_rate = r;
        return_amount = principal;
        for (int i = 0; i < loan_period; i++)
        {
            return_amount = return_amount * (1 + interest_rate);
        }
    }
    Bank(int p, int n, int r)
    {
        principal = p;
        loan_period = n;
        interest_rate = float(r) / 100;
        return_amount = principal;
        for (int i = 0; i < loan_period; i++)
        {
            return_amount = return_amount * (1 + interest_rate);
        }
    }

    void get_data()
    {
        cout << "Principal Amount:- " << principal << endl
             << "Loan Period:- " << loan_period << endl
             << "Interest Rate:- " << interest_rate << endl
             << "Total Return Amount:- " << return_amount << endl;
    }
};

int main()
{
    Bank b1, b2, b3;
    int p;
    int n;
    int R;
    float r;

    cout << "Enter p, n and r(f):- " << endl;
    cin >> p >> n >> r;
    b1 = Bank(p, n, r);
    b1.get_data();

    cout << "Enter p, n and r(p):- " << endl;
    cin >> p >> n >> R;
    b2 = Bank(p, n, R);
    b2.get_data();
    return 0;
}