#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

typedef struct _shark{
    int y;
    int x;
    int speed;
    int dir;
    int size;
    
    inline bool operator==(struct _shark a){
        if(a.x == x && a.y == y)
            return true;
        return false;
    }
}shark;

vector<shark> sharks;

int R, C, M;
// Up, Down, Right, Left
int dy[] = {-1, 1, 0, 0};
int dx[] = {0, 0, 1, -1};

void move_sharks(){
    for(auto i = sharks.begin(); i != sharks.end(); ++i){
        
        if((*i).dir < 2){
            int move = (*i).speed % (2 * (R - 1)); 
            while(move > 0){
                int new_y = (*i).y + dy[(*i).dir] * move;
                if(new_y < 0){
                    move -= (*i).y;
                    (*i).y = 0;
                    (*i).dir = ((*i).dir+1)%2;
                }else if(new_y >= R){
                    move -= (R-1)-(*i).y;
                    (*i).y = R-1;
                    (*i).dir = ((*i).dir+1)%2;
                }else{
                    move -= abs(new_y-(*i).y);
                    (*i).y = new_y;
                }
                
            }
            
        }else{
            int move = (*i).speed % (2 * (C - 1)); 
            while(move > 0){
                int new_x = (*i).x + dx[(*i).dir] * move;
                if(new_x < 0){
                    move -= (*i).x;
                    (*i).x = 0;
                    (*i).dir = ((*i).dir+1)%2 +2;
                }else if(new_x >= C){
                    move -= (C-1)-(*i).x;
                    (*i).x = C-1;
                    (*i).dir = ((*i).dir+1)%2 +2;
                }else{
                    move -= abs(new_x-(*i).x);
                    (*i).x = new_x;
                }
            }
        }
    }
}
void eat_sharks(){
    shark map[100][100];
    shark empty = {0,0,0,0,0};
    set<pair<int, int>> s;
    
    for(int i=0; i<R; ++i){
        for(int j=0; j<C; ++j){
            map[i][j] = empty;
        }
    }
    for(auto i = sharks.begin(); i != sharks.end(); ++i){
        s.insert(make_pair((*i).y, (*i).x));
        if(map[(*i).y][(*i).x] == empty){
            map[(*i).y][(*i).x] = (*i);
        }else{
            if(map[(*i).y][(*i).x].size < (*i).size){
                map[(*i).y][(*i).x] = (*i);
            }
        }
    }
    sharks.clear();
    for(auto i = s.begin(); i != s.end(); ++i){
        sharks.push_back(map[(*i).first][(*i).second]);
    }
}
int solution(){
    int answer = 0;
    for(int man=0; man<C; ++man){
        if(sharks.size()==0)
            break;
        // catch
        for(auto i = sharks.begin(); i != sharks.end(); ++i){
            if(man == (*i).x){
                answer += (*i).size;
                sharks.erase(i);
                break;
            }
        }
        // move
        move_sharks();
        // eat
        eat_sharks();
    }
    return answer;
}
int main(void){    
    cin >> R >> C >> M;
    for(int i=0; i<M; ++i){
        int r, c, s, d, z;
        cin >> r >> c >> s >> d >> z;
        
        sharks.push_back({--r,--c,s,--d,z});
    }
    cout << solution() << endl;
}
