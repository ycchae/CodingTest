#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
int T[16], P[16];
int DP[17];

int main(void){
    cin >> N;
    for(int i=1; i != N+1; ++i){
        cin >> T[i];
        cin >> P[i];
    }
    
    DP[0] = 0;
    DP[1] = 0;
    
    int mday = 2;   // money day
    vector<int> money;
    while(mday != N+2){
        for(int i=1; i != mday; ++i){
            if(T[i] + i <= mday){
                money.push_back(P[i] + DP[i]);
            }else{
                money.push_back(0);
            }
        }
        
        sort(money.begin(), money.end());
        DP[mday] = *(money.end()-1);
        mday++;
    }
    cout << DP[N+1] << endl;
        
    return 0;
}
