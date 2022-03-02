#include <iostream>

using namespace std;

int N, M;
int field[101][101];
int fired;
int barrier;

// N E S W
int dy[] = {-1, 0, 1, 0};
int dx[] = {0, 1, 0, -1};
void solution(int y, int x){
    if(field[y][x] == 1 || field[y][x] == 3)
        return ;
    if(field[y][x] == 0 || field[y][x] == 2){
        field[y][x] = 3;
        fired++;
        for(int i=0; i<4; i++){
            int new_y = y+dy[i], new_x = x+dx[i];
            if(new_y >= N || new_y < 0 || new_x >= N || new_x < 0)
                continue;
            solution(y+dy[i], x+dx[i]);
        }
    }
    return;
}

int main(void){
    int n;
    
    freopen("input.txt","r",stdin);
    
    cin >> n;
    while(n-- > 0){
        cin >> N;
        memset(field, -1, sizeof(field));
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                cin >> field[i][j];
            }
        }
        fired = 0;
        barrier = 0;
        
        for(int y=0; y<N; y++){
            for(int x=0; x<N; x++){
                if(field[y][x] == 2){
                    solution(y, x);
                }
                else if(field[y][x] == 1){
                    barrier++;
                }
            }
        }
        
        int answer = N*N - fired - barrier;
        
        cout << answer <<endl;
    }
}
