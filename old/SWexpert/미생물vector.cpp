#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef struct _m{
    int y;
    int x;
    int size;
    int dir;
}microbe;

int N, M, K;

// NOT, UP, DOWN, LEFT, RIGHT
int dy[] = {0, -1, 1, 0, 0};
int dx[] = {0, 0, 0, -1, 1};

vector<microbe> map[101][101];
vector<microbe> microbes;

bool comp(microbe a, microbe b){
    return a.size > b.size;
}

int solution(){
    int cnt=0, i, j;
    
    while(cnt != M){
        for(i=0; i<=N; ++i){
            for(j=0; j<=N; ++j){
                map[i][j].clear();
            }
        }
        
        // move
        for(i=0; i<microbes.size(); ++i){
            microbe& cur = microbes[i];
            
            cur.y += dy[cur.dir];
            cur.x += dx[cur.dir];
            // die and turn
            if(cur.y == 0 || cur.x == 0 || cur.y == N-1 || cur.x == N-1){
                cur.size /= 2;
                if(cur.dir < 3){
                    cur.dir = (cur.dir+2)%2 +1;
                }else{
                    cur.dir = (cur.dir+2)%2 +3;
                }
            }
            // just go
            if(cur.size != 0){
                map[cur.y][cur.x].push_back(cur);
            }
        }
        
        // combine
        microbes.clear();
        for(i=0; i<=N; ++i){
            for(j=0; j<=N; ++j){
                if(map[i][j].size() == 0)
                    continue;
                vector<microbe>& m = map[i][j];
                sort(m.begin(), m.end(), comp);
                int new_size = 0;
                for(int k=0; k<m.size(); ++k){
                    new_size += m[k].size;
                }
                microbes.push_back({m[0].y, m[0].x, new_size, m[0].dir});
            }
        }
        ++cnt;
    }
    
    int answer = 0;
    for(i=0; i<microbes.size(); ++i){
        microbe cur = microbes[i];
        answer += cur.size;
    }
    return answer;
}

int main(void){
    int CASES;
    int cnt =0, i;
    microbe temp;
    scanf("%d", &CASES);
    while(CASES != cnt){
        scanf("%d %d %d", &N, &M, &K);
        for(i = 0; i < K; ++i){
            scanf("%d %d %d %d", &temp.y, &temp.x, &temp.size, &temp.dir);
            microbes.push_back(temp);
        }
        printf("#%d %d\n", cnt+1, solution());
        ++cnt;
        microbes.clear();
    }
}

