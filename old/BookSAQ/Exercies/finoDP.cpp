#include <iostream>

using namespace std;

int N;
long long dp[91];

long long fibo(int n){
    if(dp[n] == -1){
        dp[n] = fibo(n-1) + fibo(n-2);
    }
    return dp[n];
}
int main(void){
    memset(dp, -1, sizeof(dp));
    
    dp[1] = 1;
    dp[2] = 1;
    
    cout << fibo(5) << endl;
    int N = 3;
    for(int i=3; i<=N; i++){
        dp[i] = dp[i-1] + dp[i-2];
    }
    cout << dp[N] << endl;
    return 0;
}


