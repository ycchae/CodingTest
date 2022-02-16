#include <iostream>
#include <vector>

using namespace std;

int N, M;
int rooms[1001] = {0, };
int Answer;

void solution(int cur, int depth){
    if(cur == M){
        if(depth > Answer)
            Answer = depth;
    }else{
        if(rooms[cur] <= M)
            solution(rooms[cur], depth+1);
    }
    
    return;
}

int main(void){
    int n;
    
    freopen("input.txt","r",stdin);
    
    cin >> n;
    while(n-- > 0){
        cin >> N >> M;
        for(int i=1; i<N; i++){
            cin >> rooms[i];
        }
        
        Answer = -1;
        for(int i=1; i<M; i++){
            solution(i, 0);
        }
        cout << Answer << endl;
        
        memset(rooms, 0, sizeof(rooms));
    }
}
