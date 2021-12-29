#include <bits/stdc++.h>
#include <sstream>
#include <vector>
using namespace std;

vector<string> split (const string &s, char delim) {
    vector<string> result;
    stringstream ss(s);
    string item;

    while (getline(ss, item, delim)) {
        result.push_back(item);
    }

    return result;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int area = 0, ribbon = 0;
    string s;
    while (cin >> s) {
        vector<string> xyz = split(s, 'x');
        int x = stoi(xyz[0]), y = stoi(xyz[1]), z = stoi(xyz[2]);
        area += 2 * (x * y + y * z + z * x) + min(min(x * y, y * z), z * x);
        ribbon += 2 * (x + y + z - max(max(x, y), z)) + x * y * z;
    }

    cout << "Part 1: " << area << endl;
    cout << "Part 2: " << ribbon << endl;

    return 0;
}