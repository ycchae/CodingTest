#include <iostream>
#include <deque>
#include <vector>
#include <climits>
#include <cstring>

using namespace std;

int N;
deque<int> nums;
int plus, minus, multi, devide;
int asw_min = INT_MAX, asw_max = INT_MAX * -1;
vector<int> operators;
bool visited[11];

void dfs(int depth, vector<int> val){
    if(depth == N-1){
        deque<int> cp_nums(nums);
        
        for(int i=0; i<N-1; ++i){
            int num1 = cp_nums.front(); cp_nums.pop_front();
            int num2 = cp_nums.front(); cp_nums.pop_front();
            switch(val[i]){
                case 0:
                    cp_nums.push_front(num1+num2);
//                    cout << "+" << num1+num2 << endl;
                    break;
                case 1:
                    cp_nums.push_front(num1-num2);
//                    cout << "-" << num1-num2 << endl;
                    break;
                case 2:
                    cp_nums.push_front(num1*num2);
//                    cout << "*" << num1*num2 << endl;
                    break;
                case 3:
                    cp_nums.push_front(num1/num2);
//                    cout << "/" << num1/num2 << endl;
                    break;
            }
        }
        
        if(asw_max < cp_nums.front())
            asw_max = cp_nums.front();
        
        if(asw_min > cp_nums.front())
            asw_min = cp_nums.front();
        
        return;
    }
    
    for(int i=0; i<N-1; ++i){
        if(!visited[i]){
            visited[i] = true;
            val.push_back(operators[i]);
            dfs(depth+1, val);
            val.pop_back();
            visited[i] = false;
        }
    }
}
int main(void){
    cin >> N;
    for(int i=0; i<N; ++i){
        int t;
        cin >> t;
        nums.push_back(t);
    }
    
    
    for(int i=0; i<4; ++i){
        int t;
        cin >> t;
        for(int j=0; j<t; ++j){
            operators.push_back(i);
        }
    }
    memset(visited, false, sizeof(visited));
    
    vector<int> val;
    dfs(0, val);
    
    cout << asw_max << endl << asw_min << endl;
}
