#include <iostream>
#include <list>
#include <queue>
#include <cmath>
#include <string>

typedef struct _cmd{
    int num;
    int dir;
}cmd;

using namespace std;

int K;
list<int> wheel[5];
queue<cmd> cmds;

void turn(int n, int dir){
    int p;
    switch(dir){
        case 1:     // clockwise
            p = *(--wheel[n].end());
            wheel[n].erase(--wheel[n].end());
            wheel[n].insert(wheel[n].begin(), p);
            break;
        case -1:     // counter clockwise
            p = *(wheel[n].begin());
            wheel[n].erase(wheel[n].begin());
            wheel[n].insert(wheel[n].end(), p);
            break;
    }
}
int solution(){
    cmd c;
    queue<cmd> loop;
    bool avail[4];
    bool done[5];
    
    while(!cmds.empty()){
        for(int i=1; i!=5; ++i)
            done[i] = false;
        
        c = cmds.front();
        cmds.pop();
        
        int n = c.num;
        for(int i=1; i!=5-1; ++i){
            list<int>::iterator left = wheel[i].begin();
            ++left; ++left;
            list<int>::iterator right = wheel[i+1].end();
            --right; --right;
            
            if(*left != *right){
                avail[i] = true;
            }else{
                avail[i] = false;
            }
        }
        loop.push({n, c.dir});
        while(!loop.empty()){
            cmd lc = loop.front();
            loop.pop();
            turn(lc.num, lc.dir);
            done[lc.num] = true;
            if(lc.num-1 > 0 && avail[lc.num-1] && !done[lc.num-1])
                loop.push({lc.num-1, lc.dir*-1});
            if(lc.num+1 < 5 && avail[lc.num] && !done[lc.num+1])
                loop.push({lc.num+1, lc.dir*-1});
        }
    }
    
    
    int answer =0;
    for(int i=1; i!=5; ++i)
        answer = answer + pow(2,i-1)*(*(wheel[i].begin()));
    
    return answer;
}

int main(void){
    string line;
    for(int i=1; i<5; ++i){
        cin >> line;
        for(int j=0; j!=8; ++j){
            wheel[i].push_back(line[j]-'0');
        }
    }
    
    cin >> K;
    for(int i=0; i!=K; ++i){
        int n, d;
        cin >> n >> d;
        cmds.push({n, d});
    }
    
    cout << solution() << endl;
}
