#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, M;
char board[10][10];

typedef struct _pos{
    int y;
    int x;
    inline bool operator==(const struct _pos& a){
        if(a.y == y && a.x == x) return true;
        return false;
    }
}pos;

typedef struct _ball{
    pos red;
    pos blue;
    int prev;
    int cnt;
}ball;

pos hole;

int answer = -1;

// N E S W
int dy[] = {-1, 0, 1, 0};
int dx[] = {0, 1, 0, -1};

int move(int dir, ball& cur){
    bool red_move = true;
    bool blue_move = true;
    bool red_hole = false;
    
    int new_r_y=0;
    int new_r_x=0;
    int new_b_y=0;
    int new_b_x=0;
    
    while(true){
        if(red_move || !red_hole){
            new_r_y = cur.red.y + dy[dir];
            new_r_x = cur.red.x + dx[dir];
            
            if(board[new_r_y][new_r_x] == '.'){
                red_move = true;
                cur.red.y = new_r_y;
                cur.red.x = new_r_x;
            }else
                red_move = false;
        }
        
        if(blue_move){
            new_b_y = cur.blue.y + dy[dir];
            new_b_x = cur.blue.x + dx[dir];
            if(board[new_b_y][new_b_x] == '.'){
                blue_move = true;
                cur.blue.y = new_b_y;
                cur.blue.x = new_b_x;
            }else
                blue_move = false;
        }
        if(cur.blue == hole)
            return -1;
        
        if(cur.red == hole)
            red_hole = true;
        
        if(cur.red == cur.blue){
            if(red_move){       // if red just moved
                cur.red.y += dy[(dir+2)%4];
                cur.red.x += dx[(dir+2)%4];
                red_move = false;
            }else if(blue_move){   // if blue just moved
                cur.blue.y += dy[(dir+2)%4];
                cur.blue.x += dx[(dir+2)%4];
                blue_move = false;
            }
        }
        if(!red_move && !blue_move)
            break;
    }
    if(red_hole)
        return 1;
    return 0;
}

void bfs(ball& balls){
    queue<ball> que;
    que.push(balls);
    
    while(!que.empty()){
        ball cur = que.front();
        que.pop();
        if(cur.cnt > 9) // I spent 3 hours because I missed this.... wow....
            break;
        for(int i=0; i<4; i++){
            if(cur.prev != -1)
                // don't go same way and opposite way
                if(i == cur.prev || i == (cur.prev+2)%4)
                    continue;
               
            ball next = cur;
            next.cnt += 1;
            next.prev = i;
            
            int res = move(i, next);
            if(res == 1){
                answer = next.cnt;
                return ;
            }else if(res == -1){
                continue;
            }
            
            que.push(next);
        }
    }
}

int main(void){
    cin >> N >> M;
    
    ball balls;
    balls.cnt = 0;
    balls.prev = -1;
    for(int i=0; i != N; ++i){
        for(int j=0; j != M; ++j){
            cin >> board[i][j];
            if(board[i][j] == 'R'){
                balls.red.y = i;
                balls.red.x = j;
                board[i][j] = '.';
            }else if(board[i][j] == 'B'){
                balls.blue.y = i;
                balls.blue.x = j;
                board[i][j] = '.';
            }else if(board[i][j] == 'O'){
                hole.y = i;
                hole.x = j;
                board[i][j] = '.';
            }
        }
    }
    
    bfs(balls);
    
    cout << answer << endl;
}
