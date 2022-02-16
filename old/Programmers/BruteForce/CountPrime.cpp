#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <algorithm>

using namespace std;

set<int> nums;

bool isPrime(int num){
    if(num == 0 || num == 1)
        return false;
    for (int i=2; i<=sqrt(num); i++)
        if (num % i == 0)
            return false;
    return true;
}
void digit_permutation(vector<int>& digits){
    do{
            int n = 0;
            for(int j=0; j<digits.size(); j++)
                n += digits[j] * pow(10, j);
            nums.insert(n);
        }while(next_permutation(digits.begin(),digits.end()));
}

void findNums(string numbers, vector<int> digits){
    if(numbers.size() == 0) return;
    for(int i=0; i<numbers.size(); i++){
        digits.push_back(numbers[i] - '0');
        digit_permutation(digits);
        findNums(numbers.substr(i+1), digits);
        digits.erase(digits.end()-1);
    }
}

int solution(string numbers) {
    int answer = 0;
    vector<int> digits;
    findNums(numbers, digits);
    
    for( auto IterPos = nums.begin(); IterPos != nums.end(); ++IterPos ){
        if(isPrime(*IterPos))
            answer++;
    }
    
    return answer;
}

int main(void){
    printf("\nanw: %d\n", solution("17"));
}
