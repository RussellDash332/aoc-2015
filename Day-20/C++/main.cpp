#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int target, n = 1000000;
    cin >> target;

    int presents[n];
    for (int i = 1; i < n; i++) {
        int tmp = i - 1;
        while (tmp < n) {
            presents[tmp] += 10 * i;
            tmp += i;
        }
        if (presents[i - 1] >= target) {
            cout << "Part 1: " << i << endl;
            break;
        }
    }

    fill(presents, presents + n, 0);
    for (int i = 1; i < n; i++) {
        int tmp = i - 1;
        for (int j = 0; j < 50 && tmp < n; j++) {
            presents[tmp] += 11 * i;
            tmp += i;
        }
        if (presents[i - 1] >= target) {
            cout << "Part 2: " << i << endl;
            break;
        }
    }

    return 0;
}