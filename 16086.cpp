#include <iostream>

#include <set>

using namespace std;

int main(){

    cin.tie(0)->ios::sync_with_stdio(0);

    int n;

    cin >> n;

    int a;

    int b;

    set<int> s;

    for(int i = 0; i < n; i ++){

        cin >> a;

        b = (i+1) - a;

        if (b < 0) {

            b = b + n;

            }

        s.insert(b);

        }

    int c = 0;

    for(auto i : s){

        if(i != c) {

            cout << c;

            return 0;

        }

        c++;

        }

    if (c != n){

        cout << c;

        return 0;

    }

    cout << -1;

    return 0;

}
