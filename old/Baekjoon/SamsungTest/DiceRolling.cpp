#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

int N, M, K;
int map[20][20];
queue<int> cmd;
int dices[7];
// E W N S
int dy[4] = {0, 0, -1, 1};
int dx[4] = {1, -1, 0, 0};

// y == row x == col
void solution(int& y, int &x){
    while(!cmd.empty()){
        int dir = cmd.front();
        cmd.pop();
        int new_y = y + dy[dir];
        int new_x = x + dx[dir];
        
        if(new_y == -1 || new_y == N || new_x == -1 || new_x == M)
            continue;
        
        int tmp[7];
        memcpy(tmp, dices, sizeof(dices));
        
        switch(dir){
            case 0: // EAST
                dices[1] = tmp[4];
                dices[3] = tmp[1];
                dices[4] = tmp[6];
                dices[6] = tmp[3];
                break;
            case 1: // WEST
                dices[1] = tmp[3];
                dices[3] = tmp[6];
                dices[4] = tmp[1];
                dices[6] = tmp[4];
                break;
            case 2: // NORTH
                dices[1] = tmp[5];
                dices[2] = tmp[1];
                dices[5] = tmp[6];
                dices[6] = tmp[2];
                break;
            case 3: // SOUTH
                dices[1] = tmp[2];
                dices[2] = tmp[6];
                dices[5] = tmp[1];
                dices[6] = tmp[5];
                break;
        }
        
        if(map[new_y][new_x] == 0){
            map[new_y][new_x] = dices[6];
            // dices[6] = 0;
        }else{
            dices[6] = map[new_y][new_x];
            map[new_y][new_x] = 0;
        }
        
        cout << dices[1] << endl;

        y = new_y;
        x = new_x;
    }
}
int main(void){
    int x, y;
    
    cin >> N >> M >> y >> x >> K;
    for(int i=0; i != N; ++i){
        for(int j=0; j != M; ++j){
            cin >> map[i][j];
            if(i == 0 && j == 0 && map[i][j] != 0){
                dices[6] = map[i][j];
            }
        }
    }
    for(int i=0; i != K; ++i){
        int t;
        cin >> t;
        cmd.push(--t);
    }
    memset(dices, 0, sizeof(dices));
    
    solution(y, x);
    return 0;
}
