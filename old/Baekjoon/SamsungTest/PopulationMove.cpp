#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

typedef struct _pos{
    int y;
    int x;
}pos;

int N, L, R;
int nations[51][51];
int visited[51][51];

// N E S W
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};

int solution(){
    int answer = 0;
    queue<pos> que;
    queue<pos> unions;
    bool loop = true;
    // 인구이동
    while(loop){
        loop = false;
        ++answer;
        // union 찾기
        for(int y=0; y<N; ++y){
            for(int x=0; x<N; ++x){
                if(visited[y][x] == answer)
                    continue;
                int sum = nations[y][x];
                que.push({y, x});
                unions.push({y, x});
                visited[y][x] = answer;

                while(!que.empty()){
                    pos cur = que.front();
                    que.pop();

                    for(int i=0; i<4; ++i){
                        int new_y = cur.y + dy[i];
                        int new_x = cur.x + dx[i];

                        if(new_y < 0 || new_y > N-1 || new_x < 0 || new_x > N-1)
                            continue;
                        if(visited[new_y][new_x] == answer)
                            continue;
                        int diff = abs(nations[cur.y][cur.x] - nations[new_y][new_x]);
                        if(diff >= L && diff <= R){
                            // union 이 하나 이상일 때만 인구 이동
                            loop = true;
                            que.push({new_y, new_x});
                            unions.push({new_y, new_x});
                            sum += nations[new_y][new_x];
                            visited[new_y][new_x] = answer;
                        }
                    }
                }

                int average = sum / unions.size();
                while(!unions.empty()){
                    int n_y = unions.front().y;
                    int n_x = unions.front().x;
                    unions.pop();
                    nations[n_y][n_x] = average;
                }
            } // x
        } // y
        
    } // while
    return answer-1;
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