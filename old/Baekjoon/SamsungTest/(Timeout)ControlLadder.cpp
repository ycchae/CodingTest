#define FILE_PATH "/Users/pd3chae/Xcode/test/test1/test1/input.txt"
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct _bridge{
    int h;
    bool right;
    
    inline bool operator==(int height){
        if(h == height)
            return true;
        return false;
    }
}bridge;

vector<bridge> bridges[11];
int N, H;
int answer = 5;

bool check(){
    for(int n=1; n <= N; ++n){
        int cur = n;
        for(int h=1; h <= H; ++h){
            vector<bridge>::iterator iter = find(bridges[cur].begin(), bridges[cur].end(), h);
            if(iter != bridges[cur].end()){
                if((*iter).right)
                    ++cur;
                else
                    --cur;
            }
        }
        if(cur != n)
            return false;
    }
    return true;
}
void dfs(int c, int cnt){
    if(cnt > 3)
        return;
    
    if(check()){
        if(answer > cnt)
            answer = cnt;
    }
    
    for(int n=1; n < N; ++n){
        for(int h=c; h <= H; ++h){
            if(find(bridges[n].begin(), bridges[n].end(), h) == bridges[n].end()){
                if(find(bridges[n+1].begin(), bridges[n+1].end(), h) == bridges[n+1].end()){
                    bridges[n].push_back({h, true});
                    bridges[n+1].push_back({h, false});
                    dfs(h, cnt+1);
                    bridges[n].pop_back();
                    bridges[n+1].pop_back();
                }
            }
        }
    }
    
}

int main(void){
    int M;
    
    freopen(FILE_PATH, "r", stdin);

    cin >> N >> M >> H;
    
    for(int i=0; i!=M; ++i){
        int n, h;
        cin >> h >> n;
        
        bridges[n].push_back({h, true});
        bridges[n+1].push_back({h, false});
    }
    
    dfs(1, 0);
    if(answer != 5)
        cout << answer << endl;
    else
        cout << -1 << endl;
    
    return 0;
}
