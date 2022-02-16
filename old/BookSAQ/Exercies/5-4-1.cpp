#include <iostream>

using namespace std;

int stone[10001];
int score[10001][2];
int N;

// score[i][0]은 현재칸으로 이전칸에서 건너온 케이스 = 여기서는 두칸 뛰어야 함         = 마지막 칸에 한칸 이동해서 도착한 최댓값
// score[i][1]은 현재칸으로 전전칸에서 건너온 케이스 = 여기서는 한칸, 두칸 뛸 수 있음   = 마지막 칸에 두칸 이동해서 도착한 최댓값
void solution(){
    // 초기값: 0번 시작점은 0으로 초기화
    score[0][0] = score[0][1] = 0;
    // 초기값: 1번 돌에 있을 때는 한칸, 두칸 뛰는거 상관 없음 = 두칸 뛰어야 할 경우가 없으므로 score[1][0] 값은 없음
    score[1][1] = stone[1];
    // 2번 돌에 있을 때부터 조건 검사
    for(int i=2; i<=N; i++){
        score[i][0] = score[i-1][1] + stone[i];                         // 현재 칸으로 올 수 있는 한칸 이동한 최대 값을 저장
        score[i][1] = max(score[i-2][0], score[i-2][1]) + stone[i];     // 현재 칸으로 올 수 있는 두칸 이동한 최대 값을 저장
    }
}

int main(void){
    int n;
    
    freopen("input.txt","r",stdin);
    
    cin >> n;
    while(n-- > 0){
        cin >> N;
        memset(stone, 0, sizeof(stone));
        for(int i=1; i<=N; i++){
            cin >> stone[i];
        }
        solution();
        
        int answer=max(score[N][0], score[N][1]);
        
        
        cout << answer << endl;
    }
}
