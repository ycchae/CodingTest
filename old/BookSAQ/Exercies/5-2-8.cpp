#include <iostream>
#include <queue>

using namespace std;

typedef struct _pos{
    int y;
    int x;
}pos;
int N, M;
int field[7][7];
int fired;

// N E S W
int dy[] = {-1, 0, 1, 0};
int dx[] = {0, 1, 0, -1};

void bfs(){
    queue<pos> que;
    int copy_field[7][7];
    int new_fired = 0;
    
    for(int y=0; y<N; y++){
        for(int x=0; x<N; x++){
            copy_field[y][x] = field[y][x];
            if(copy_field[y][x] == 2){
                pos start = {y, x};
                que.push(start);
                new_fired++;
            }
        }
    }
        
    while(!que.empty()){
        pos cur = que.front();
        que.pop();
        
        for(int i=0; i<4; i++){
            int new_y = cur.y + dy[i];
            int new_x = cur.x + dx[i];
            if(new_y >= N || new_y < 0 || new_x >= N || new_x < 0)
                continue;
            if(copy_field[new_y][new_x] == 0){
                copy_field[new_y][new_x] = 3;
                pos new_cur = {new_y, new_x};
                que.push(new_cur);
                new_fired++;
            }
        }
    }
    
    // fired minimize
    if(fired == 0 || fired > new_fired){
        fired = new_fired;
    }
    
}
void dfs(int y, int x, int depth){
    if(depth == M){
        bfs();
        return;
    }
    
    for(int i = y*N + x; i < N*N; i++){
        int next_y = i / N;
        int next_x = i % N;
        if(field[next_y][next_x] == 0){
            field[next_y][next_x] = 1;
            dfs(next_y, next_x, depth+1);
            field[next_y][next_x] = 0;
        }
    }
    
}

int main(void){
    int n;
    int barrier;
    
    freopen("input.txt","r",stdin);
    
    cin >> n;
    while(n-- > 0){
        // initialize
        cin >> N >> M;
        memset(field, -1, sizeof(field));
        fired = 0;
        barrier = 0;
        
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                cin >> field[i][j];
                if(field[i][j] == 1)
                    barrier++;
            }
        }
        
        // build barriers by dfs and check by bfs
        dfs(0, 0, 0);
        int answer = N*N - fired - barrier - M;
        
        
        cout << answer <<endl;
    }
}
