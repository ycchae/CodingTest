#include <iostream>
#include <vector>

using namespace std;

typedef struct _h{
    int y;
    int x;
    int height;
}hill;

int N, K;
int map[9][9];
bool visited[9][9];
hill hills[5];
int max_height;
int answer = 0;

// N E S W
int dy[] = {-1, 0, 1, 0};
int dx[] = {0, 1, 0, -1};

void dfs(int y, int x, int length, bool can){
    answer = max(length, answer);
    
    for(int i=0; i<4; ++i){
        int ny = y + dy[i];
        int nx = x + dx[i];
        if(ny < 0 || ny >= N || nx < 0 || nx >= N)
            continue;
        if(visited[ny][nx])
            continue;
        
        if(map[y][x] <= map[ny][nx] && can == false){
            for(int cut=1; cut<=K; ++cut){
                int before = map[ny][nx];
                int after = map[ny][nx] - cut;
                
                if(map[y][x] > after){
                    map[ny][nx] = after;
                    visited[ny][nx] = true;
                    dfs(ny, nx, length+1, true);
                    map[ny][nx] = before;
                    visited[ny][nx] = false;
                }
            }
        }else if(map[ny][nx] < map[y][x]){
            visited[ny][nx] = true;
            dfs(ny, nx, length+1, can);
            visited[ny][nx] = false;
        }
    }
}
int solution(){
    max_height = 0;
    answer = 0;
    int i, j, hills_size;
    
    for(i=0; i<N; ++i)
        for(j=0; j<N; ++j)
            visited[i][j] = false;
    
    scanf("%d %d", &N, &K);
    for(i=0; i<N; ++i){
        for(j=0; j<N; ++j){
            scanf("%d", &map[i][j]);
            if(max_height < map[i][j])
                max_height = map[i][j];
        }
    }
    
    hills_size=0;
    for(i=0; i<N; ++i){
        for(j=0; j<N; ++j){
            if(map[i][j] == max_height){
                hills[hills_size] = {i, j, map[i][j]};
                ++hills_size;
            }
        }
    }
    for(i=0; i<hills_size; ++i){
        visited[hills[i].y][hills[i].x] = true;
        dfs(hills[i].y, hills[i].x, 1, false);
        visited[hills[i].y][hills[i].x] = false;
    }
    
    return answer;
}
int main(void){
    int testcase;
    scanf("%d", &testcase);
    for(int i=1; i<=testcase; ++i){
        printf("#%d %d\n", i, solution());
    }
    return 0;
}
