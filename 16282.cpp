#include <iostream>
#include <cmath>
using namespace std;
long long int n;
int main(){
    cin >> n;
    int k = 1;
    while(((k+1)* (long long)pow(2,k+1)-1 ) < n ) k++;
    cout << k;
    return 0;
}
