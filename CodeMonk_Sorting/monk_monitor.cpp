#include <iostream>
#include <list>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iterator>
using namespace std;

int main() {
    int T, N, Si;
    cin >> T;
    for(int x = 0; x < T; x++) {
        vector<int> S;
        list<int> heights;
        cin >> N;
        for(int y = 0; y < N; y++) {
            cin >> Si;
            S.push_back(Si);
            heights.push_back(Si);
        }
        heights.unique();
        vector<int> heights_v{begin(heights), end(heights)};

        int m = 0;
        for(int i = 0; i < heights.size(); i++) {
            for(int j = 0; j < heights.size(); j++) {
                if(i != j) {
                    int d;
                    d = abs(count(S.begin(),S.end(),heights_v[i]) - count(S.begin(),S.end(),heights_v[j]));
                    if(d > m) {
                        m = d;
                    }
                }
            }
        }
        if(m == 0)
            cout << -1 << endl;
        else
            cout << m << endl;
    }
}
