#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

long long A, B;
int B_depth;
vector<vector<long long>> answers;

bool comp(vector<long long>& a, vector<long long>& b){
    return a.size() > b.size();
}

int cnt_digits(long long n){
    int i;
    for(i=1; i<10; i++){
        if(n/pow(10,i) < 0)
            break;
    }
    return i;
}


void dfs(long long num, vector<long long> converted){
    if(num > B){
        return;
    }
    if(cnt_digits(num) == B_depth){
        if(num == B){
            answers.push_back(converted);
            converted.clear();
        }
    }
    
    converted.push_back(num*2);
    dfs(num*2, converted);
    converted.pop_back();
    
    converted.push_back(num*10 +1);
    dfs(num*10 +1, converted);
    converted.pop_back();
}

int main(void){
    int n, pn=1;
    freopen("input.txt","r",stdin);
    
    cin >> n;
    while(n-- > 0){
        cin >> A >> B;
        B_depth = cnt_digits(B);
        
        vector<long long> first;
        first.push_back(A);
        dfs(A, first);
        
        cout << "# "<< pn++ << ' ';
        if(answers.size() != 0){
            sort(answers.begin(), answers.end(), comp);
            
            cout << answers[0].size() << endl;
            for(auto i = answers[0].begin(); i != answers[0].end(); ++i){
                cout << *i << ' ';
            }
            cout << endl;
            
            answers.clear();
        }
        else{
            cout << -1 << endl;
        }
    }
}
