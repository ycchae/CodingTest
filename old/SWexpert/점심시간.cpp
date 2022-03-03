#include <iostream>
#include <queue>
#include <vector>
#include <climits>
#include <cmath>
#include <algorithm>

using namespace std;

typedef struct _pos{
    int y;
    int x;
    inline bool operator==(struct _pos a){
        return (y == a.y && x == a.x);
    }
    inline int operator-(struct _pos a){
        return (abs(a.y-y) + abs(a.x-x));
    }
}position;

typedef struct _pers{
    position pos;
    int distance[2];
    int stair;
    inline bool operator==(struct _pers a){
        return (pos == a.pos && distance[0] == a.distance[0] && distance[1] == a.distance[1]);
    }
}person;

typedef struct _st{
    position pos;
    int length;
}stair;

stair stairs[2];
vector<person> people;
int map_size;

int selects[11];
vector<person> walking[2];
int results[11];

int answer;

bool comp1(person a, person b){
    return a.distance[0] < b.distance[0];
}
bool comp2(person a, person b){
    return a.distance[1] < b.distance[1];
}

queue<person> que;

int lunch(){
    int walk_size=0, i, s, result=0;
    walking[0].clear(); walking[1].clear();
    for (i = 0; i < people.size(); ++i) {
        if (selects[i] == 0) {
            walking[0].push_back(people[i]);
        }
        else {
            walking[1].push_back(people[i]);
        }
    }
    sort(walking[0].begin(), walking[0].end(), comp1);
    sort(walking[1].begin(), walking[1].end(), comp2);
    
    for(s = 0; s < 2; ++s){
        
        for(i=0; i<11; ++i)
            results[i] = 0;
        
        walk_size = (int)walking[s].size();
        if(walk_size == 0)
            continue;
        
        // less than 3 people
        if(walk_size < 4){
            result = max(result, walking[s][walk_size-1].distance[s] +1 +stairs[s].length);
            continue;
        }
        
        for(i=0; i<walk_size; ++i){
            if(i < 3){
                results[i] = walking[s][i].distance[s] + 1 +stairs[s].length;
            }else{
                if(walking[s][i].distance[s] < results[i-3]){
                    int wait_time = results[i-3] - walking[s][i].distance[s];
                    results[i] =  walking[s][i].distance[s] + wait_time + stairs[s].length;
                }else{
                    results[i] = walking[s][i].distance[s] + 1 + stairs[s].length;
                }
            }
        }
        result = max(result, results[walk_size-1]);
        continue;
        
    }
    return result;
    
}
void dfs(int cur){
    if(cur == people.size()){
        answer = min(answer, lunch());
        return;
    }
    for(int i=0; i<2; ++i){
        selects[cur] = i;
        dfs(cur+1);
    }
}
void solution(){
    int i, j;
    person p;
    stair s;
    int sidx = 0;
    int val;
    
    scanf("%d", &map_size);
    for(i=0; i<map_size; ++i){
        for(j=0; j<map_size; ++j){
            scanf("%d", &val);
            if(val == 1){
                p.pos.y = i; p.pos.x = j; p.stair = 0;
                people.push_back(p);
            }else if(val > 1){
                s.pos.y = i; s.pos.x = j; s.length = val;
                stairs[sidx] = s;
                ++sidx;
            }
        }
    }
    for(int i=0; i<people.size(); ++i){
        for(int j=0; j<2; ++j){
            people[i].distance[j] = stairs[j].pos - people[i].pos;
        }
    }
    dfs(0);
    
}

int main(void){
    int testcase;
    scanf("%d", &testcase);
    
    for(int i=1; i<=testcase; ++i){
        people.clear();
        answer = INT_MAX;
        solution();
        printf("#%d gi%d\n", i, answer);
    }
}
