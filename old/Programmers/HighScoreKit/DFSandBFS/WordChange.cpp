#include <string>
#include <vector>

using namespace std;

vector<string> change_able[50];
void make_adjency_vector(const vector<string> words){
    for(int ch=0; ch<words[0].size(); ch++){
        for(int i=0; i<words.size(); i++){
            string base = words[i];
            base[ch] = '?';
            for(int j=0; j<words.size(); j++){
                string comp = words[j];
                comp[ch] = '?';
                if(base == comp)
                    change_able[i].push_back(words[j]);
            }
        }
    }
}
int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    make_adjency_vector(words);
    
    return answer;
}

int main(void){
    vector<string> words = {"hot", "dot", "dog", "lot", "log", "cog"};
    printf("answer: %d\n", solution("hit", "cog", words));
}
