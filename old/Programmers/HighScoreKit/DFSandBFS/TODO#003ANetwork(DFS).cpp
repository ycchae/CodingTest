#include <string>
#include <vector>

using namespace std;
int visited[200] = {0, };

int dfs(const vector<int> network[], int com, const int n){
    if(network[com].size() == 0){
        visited[com] = 1;
        return 1;
    }
    
    int ret = 0;
    for(int i=0; i<n; i++){
        if(!visited[i]){
            visited[i] = 1;
            for(int i=0; i<network[i].size(); i++)
                dfs(network, i, n)
        }
    }
    return ret;
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<int> network[200];
    for(int i=0; i<n-1; i++){
        for(int j=i+1; j<n; j++){
            if(computers[i][j] == 1)
                network[i].push_back(j);
        }
    }
    answer = dfs(network);
    
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
