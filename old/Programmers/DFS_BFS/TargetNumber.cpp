#include <string>
#include <vector>

using namespace std;
int answer = 0;
void dfs(const int target, vector<int> numbers, int depth){
    if(depth == numbers.size()){
        
        puts("");
        int sum = 0;
        for(int i=0; i<numbers.size(); i++)
            sum += numbers[i];
        if(sum == target)
            answer++;
        return;
    }else{
        numbers[depth] *= -1;
        dfs(target, numbers, depth+1);
        numbers[depth] *= -1;
        dfs(target, numbers, depth+1);
    }
}

int solution(vector<int> numbers, int target) {
    dfs(target, numbers, 0);
    return answer;
}

int main(void){
    printf("%d\n", solution({1,1,1,1,1}, 3) );
}