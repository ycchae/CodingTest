#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <cstring>

using namespace std;

typedef struct _pos{
    int y;
    int x;
}pos;

typedef struct st_union{
    int members[100];
    int people;
    int num;
}_union;

int N, L, R;
int nations[100][100];
bool visited[100][100];
vector<_union> unions;

// N E S W
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};

int solution(){
    int answer = 0;
    queue<pos> que;

    while(1){
        int n=-1;
        unions.clear();
        
        for(int i=0; i<N; ++i)
            memset(visited[i], false, sizeof(visited[i]));
        
        // check can be union and make union group
        for(int y=0; y<N; ++y){
            for(int x=0; x<N; ++x){
                if(visited[y][x]){
                    continue;
                }
                
                ++n;
                unions.push_back({{}, 0, 0});
                visited[y][x] = true;
                que.push({y,x});
                
                while(!que.empty()){
                    pos cur = que.front();
                    que.pop();
                    
                    unions[n].members[unions[n].num] = cur.y*N + cur.x;
                    unions[n].people += nations[cur.y][cur.x];
                    ++unions[n].num;
                    
                    int new_y, new_x;
                    for(int i=0; i<4; i++){
                        new_y = cur.y + dy[i];
                        new_x = cur.x + dx[i];
                        if(new_y < 0 || new_y > N-1 || new_x < 0 || new_x > N-1)
                            continue;
                        if(visited[new_y][new_x])
                            continue;
                        int diff = abs(nations[cur.y][cur.x] - nations[new_y][new_x]);
                        if(diff >= L && diff <= R){
                            que.push({new_y, new_x});
                            visited[new_y][new_x] = true;
                        }
                    }
                }
            }
        }
        
        // no union
        if(unions.size() == N*N)
            return answer;
        
        for(int i=0; i<unions.size(); ++i){
            for(int j=0; j<unions[i].num; ++j){
                int y = unions[i].members[j]/N;
                int x = unions[i].members[j]%N;
                nations[y][x] = unions[i].people / unions[i].num;
            }
        }
        
        for(int i=0; i<N; ++i){
            for(int j=0; j<N; ++j){
                printf("%4d", nations[i][j]);
            }
            cout << endl;
        }
        cout << endl;

        ++answer;
    }
    return answer;
}

int main(void){
    cin >> N >> L >> R;
    for(int i=0; i!=N; ++i){
        for(int j=0; j!=N; ++j){
            cin >> nations[i][j];
        }
    }
    cout << solution() << endl;
}
