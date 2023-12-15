#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>
using namespace std;



int main() {
    map<string, int> m {
        {"one", 1}, 
        {"two", 2}, 
        {"three", 3}, 
        {"four", 4}, 
        {"five", 5}, 
        {"six", 6},
        {"seven", 7}, 
        {"eight", 8}, 
        {"nine", 9},
        {"1", 1}, 
        {"2", 2}, 
        {"3", 3}, 
        {"4", 4}, 
        {"5", 5}, 
        {"6", 6},
        {"7", 7}, 
        {"8", 8}, 
        {"9", 9}
    };


    fstream monFichier("input1.txt", ios::in);

    long somme = 0;
    string s;
    while (getline(monFichier, s)) {
        size_t minDist = s.length() +1;
        long minVal = 0;
        size_t maxDist = 0;
        long maxVal = 0;

        for (const auto &[cle, valeur] : m ) {
            size_t pos = s.find(cle);
            if (minDist > pos && pos != string::npos) {
                minDist = pos;
                minVal = m[cle];
            }

            pos = s.rfind(cle);
            if (maxDist <= pos && pos != string::npos) {
                maxDist = pos;
                maxVal = m[cle];
            }
        }

        cout << s << " - " << minVal << " - " << maxVal << endl; 

        somme += (minVal * 10) + maxVal;
    }
    cout << somme << endl;
}