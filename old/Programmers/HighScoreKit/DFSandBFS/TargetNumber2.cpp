#include <string>
#include <vector>

using namespace std;
int answer = 0;
void dfs(const int target, vector<int> numbers, int depth, int val){
    if(depth == numbers.size()){
        if(val == target) answer++;

    }else{

        dfs(target, numbers, depth+1, val+ numbers[depth] * -1);
        
        dfs(target, numbers, depth+1, + numbers[depth] * -1);
    }
}

int solution(vector<int> numbers, int target) {
    dfs(target, numbers, 0, 0);
    return answer;
}

int main(void){
    printf("%d\n", solution({1,1,1,1,1}, 3) );
}