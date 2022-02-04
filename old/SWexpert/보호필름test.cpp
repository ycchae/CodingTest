// 00:23
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int map[14][21];
int cpmap[14][21];

vector<int> select_line;
vector<int> selectA;
vector<int> selectB;
int D, W, K;
int answer;

void dfs2(int cur, int depth){
    if(answer != INT_MAX)
        return;
    if(selectA.size() == depth){
        cout << "selectA ";
        for(int i=0; i<selectA.size(); ++i){
            printf("%2d", selectA[i]);
        }
        cout << endl;
        
        cout << "selectB ";
        selectB.clear();
        for(int i=0, i2=0; i<select_line.size(); ++i){
            if(i2 < selectA.size() && selectA[i2] == select_line[i]){
                ++i2;
            }else{
                printf("%2d", select_line[i]);
                selectB.push_back(select_line[i]);
            }
        }
        cout << endl;
        int a=0, b=0;
        for(int i=0; i<D; ++i){
            if(a < selectA.size() && selectA[a] == i){
                for(int j=0; j<W; ++j)
                    cpmap[i][j] = 0;
                ++a;
            }else if(b < selectB.size() && selectB[b] == i){
                for(int j=0; j<W; ++j)
                    cpmap[i][j] = 1;
                ++b;
            }else{
                for(int j=0; j<W; ++j)
                    cpmap[i][j] = map[i][j];
            }
            for(int j=0; j<W; ++j)
                printf("%2d", cpmap[i][j]);
            cout << endl;
        }
        cout << endl;
        
        return;
    }
    for(int i=cur; i<select_line.size(); ++i){
        selectA.push_back(select_line[i]);
        dfs2(i+1, depth);
        selectA.pop_back();
    }
}
void dfs(int cur, int depth){
    if(answer != INT_MAX)
        return;
    if(select_line.size() == depth){
        cout << "==== " << "select_line " << depth << " ====" << endl;
        selectA.clear();
        for(int i=0; i<select_line.size(); ++i){
            printf("%2d", select_line[i]);
        }
        cout << endl;
        for(int i=0; i<=depth; ++i)
            dfs2(0, i);
        return;
    }
    for(int i=cur; i<D; ++i){
        select_line.push_back(i);
        dfs(i+1, depth);
        select_line.pop_back();
    }
}
int solution(){
    scanf("%d %d %d", &D, &W, &K);
    if(K == 1) return 0;
    
    for(int i=0; i<D; ++i){
        for(int j=0; j<W; ++j){
            scanf("%d", &map[i][j]);
        }
    }
    
    answer = INT_MAX;
    for(int i=0; i<=K; ++i){
        select_line.clear();
        dfs(0, i);
    }
    return answer;
}

int main(void){
    freopen("/Users/pd3chae/Xcode/test/test2/test2/input.txt", "r", stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int i=1; i<=testcase; ++i){
        printf("#%d %d\n", i, solution());
    }
    return 0;
}

