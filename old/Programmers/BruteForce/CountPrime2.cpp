#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <cmath>

using namespace std;

// 7!+6!+5!+4!+3!+2!+1!
int visited[5914] = {0, };
vector<string> digits;
set<int> nums;

bool isPrime(int num){
    if(num == 0 || num == 1)
        return false;
    for (int i=2; i<=sqrt(num); i++)
        if (num % i == 0)
            return false;
    return true;
}


void dfs(int depth, string val){
    if(depth == digits.size()) return;
    nums.insert(atoi(val.c_str()));
    for(int i=0; i<digits.size(); i++){
        if(!visited[i]){
            visited[i] = 1;
            string tmp = val;
            tmp += digits[i];
            dfs(depth+1, tmp);
            visited[i] = 0;
        }
    }
}
int main(void){
    int answer = 0;
    string st = "0011";
    int n = st.size();
    for(int i=0; i != n; i++)
        digits.push_back(st.substr(i,1));
    
    for(int i=0; i != digits.size(); i++){
        visited[i] = 1;
        dfs(0, digits[i]);
        visited[i] = 0;
    }

    for( auto IterPos = nums.begin(); IterPos != nums.end(); ++IterPos ){
        if(isPrime(*IterPos))
            answer++;
        printf("%d ", *IterPos);
    }
    puts("");
    printf("%d\n", answer);

    return answer;
}