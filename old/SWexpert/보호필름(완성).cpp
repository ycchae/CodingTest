#include <iostream>
#include <algorithm>

using namespace std;

int D, W, K;//두께, 가로길이, 함격기준

int result;
int min_cnt;
int visited[15];
int film[14][21];

//약품을 투여하는 모든경우를 고려한다 ->
void check(int ans) {
   for(int i = 0; i < W; i++){
       int cnt = 1;
       for(int j = 0; j < D-1; j++){
           if(cnt >= K)
               break;
           if(D-K+1 == j && cnt == 1)
               break;
           
           if(film[j][i] == film[j+1][i])
               ++cnt;
           else
               cnt = 1;
           
       }
       if(cnt < K){
           return ;     // 조건 미달 이면 다름 열 검사 없이 return
       }
   }
    result = min(result, ans);
   return ;       // 조건 만족하면 약품 칠한 라인 수 return
}


void dfs(int d, int cnt) {
    int temp[21];
   if (cnt >= result)
      return;
   
   if (d >= D) {//종료조건
       check(cnt);
       return;
   }

    dfs(d+1, cnt);
        
    for (int i = 0; i < W; i++) {//원본복사해놓기
        temp[i] = film[d][i];
    }
    
    for (int c = 0; c < W; c++) {
        film[d][c] = 0;
    }
    dfs(d+1, cnt + 1);
    
    for (int c = 0; c < W; c++) {
        film[d][c] = 1;
    }
    dfs(d+1, cnt + 1);
    
    for (int i = 0; i < W; i++) {//되돌리기
        film[d][i] = temp[i];
    }

}

void Testcase() {
   
   scanf("%d %d %d", &D, &W, &K);
   for (int i = 0; i < D; i++) {
      for (int j = 0; j < W; j++) {
         scanf("%d", &film[i][j]);
      }
   }

   dfs(0, 0);
}

int main() {
   int testcase;
   scanf("%d", &testcase);
   for (int i = 1; i <= testcase; i++) {
      result = 15;
      Testcase();
      printf("#%d %d\n", i, result);
   }
}
