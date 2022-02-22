#include <vector>
#include <algorithm>

using namespace std;

struct stu{
    int num;
    int score;
    
};
typedef struct stu student;
bool score_compare (const struct stu &a, const struct stu &b){
        return a.score > b.score;
}

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<student> students;
    for(int i=1; i != 4; i++){
        student student = {i ,0};
        students.push_back(student);
    }
    
    int ans1[5] = {1,2,3,4,5};
    int ans2[8] = {2,1,2,3,2,4,2,5}
    int ans3[10] = {3,3,1,1,2,2,4,4,5,5};
    
    for(int i=0; i<answers.size(); i++){
        // 1
        if(answers[i] ==  ans1[i%5])
            students[0].score++;
        // 2
         if(answers[i] ==  ans2[i%8])
            students[1].score++;
        // 3
        if(answers[i] == ans3[i%10])
            students[2].score++;
    }
    sort(students.begin(), students.end(), score_compare);
    
    for(int i=0; i<3; i++){
        if(students[0].score == students[i].score)
            answer.push_back(students[i].num);
    }
    sort(answer.begin(), answer.end());
    
    return answer;
}

int main(void){
    // vector<int> a;
    // solution(a);
    int ans1[5] = {1,2,3,4,5};
    int ans3[10] = {3,3,1,1,2,2,4,4,5,5};
    
    for(int i=0; i<23; i++){
        // printf("1: %d\n", ans1[i%5]);
        if(i%2 == 0)
            printf("%d: %d\n",i,  2);
        else if( i%2 == 1)
            printf("%d: %d\n",i, ans1[(i/2)%5]);
        // printf("%d: %d\n", i, ans3[i%10]);
    }
}