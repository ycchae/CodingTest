#include <iostream>
#include <vector>

using namespace std;

int N, M;
bool visited[11] = {false, };
int mat[11][11] = {0, };
int answer;

void solution(int cur, int depth, int cost){
    if(depth == N && mat[cur][M-1] != 0){
        if(answer == -1 || answer > cost+mat[cur][M-1])
            answer = cost+mat[cur][M-1];
        return;
    }
    
    
    for(int i=0; i<N; i++){
        if(!visited[i] && mat[cur][i] != 0){
            int new_cost = mat[cur][i] + cost;
            if(answer == -1 || answer > new_cost){
                visited[i] = true;
                solution(i, depth+1, new_cost);
                visited[i] = false;
            }
        }
    }
    
    
    return;
}

int main(void){
    int n;
    
    freopen("input.txt","r",stdin);
    
    cin >> n;
    while(n-- > 0){
        cin >> N >> M;
        
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                cin >> mat[i][j];
            }
        }
        answer=-1;
        visited[M-1] = true;
        solution(M-1, 1, 0);
        
        cout << answer <<endl;
        
        memset(mat, 0, sizeof(mat));
        memset(visited, false, sizeof(visited));
    }
}
