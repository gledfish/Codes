#include <iostream>

using namespace std; 

int main(){
    int max_temps[4][5];
    for(int row = 0; row < 4; row++){
        for(int col = 0; col <5; col++){
            max_temps[row][col] = row * 10 + col;
            cout << max_temps[row][col] << " ";
        }
        cout << endl;
    }
    return 0;
}