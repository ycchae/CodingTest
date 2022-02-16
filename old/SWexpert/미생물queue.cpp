#include <iostream>
#include <queue>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct _m{
    int y;
    int x;
    int size;
    int dir;
}microbe;

int N, M, K;
vector<microbe> map[101][101];
queue<microbe> microbes;

// NOT, UP, DOWN, LEFT, RIGHT
int dy[] = {0, -1, 1, 0, 0};
int dx[] = {0, 0, 0, -1, 1};

bool comp(microbe a, microbe b){
    return a.size > b.size;
}

int solution(){
    int cnt=0;
    set<pair<int, int>> pos;
    queue<microbe> empty;
    
    while(cnt != M){
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                map[i][j].clear();
            }
        }
        // move
        while(!microbes.empty()){
            microbe cur = microbes.front();
            microbes.pop();
            
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
                pos.insert(make_pair(cur.y, cur.x));
            }
        }
        
        microbes = empty;
        // combine
        for(set<pair<int, int>>::iterator iter = pos.begin(); iter != pos.end(); ++iter){
            vector<microbe> &m = map[(*iter).first][(*iter).second];
            sort(m.begin(), m.end(), comp);
            int new_size = 0;
            for(int i=0; i<m.size(); ++i){
                new_size += m[i].size;
            }
            microbes.push({m[0].y, m[0].x, new_size, m[0].dir});
        }
        pos.clear();
        
        ++cnt;
    }
    
    int answer = 0;
    while(!microbes.empty()){
        microbe cur = microbes.front();
        microbes.pop();
        answer += cur.size;
    }
    return answer;
}

int main(void){
    int cnt =0;
    int testcase;
    scanf("%d", &testcase);
    while(testcase != cnt){
        scanf("%d %d %d", &N, &M, &K);
        for(int i = 0; i < K; ++i){
            int y, x, size, dir;
            scanf("%d %d %d %d", &y, &x, &size, &dir);
            microbes.push({y, x, size, dir});
        }
        printf("#%d %d\n", cnt+1, solution());
        ++cnt;
    }
}

