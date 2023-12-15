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
        {"red", 12}, 
        {"green", 13}, 
        {"blue", 14}, 
    };

    fstream monFichier("input2.txt", ios::in);

    size_t indice = 1;
    long somme = 0;
    string s;
    while (getline(monFichier, s)) {
        bool test = true;
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
                cout << oneGemme << endl;
                stringstream gemme(oneGemme.substr(1));
                string qte;
                string color;
                getline(gemme, qte, ' ');
                getline(gemme, color, ' ');

                cout << qte << " - " << color << endl;

                if (cube[color] < stoi(qte)) {
                    test = false;
                } 
            }
        }

        if (test) {
            somme += indice;
        }

        indice++;
    }
    cout << somme << endl;
}