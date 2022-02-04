#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <cstring>
using namespace std;

typedef struct _pos{
    int point;
    int time;
}pos;

int N, M;
int map[50][50];
int virus_num = 0;
int wall_num = 0;

// N E S W
int dy[] = {-1, 0, 1, 0};
int dx[] = {0, 1, 0, -1};

vector<int> selected;

int answer = INT_MAX;
int cp[50][50];
int bfs(){
    queue<pos> que;
    int nvirus = virus_num;
    
    for(int i=0; i<N; ++i){
        memcpy(cp[i], map[i], sizeof(map[i]));
    }
    
    for(int i=0; i<M; ++i){
        que.push({selected[i], 0});
        cp[selected[i]/N][selected[i]%N] = 3;
    }
    
    while(!que.empty()){
        pos cur = que.front();
        que.pop();
        
        for(int i=0; i<4; ++i){
            int new_y = cur.point/N + dy[i];
            int new_x = cur.point%N + dx[i];
            
            if(new_y < 0 || new_y >= N || new_x < 0 || new_x >= N)
                continue;
            if(cp[new_y][new_x] == 1)
                continue;
            if(cp[new_y][new_x] == 3)
                continue;
            if(cp[new_y][new_x] == 0)
                ++nvirus;
            cp[new_y][new_x] = 3;
            if(N*N - wall_num - nvirus == 0)
                return cur.time+1;
            
            que.push({new_y*N + new_x, cur.time+1});
        }
    }
    
    return -1;
}

void dfs(int cur, int depth){
    if(depth == M){
        int ret = bfs();
        if(answer == INT_MAX || (ret != -1 && answer == -1)){
            answer = ret;
        }
        if(answer != -1 && ret != -1 && answer > ret){
            answer = ret;
        }

        return ;
    }
    
    for(int i=cur; i<N*N; ++i){
        int y = i / N;
        int x = i % N;
        if(map[y][x] == 2){
            selected.push_back(i);
            dfs(i+1, depth+1);
            selected.pop_back();
        }
    }
}
int main(void){
    cin >> N >> M;
    
    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            cin >> map[i][j];
            if(map[i][j] == 2)
                ++virus_num;
            else if(map[i][j] == 1)
                ++wall_num;
        }
    }
    if(N*N - wall_num - virus_num != 0)
        dfs(0, 0);
    else
        answer = 0;
    
    cout << answer << endl;
}
