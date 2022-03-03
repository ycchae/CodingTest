#include <iostream>
#include <queue>

using namespace std;
typedef struct _p{
    int y;
    int x;
    int time;
}pos;
typedef struct _pipe{
    bool open[4];       // N S W E
}pipe;

bool p[8][4] = {
    {false, false, false, false},
    {true, true, true, true},
    {true, true, false, false},
    {false, false, true, true},
    {true, false, false, true},
    {false, true, false, true},
    {false, true, true, false},
    {true, false, true, false}
};
bool visited[51][51];
pipe map[51][51];
int N, M, R, C, L;

// N S W E
int dy[] = {-1, 1, 0, 0};
int dx[] = {0, 0, -1, 1};

int bfs(){
    queue<pos> que;
    int answer = 1;
    
    que.push({R, C, 1});
    visited[R][C] = true;
    
    while(!que.empty()){
        pos cur = que.front();
        que.pop();
        if(cur.time >= L)
            break;
        for(int i=0; i<4; ++i){
            int ny = cur.y + dy[i];
            int nx = cur.x + dx[i];
            
            if(ny < 0 || ny >= N || nx < 0 || nx >= M)
                continue;
            if(visited[ny][nx])
                continue;
            // 현재 위치에서 방향쪽이 안 열려 있으면 no push
            if(!map[cur.y][cur.x].open[i])
                continue;
            // 반대가 열려 있을 때
            if(i < 2){          // N S 방향
                if(map[ny][nx].open[(i+1)%2]){
                    visited[ny][nx] = true;
                    que.push({ny, nx, cur.time+1});
                    ++answer;
                }
            }else{              // W E 방향
                if(map[ny][nx].open[(i+1)%2+2]){
                    visited[ny][nx] = true;
                    que.push({ny, nx, cur.time+1});
                    ++answer;
                }
            }
        }
        
    }
    return answer;
}
int solution(){
    int val;
    scanf("%d %d %d %d %d", &N, &M, &R, &C, &L);
    for(int i=0; i<N; ++i){
        for(int j=0; j<M; ++j){
            scanf("%d", &val);
            memcpy(map[i][j].open, p[val], sizeof(p[val]));
            visited[i][j] = false;
        }
    }
    
    return bfs();
}

int main(void){
    int testcase;
    scanf("%d", &testcase);
    for(int i=1; i<=testcase; ++i){
        printf("#%d %d\n", i, solution());
    }
    return 0;
}

