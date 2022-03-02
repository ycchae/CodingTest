#include <iostream>
#include <vector>

using namespace std;

int N, M;
int rooms[1001] = {0, };
bool visited[1001] = {false, };
vector<int> answers;

void solution(int cur, int depth){
    if(cur == M){
        answers.push_back(depth);
        return;
    }
    if(cur > M){
        answers.push_back(-1);
        return;
    }
    
    if(!visited[cur]){
        visited[cur] = true;
        solution(rooms[cur], depth+1);
        visited[cur] = false;
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
        
        for(int i=1; i<N; i++){
            if(i == M)
                continue;
            solution(i, 0);
        }
        sort(answers.begin(), answers.end());
        cout << *(answers.end()-1) << endl;
        
        memset(rooms, 0, sizeof(rooms));
        memset(visited, false, sizeof(visited));
        answers.clear();
    }
}
/// 단 방향으로만 움직이기 때문에 visited 체크 할 필요 없음!
/// 지나온 길을 다시 돌아가지 않음.