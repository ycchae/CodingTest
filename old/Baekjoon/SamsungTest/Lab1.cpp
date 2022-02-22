#include <iostream>
#include <vector>

using namespace std;
int N, M, K;

int labs[51][51];
vector<int> room;
int answer;

void dfs(int cur, int depth){
    if(depth == K){
        for(int i=0; i<K; i++)
            cout << room[i] << endl;
        return;
    }
    for(int i=cur; i != N*N; i++){
        int row = i/N;
        int col = i%N;
        if(town[row][col] == 2){    // if room
            int new_cur = row*N+col;
            room.push_back(new_cur);
            dfs(new_cur, depth+1);
            room.pop_back();
        }
    }
}
int main(void){
    int n, pn=1;
    freopen("input.txt","r",stdin);
    
    cin >> n;
    while(n-- > 0){
        cin >> N >> M >> K;
        // 1: fishing 2: room
        memset(town, 0, sizeof(town));
        
        room.clear();
        answer = 0;
        for(int i=0; i != N; ++i){
            for(int j=0; j != N; ++j){
                cin >> town[i][j];
            }
        }
        
        cout << "# "<< pn++ << ' ';
        dfs(0,0);
    }
}
