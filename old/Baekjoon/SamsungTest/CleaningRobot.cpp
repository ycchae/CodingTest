#include <iostream>

using namespace std;

typedef struct _robot{
    int y;
    int x;
    int dir;
}robot;

int N, M;
int board[50][50];

// North West South East
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, -1, 0, 1};

// N E S W
// int dy[4] = {-1, 0, 1, 0};
// int dx[4] = {0, 1, 0, -1};


int solution(robot init){
    int answer = 0;
    
    int new_dir = -1, new_y = -1, new_x = -1;
    int i;
    robot cur = init;
    while(1){
        if(board[cur.y][cur.x] == 0){
            board[cur.y][cur.x] = 2;
            answer++;
        }

        new_dir = cur.dir;
        for(i=0; i != 4; ++i){
           new_dir = (new_dir+1)%4;
            // new_dir = (new_dir + 3) % 4;
            new_y = cur.y + dy[new_dir];
            new_x = cur.x + dx[new_dir];
            if(board[new_y][new_x] == 0)
                break;
        }
        
        if(i == 4){ // go back
            new_y = cur.y + dy[(new_dir+2)%4];
            new_x = cur.x + dx[(new_dir+2)%4];
            if(board[new_y][new_x] == 1){
                break;
            }

            cur.y = new_y;
            cur.x = new_x;
        }else{  // go ahead
            cur.y = new_y;
            cur.x = new_x;
            cur.dir = new_dir;
        }
    }
    
    return answer;
}
int main(void){
    cin >> N >> M;
    robot init;
    cin >> init.y >> init.x >> init.dir;
   if(init.dir == 1)
       init.dir = 3;
   else if(init.dir == 3)
       init.dir = 1;

    for(int i=0; i != N; ++i){
        for(int j=0; j != M; ++j){
            cin >> board[i][j];
        }
    }
    
    cout << solution(init) << endl;
}