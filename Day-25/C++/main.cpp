#include <bits/stdc++.h>
#include <sstream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    string line;
    getline(cin, line);

    stringstream ss;
    ss << line;

    int r = 0, c = 0;
    string word;
    while (!ss.eof()) {
        ss >> word;
        if (r == 0) {
            stringstream(word) >> r;
        } else {
            stringstream(word) >> c;
        }
    }

    long ans = 20151125;
    for (int i = 0; i < (r + c) * (r + c - 1) / 2 - r; i++) {
        ans = 252533 * ans % 33554393;
    }

    cout << "Part 1: " << ans << endl;
    cout << "Part 2: THE END!" << endl;

    return 0;
}