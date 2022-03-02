#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct _f{
    int y;
    int x;
    int distance;
}fish;

int N;
int map[21][21];
int visited[21][21];

// N W S E
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, -1, 0, 1};

fish shark;
int shark_size;

bool comp(const fish &a, const fish &b){
    if(a.distance == b.distance){  // same distance
        if(a.y == b.y)
            return a.x < b.x;
        else
            return a.y < b.y;
    }else if(a.distance < b.distance)
        return a.distance < b.distance;
    else
        return b.distance > a.distance;
}

int solution(){
    int answer = 1;
    queue<fish> que;
    vector<fish> can_eat;
    int eaten = 0;
    int new_y, new_x, i;
    
    while(1){
        que.push(shark);
        
        while(!que.empty()){
            fish cur = que.front();
            visited[cur.y][cur.x] = answer;
            que.pop();
            
            for(i=0; i<4; i++){
                new_y = cur.y + dy[i];
                new_x = cur.x + dx[i];
                if(new_y < 0 || new_y >= N || new_x < 0 || new_x >= N)
                    continue;
                if(map[new_y][new_x] > shark_size)
                    continue;
                if(visited[new_y][new_x] == answer)
                    continue;
                if(map[new_y][new_x] < shark_size && map[new_y][new_x] > 0){
                    visited[new_y][new_x] = answer;
                    can_eat.push_back({new_y, new_x, cur.distance+1});
                }else{  // same size or 0
                    if(can_eat.size() == 0){
                        visited[new_y][new_x] = answer;
                        que.push({new_y, new_x, cur.distance+1});
                    }
                }
            }
        }
        if(can_eat.size() == 0)
            return answer-1;
        sort(can_eat.begin(), can_eat.end(), comp);
        shark.y = can_eat[0].y;
        shark.x = can_eat[0].x;
        if(shark_size < 7){
            ++eaten;
            if(eaten == shark_size){
                ++shark_size;
                eaten = 0;
            }
        }
        answer += can_eat[0].distance;
        map[shark.y][shark.x] = 0;
        can_eat.clear();
    }
}

int main(void){
    cin >> N;
    
    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            cin >> map[i][j];
            if(map[i][j] == 9){
                shark.y = i; shark.x = j; shark.distance=0;
                map[i][j] = 0;
            }
        }
    }
    shark_size = 2;
    cout << solution() << endl;
}
