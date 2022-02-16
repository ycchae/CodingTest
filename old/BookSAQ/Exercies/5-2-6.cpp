#include <iostream>
#include <queue>
using namespace std;

// N E S W
int dy[] = {-1, 0, 1, 0};
int dx[] = {0, 1, 0, -1};

int N, M;
int s_y, s_x, e_y, e_x;

typedef struct _pos{
    int y;
    int x;
    int cost;
    inline bool operator==(struct _pos a){
        if(a.y == y && a.x == x)
            return true;
        else
            return false;
    }
    
}pos;

int map[1001][1001];
int solution(){
    int answer=-1;
    
    queue<pos> pq;
    pos start={s_y, s_x, 0};
    pos end={e_y, e_x, 0};
    pq.push(start);
    
    while(!pq.empty()){
        pos cur = pq.front();
        pq.pop();
        if(cur == end){
            if(answer == -1 || answer > cur.cost)
                answer = cur.cost;
            continue;
        }
        
        for(int i=0; i<4; i++){
            int new_y = cur.y + dy[i];
            int new_x = cur.x + dx[i];
            int new_cost = cur.cost +1;
            if(new_y >= 0 && new_y < N && new_x >= 0 && new_x < M){
                if(map[new_y][new_x] == 0){
                    map[new_y][new_x] = -1;
                    pos tmp = {new_y, new_x, new_cost};
                    pq.push(tmp);
                }
            }
        }
    }
    
    return answer;
}

int main(void){
    int n;
    
    freopen("input.txt","r",stdin);
    
    cin >> n;
    while(n-- > 0){
        cin >> N >> M;
        cin >> s_y >> s_x >> e_y >> e_x;
        s_y--; s_x--; e_y--; e_x--;
        
        memset(map, -1, sizeof(map));
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                cin >> map[i][j];
            }
        }
        
        int answer = solution();
        
        cout << answer << endl;
    }
}
