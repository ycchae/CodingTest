#include <iostream>

using namespace std;
int N, M;
int maze[3001][3001];
int dp[3001][3001];

void solution(){
    dp[0][0] = maze[0][0];
    for(int i=1; i<N; i++){
        dp[i][0] = dp[i-1][0] + maze[i][0];
    }
    for(int i=1; i<M; i++){
        dp[0][i] = dp[0][i-1] + maze[0][i];
    }
    
    for(int y=1; y<N; y++){
        for(int x=1; x<M; x++){
            dp[y][x] = max(dp[y-1][x], dp[y][x-1]) + maze[y][x];
        }
    }
}

int main(void){
    int n;
    
    freopen("input.txt","r",stdin);
    
    cin >> n;
    while(n-- > 0){
        cin >> N >> M;
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++)
                cin >> maze[i][j];
        }
        solution();
//        for(int i=0; i<N; i++){
//            for(int j=0; j<M; j++){
//                cout << dp[i][j] << ' ';
//            }
//            cout << endl;
//        }
//        cout << endl;
        cout << dp[N-1][M-1] << endl;
    }
    
    
}
