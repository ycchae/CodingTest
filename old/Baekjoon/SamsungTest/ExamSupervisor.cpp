#define FILE_PATH "/Users/pd3chae/Xcode/test/test1/test1/input.txt"
#include <iostream>
#include <vector>

using namespace std;

long long N, B, C;
vector<long long> A;

int main(void){
    long long answer = 0;
    
    freopen(FILE_PATH, "r", stdin);
    
    cin >> N;
    for(long long i=0; i != N; ++i){
        long long p;
        cin >> p;
        A.push_back(p);
    }
    cin >> B >> C;
    
    for(long long i=0; i != N; ++i){
        A[i] -= B;
        answer++;
        if(A[i] < 1)
            continue;

        if(A[i] % C == 0)
            answer += (A[i] / C);
        else
            answer += (A[i] / C + 1);
    }
    
    cout << answer << endl;
    return 0;
}
