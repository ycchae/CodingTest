#include <iostream>
#include <vector>
#include <string> 

using namespace std;

bool visited[7] = {false, };
void solution(vector<int>& nums, int depth, string val){
    if(depth == nums.size()) {
        cout << val << endl;
        return;
    }
    for(int i=0; i<nums.size(); i++){
        if(!visited[i]){
            visited[i] = true;
            string temp = val + ' '+ (char)(nums[i]+'0');
            solution(nums, depth+1, temp);
            visited[i] = false;
        }
    }
}
int main(void){
    int n, N;
    vector<int> nums;

    cin >> n;
    while(n-- != 0){
        cin >> N;
        for(int i=1; i<=N; i++)
            nums.push_back(i);
        
        solution(nums, 0, "");
        
        nums.clear();
    }
}