#include <iostream>

using namespace std;
int N, K, P;
int cards[101];

int solution(){
    int card_sum = 0;
    
    for(int i=1; i<=N; i++){
        card_sum += cards[i];
    }
    if(card_sum < K)        // 카드수가 모자라면
        return -1;
    if(K > N * P)   // 매일 줘도 다 못주면
        return -1;
    
    card_sum = 0;
    int day;
    for(day=1; day<=N; day++){
        if(card_sum >= K)
            break;
        if(cards[day] <= P){
            card_sum += cards[day];
        }else{
            card_sum += P;
            if(day+1 <= N)
                cards[day+1] += (cards[day]-P);
        }
    }
    if(card_sum < K)
        return -1;
    
    // for문 마지막 1 추가 되므로 제거해줌
    return --day;
}

int main(void){
    int n;
    freopen("input.txt","r",stdin);
    
    cin >> n;
    while(n-- > 0){
        // buy want limit
        cin >> N >> K >> P;
        memset(cards, 0, sizeof(cards));
        for(int i=1; i<=N; i++){
            cin >> cards[i];
        }
        
        cout << solution() << endl;
    }
}