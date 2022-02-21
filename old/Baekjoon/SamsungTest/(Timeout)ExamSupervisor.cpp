#define FILE_PATH "/Users/pd3chae/Xcode/test/test1/test1/input.txt"
#include <iostream>
#include <vector>

using namespace std;

long long N, B, C;
vector<long long> A;

long long min_sp;
void binary_search_min(long long n, long long left, long long right){
    if(right - left == 1){
        bool l_can = (n <= (C*left));
        if(l_can)
            min_sp = left;
        else
            min_sp = right;
        return ;
    }
    long long mid = (left + right) / 2;
    bool can = (n <= (C*mid));
    if(can)
        binary_search_min(n, left, mid);
    else
        binary_search_min(n, mid+1, right);
}


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
        min_sp = 1000000;
        binary_search_min(A[i], 1, 1000000-B);
    }
    
    cout << answer << endl;
}
