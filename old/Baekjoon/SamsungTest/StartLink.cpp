#include <iostream>
#include <vector>
#include <cmath>
#include <cstring>
#include <climits>

using namespace std;

int N;
int s[20][20];
int pairs[400];
bool visited[20];

vector<int> team1;
int answer = INT_MAX;

void dfs(int p, int depth){
    if(depth == N/2){
        vector<int> team2;
        for(int i=0; i<N; i++){
            if(!visited[i])
                team2.push_back(i);
        }
        int point1 = 0;
        for(int i=0; i<team1.size(); ++i){
            for(int j=i+1; j<team1.size(); ++j){
                point1 += pairs[team1[i]*N + team1[j]];
            }
        }
        
        int point2 = 0;
        for(int i=0; i<team2.size(); ++i){
            for(int j=i+1; j<team2.size(); ++j){
                point2 += pairs[team2[i]*N + team2[j]];
            }
        }
        int diff = abs(point1 - point2);
        if(answer > diff)
            answer = diff;
        
        return ;
    }
                
    for(int i=p; i<N; i++){
        if(!visited[i]){
            visited[i] = true;
            team1.push_back(i);
            
            dfs(i, depth+1);
            
            visited[i] = false;
            team1.pop_back();
        }
    }
}
int main(void){
    freopen("StartLink.txt","r",stdin);
    
    cin >> N;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin >> s[i][j];
        }
    }
    memset(pairs, 0, sizeof(pairs));
    memset(visited, false, sizeof(visited));
    int p_idx=0;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++)
            pairs[p_idx++] = s[i][j] + s[j][i];
    }
    
    dfs(0, 0);
    
    cout << answer << endl;
    
    return 0;
}

