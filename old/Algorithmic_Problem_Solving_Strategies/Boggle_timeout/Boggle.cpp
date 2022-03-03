#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

bool has_word(int y, int x, const string& word);

string maps[5];

int main(void){
    int C=0, N=0;
    
    freopen("input.txt","r",stdin);
    cin >> C;
    while(C != 0){
        for(int i=0; i != 5; ++i)
            cin >> maps[i];
        
        cin >> N;
        for(int i=0; i != N; i++){
            string word;
            cin >> word;

            cout << word << ' ';
            int y, x;
            bool hasWord = false;
            for(y=0; y != 5; y++){
                for(x=0; x != 5; x++){         // find the first letter
                    if(word[0] == maps[y][x]){
                        if(has_word(y, x, word))
                            hasWord = true;
                    }
                }
            }

            if(hasWord)
                printf("YES\n");
            else
                printf("NO\n");
        }

        N = 0;
        C -= 1;
    }
    return 0;
}

const int dy[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dx[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
bool has_word(int y, int x, const string& word){
    if(y == 5 || x == 5 || y == -1 || x == -1) return false;
    if(maps[y][x] != word[0]) return false;
    if(word.size() == 1) return true;
    for(int i=0; i<8; i++){
        int nextY = y + dy[i];
        int nextX = x + dx[i];
        if(has_word(nextY, nextX, word.substr(1)))
            return true;
    }
    return false;
}
