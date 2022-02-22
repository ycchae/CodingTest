#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int day;
int mon;
int mon3;
int year;
int usage[12];
int money[12];

int solution(){
    int i;
    for(i=0; i<12; ++i){
        usage[i] = 0;
    }
    scanf("%d %d %d %d", &day, &mon, &mon3, &year);
    for(i=0; i<12; ++i){
        scanf("%d", &usage[i]);
        money[i] = min(day * usage[i], mon);       // 1일권 vs 한달
        if(i >= 1)
            money[i] += money[i-1]; // 한달권or1일권 = 누적 결과
        if(i == 2)
            money[i] = min(money[i], mon3); // 3개월권 vs 누적결과
        if(i >= 3)
            money[i] = min(money[i], money[i-3] + mon3);
    }
    return min(year, money[11]);
}
int main(void){
    int testcase;
    scanf("%d", &testcase);
    for(int i=1; i<=testcase; ++i){
        printf("#%d %d\n", i, solution());
    }
    return 0;
}
