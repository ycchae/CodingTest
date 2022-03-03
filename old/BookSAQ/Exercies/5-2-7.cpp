#include <iostream>
#include <queue>

using namespace std;

typedef struct _move{
    int room;
    int cost;
}moves;

int visited[50001];
int S, E;

int solution(){
    int answer=-1;
    
    queue<moves> q;
    moves start = {S, 0};
    q.push(start);
    
    visited[S] = true;
    
    while(!q.empty()){
        moves cur = q.front();
        q.pop();
        
        if(cur.room == E){
            if(answer == -1 || answer > cur.cost)
                answer = cur.cost;
            break;
        }
        
        int new_room = -1;
        int new_cost = cur.cost +1;
        for(int i=0; i<3; i++){
            if(i == 0)
                new_room = cur.room -1;
            else if(i == 1)
                new_room = cur.room +1;
            else if(i == 2){
                new_room = cur.room *2;
            }
            
            if(new_room > 0 && new_room <= 50000){
                if(!visited[new_room]){
                    visited[new_room] = true;
                    moves tmp = {new_room, new_cost};
                    q.push(tmp);
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
        cin >> S >> E;
        
        int answer = solution();
        
        cout << answer << endl;
        memset(visited, false, sizeof(visited));
    }
}
