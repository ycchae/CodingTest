#include <string>
#include <vector>
#include <queue>

using namespace std;
int visited[200] = {0, };

int bfs(const vector<int> network[], int start, const int n){
    int ret = 0;
    int com;
    queue<int> q;
    
    while(true){
        q.push(start);
        ret += 1;
        while(!q.empty()){
            com = q.front();
            q.pop();
            if(!visited[com]){
                visited[com] = 1;
                for(int i=0; i<network[com].size(); i++)
                    q.push(network[com][i]);
            }
        }
        
        for(com=0; com<n; com++){
            if(!visited[com]){
                start = com;
                break;
            }
        }
        if(com == n)
            return ret;
    }
    return -1;
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<int> network[200];
    for(int i=0; i<n-1; i++){
        for(int j=i+1; j<n; j++){
            if(computers[i][j] == 1){
                network[i].push_back(j);
                network[j].push_back(i);
            }
        }
    }
    
    answer = bfs(network, 0, n);
    
    return answer;
}

int main(void){
//    printf("answer: %d\n", solution(3, {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}}));
    printf("answer: %d\n",          \
           solution(5,
                    {{1,0,1,1,0},
                    {0,1,0,0,1},
                    {1,0,1,0,0},
                    {1,0,0,1,0},
                    {0,1,0,0,1}}
    ));
    return 0;
}

/*
// for(int i=0; i<n; i++){
//     for(auto j=network[i].begin(); j != network[i].end(); j++)
//         printf("%d", *j);
//     puts("");
// }
 
 for(int i=0; i<n; i++){
     if(!visited[i]){
         visited[i] = 1;
         queue<int> q;
         for(int j=0; j<network[i].size(); i++)
             q.push(network[i][j]);
         bfs(network, q);
         answer++;
     }
 }
*/
