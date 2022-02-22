#define FILE_PATH "/Users/pd3chae/Xcode/test/test1/test1/input.txt"
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef struct _pos{
    int y;
    int x;
    
    inline int operator-(struct _pos a){
        return (abs(y-a.y)+abs(x-a.x));
    }
}pos;

int map[50][50];
int N, M;
vector<pos> chicken;
vector<pos> home;

vector<pos> selected;
int answer = 99999999;

void dfs(int cur){
    if(selected.size() == M){
        int city_distance=0;
        for(int i=0; i<home.size(); ++i){
            int chicken_distance=9999999;
            for(int j=0; j<selected.size(); ++j){
                int d = home[i]-selected[j];
                if(chicken_distance > d)
                    chicken_distance = d;
            }
            city_distance += chicken_distance;
        }
        if(answer > city_distance)
            answer = city_distance;
        return;
    }
    for(int i=cur; i<chicken.size(); i++){
        selected.push_back(chicken[i]);
        dfs(i+1);
        selected.pop_back();
    }
    
}
int main(void){
    freopen(FILE_PATH, "r", stdin);
    cin >> N >> M;
    
    for(int i=0; i != N; ++i){
        for(int j=0; j != N; ++j){
            cin >> map[i][j];
            if(map[i][j] == 1){
                home.push_back({i, j});
            }else if(map[i][j] == 2){
                chicken.push_back({i, j});
            }
        }
    }
    
    dfs(0);
    cout << answer << endl;
    return 0;
}
