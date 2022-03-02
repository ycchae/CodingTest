#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef struct _diff{
    int idx;
    int dif;
}diff;

int N, M;
int today[100001];
int tomorrow[100001];

bool comp(diff& a, diff& b){
    return a.dif < b.dif;
}

int solution(){
    int answer = 0;
    vector<diff> v;
    
    for(int i=0; i<N+M; i++){
        diff tmp = {i, today[i]-tomorrow[i]};
        v.push_back(tmp);
    }
    sort(v.begin(), v.end(), comp);
    
    for(int i=0; i<N; i++){
        int idx = v[i].idx;
        answer += today[idx];
    }
    for(int i=N; i<N+M; i++){
        int idx = v[i].idx;
        answer += tomorrow[idx];
    }
    
    return answer;
}

int main(void){
    int n;
    freopen("input.txt","r",stdin);
    
    cin >> n;
    while(n-- > 0){
        // today tommorow
        cin >> N >> M;
        memset(today, 0, sizeof(today));
        memset(tomorrow, 0, sizeof(tomorrow));
        
        for(int i=0; i<N+M; i++){
            cin >> today[i];
        }
        for(int i=0; i<N+M; i++){
            cin >> tomorrow[i];
        }
        
        cout << solution() << endl;
    }
}
