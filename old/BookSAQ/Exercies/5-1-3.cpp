#include <iostream>

using namespace std;
enum move_dir {N, E, S, W};

typedef struct st_pos{
    int x;
    int y;
    int dir;
}pos;

int _N, M;
bool visited[51][51] = {false,};
int board[51][51] = {0,};
// N E S W
int x_move[] = {0, 1, 0, -1};
int y_move[] = {-1, 0, 1, 0};

bool can_move(int y, int x){
    return y<_N && x<M && !visited[y][x] && board[y][x] == 0;
}
bool isWall(int y, int x){
    return y<_N && x<M && board[y][x] == 1;
}
int solution(pos cur){
    int cnt=0, i=0;
    int next_x=0, next_y=0;
    
    while(true){
        visited[cur.y][cur.x] = true;
//        cout << "=======" << endl;
//        for(int a=0; a<_N; a++){
//            for(int b=0; b<M; b++){
//                cout << visited[a][b] << ' ';
//            }
//            cout << endl;
//        }
        for(i=0; i<4; i++){
            if(cur.dir == N){
                next_y = cur.y + y_move[N];
                next_x = cur.x + x_move[N];
                if(can_move(next_y, next_x)){
                    cur.y = next_y;
                    cur.x = next_x;
                    break;
                }else{
                    cur.dir = E;
                }
            }else if(cur.dir == E){
                next_y = cur.y + y_move[E];
                next_x = cur.x + x_move[E];
                if(can_move(next_y, next_x)){
                    cur.y = next_y;
                    cur.x = next_x;
                    break;
                }else{
                    cur.dir = S;
                }
            }else if(cur.dir == S){
                next_y = cur.y + y_move[S];
                next_x = cur.x + x_move[S];
                if(can_move(next_y, next_x)){
                    cur.y = next_y;
                    cur.x = next_x;
                    break;
                }else{
                    cur.dir = W;
                }
            }else if(cur.dir == W){
                next_y = cur.y + y_move[W];
                next_x = cur.x + x_move[W];
                if(can_move(next_y, next_x)){
                    cur.y = next_y;
                    cur.x = next_x;
                    break;
                }else{
                    cur.dir = N;
                }
            }
        }
        if(i == 4){
            if(cur.dir == N){
                next_y = cur.y + y_move[S];
                next_x = cur.x + x_move[S];
            }
            else if(cur.dir == E){
                next_y = cur.y + y_move[W];
                next_x = cur.x + x_move[W];
            }else if(cur.dir == S){
                next_y = cur.y + y_move[N];
                next_x = cur.x + x_move[N];
            }else if(cur.dir == W){
                next_y = cur.y + y_move[E];
                next_x = cur.x + x_move[E];
            }
            if(isWall(next_y, next_x)){
                break;
            }else{
                cur.y = next_y;
                cur.x = next_x;
            }
        }
        cnt++;
    }

    return cnt;
}
int main(void){
    int n;
    pos cur;
    
    freopen("input.txt","r",stdin);
    
    cin >> n;
    while(n-- != 0){
        cin >> _N >> M;
        int y, x;
        cin >> y >> x >> cur.dir;
        cur.y = y-1;
        cur.x = x-1;
        
        for(int i=0; i<_N; i++)
            for(int j=0; j<M; j++)
                cin >> board[i][j];
//        for(int i=0; i<_N; i++){
//            for(int j=0; j<M; j++) cout << board[i][j] << ' ';
//            cout << endl;
//        }
            
        cout << solution(cur) << endl;
        for(int i=0; i<_N; i++)
            for(int j=0; j<M; j++){
                visited[i][j] = false;
                board[i][j] = 0;
            }
    }
}
