// 00:23
#include <iostream>
#include <vector>
using namespace std;

int map[14][21];
int cpmap[14][21];

vector<int> select_line;
vector<int> selectA;
vector<int> selectB;
int D, W, K;
int answer;


int check(){
    int a_size = (int)selectA.size();
    int line_size = (int)select_line.size();
    
    // 약품 칠할 전체 줄 종류에서 A약품 사용할 라인까지 나눠줬으므로
    // B 약품 칠할 라인을 구할 수 있음
    selectB.clear();
    for(int i=0, i2=0; i<line_size; ++i){
        if(i2 < a_size && selectA[i2] == select_line[i]){
            ++i2;
        }else{
            selectB.push_back(select_line[i]);
        }
    }
    int b_size = (int)selectB.size();
    
    // 각 라인에 맞게 약품 칠하기
    int a=0, b=0;
    for(int i=0; i<D; ++i){
        if(a < a_size && selectA[a] == i){
            for(int j=0; j<W; ++j)
                cpmap[i][j] = 0;
            ++a;
        }else if(b < b_size && selectB[b] == i){
            for(int j=0; j<W; ++j)
                cpmap[i][j] = 1;
            ++b;
        }else{
            for(int j=0; j<W; ++j)
                cpmap[i][j] = map[i][j];
        }
    }
    
    // 검사하기
    for(int i = 0; i < W; i++){
        int cnt = 1;
        for(int j = 0; j < D-1; j++){
            if(cnt >= K)
                break;
            if(D-K+1 == j && cnt == 1)
                break;
            
            if(cpmap[j][i] == cpmap[j+1][i])
                ++cnt;
            else
                cnt = 1;
            
        }
        if(cnt < K){
            return INT_MAX;     // 조건 미달 이면 다름 열 검사 없이 return
        }
    }
    return line_size;       // 조건 만족하면 약품 칠한 라인 수 return
}

// A약품 사용할 라인 종류 나누기.
void dfs2(int cur, int depth){
    if(answer != 15)
        return;
    if(selectA.size() == depth){
        int ret = check();
        if(ret != INT_MAX)
            answer = check();
        return;
    }
    for(int i=cur; i<select_line.size(); ++i){
        selectA.push_back(select_line[i]);
        dfs2(i+1, depth);
        selectA.pop_back();
    }
}

// 약품 칠 라인 종류 정하기. 0개에서 최대 K개 까지
void dfs(int cur, int depth){
    if(answer != 15)
        return;
    // depth가 0~K 까지 라서 그 수 만큼의 line이 선택됐으면 dfs2실행
    if(select_line.size() == depth){
        selectA.clear();
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
    
    answer = 15;
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

