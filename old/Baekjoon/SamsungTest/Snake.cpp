#include <iostream>
#include <deque>
#include <vector>
#include <cstring>

using namespace std;

typedef struct _pos{
    int y;
    int x;
    inline bool operator==(const struct _pos& a){
        if(a.y == y && a.x == x) return true;
        return false;
    }
}pos;

enum head_dir{U, R, D, L};

vector<pos> apples;
char turns[10001];

int N, K, M;

int solution(){
    pos head_cur = {1,1};
    int answer = 0;
    deque<pos> snake;
    snake.push_front(head_cur);
    
    int head_dir = R;
    bool eat_apple = false;
    
    while(1){
        answer++;
        switch(head_dir){
            case U:
                head_cur.y -= 1;
                break;
            case R:
                head_cur.x += 1;
                break;
            case D:
                head_cur.y += 1;
                break;
            case L:
                head_cur.x -= 1;
                break;
        }
        
        // terminate condition
        if(head_cur.x == N+1 || head_cur.x == 0 || head_cur.y == N+1 || head_cur.y == 0)
            return answer;
        for(auto i = snake.begin(); i != snake.end(); ++i){
            if(head_cur == *i)
                return answer;
        }
        
        for(auto i = apples.begin(); i != apples.end(); ++i){
            if(head_cur == *i){
                eat_apple = true;
                apples.erase(i);
                break;
            }
        }
        
        snake.push_front(head_cur);
        if(eat_apple){
            eat_apple = false;
        }else{
            snake.pop_back();
        }
        
        // 0:U 1:R 2:D 3:L
        if(turns[answer] != 0){
            if(turns[answer] == 'L'){
                head_dir = (head_dir - 1) >= 0 ? (head_dir - 1) % 4 : (4 - head_dir - 1) % 4;
            }else if(turns[answer] == 'D'){
                head_dir = (head_dir + 1) >= 0 ? (head_dir + 1) % 4 : (4 - head_dir + 1) % 4;
            }
        }
    }
    
    return answer;
}

int main(void){
    cin >> N >> K;
    for(int i=0; i<K; i++){
        int y, x;
        cin >> y >> x;
        apples.push_back({y, x});
    }
    
    memset(turns, 0, sizeof(turns));
    cin >> M;
    for(int i=1; i<=M; i++){
        int sec;
        char c;
        cin >> sec >> c;
        turns[sec] = {c};
    }
    
    int answer = solution();
    cout << answer << endl;
}
