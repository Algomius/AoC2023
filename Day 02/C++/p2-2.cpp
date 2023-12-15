#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>
using namespace std;



int main() {
    map<string, int> cube {
        {"red", 0}, 
        {"green", 0}, 
        {"blue", 0}, 
    };

    fstream monFichier("input2.txt", ios::in);

    long somme = 0;
    string s;
    while (getline(monFichier, s)) {
        cube["red"] = 0;
        cube["green"] = 0;
        cube["blue"] = 0;
        stringstream ligne(s);
        
        string gameNumber;
        string gameValues;
        getline(ligne, gameNumber, ':');
        getline(ligne, gameValues, ':');

        stringstream hands(gameValues);
        string oneHand;
        while (getline(hands, oneHand, ';')) {
            stringstream turn(oneHand);
            string oneGemme;
            while (getline(turn, oneGemme, ',')) {
                stringstream gemme(oneGemme.substr(1));
                string qte;
                string color;
                getline(gemme, qte, ' ');
                getline(gemme, color, ' ');

                if (cube[color] < stoi(qte)) {
                    cube[color] = stoi(qte);
                } 
            }
        }

        somme += (cube["red"] * cube["blue"] * cube["green"]);
    }
    cout << somme << endl;
}