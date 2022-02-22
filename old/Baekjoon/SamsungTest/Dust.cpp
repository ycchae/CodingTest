#include <iostream>
#include <queue>

typedef struct _pos{
    int r;
    int c;
    int amt;
}pos;

using namespace std;

int R, C, T;
int map[50][50];
int machine[2];

enum dir{N, E, S, W};
// N, E, S, W
int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, 1, 0, -1};
queue<pos> dust;

void machine0();
void machine1();

int solution(){
    int answer = 0, t=0;
    int copy_map[50][50];
    pos cur;
    
    
    while(T != t){
        for(int i=0; i!=R; ++i){
            for(int j=0; j!=C; ++j){
                copy_map[i][j] = map[i][j];
                if(map[i][j] >= 1){
                    dust.push({i, j, map[i][j]});
                }
            }
        }
        
        // diffusion
        while(!dust.empty()){
            cur = dust.front();
            dust.pop();
            int new_r=0, new_c=0, new_amt=0;
            for(int i=0; i!=4; ++i){
                new_r = cur.r + dr[i];
                new_c = cur.c + dc[i];
                if(new_r < 0 || new_r >= R || new_c < 0 || new_c >= C)
                    continue;
                if(map[new_r][new_c] == -1)
                    continue;
                new_amt = cur.amt/5;
                if(new_amt < 0)
                    continue;
                map[cur.r][cur.c] -= new_amt;
                map[new_r][new_c] += new_amt;
            }
        }

        // wind
        machine0();
        machine1();
        ++t;
    }
    for(int i=0; i!=R; ++i){
        for(int j=0; j!=C; ++j){
            answer += map[i][j];
        }
    }
    answer += 2;
    return answer;
}

int main(void){
    machine[0] = machine[1] = 0;
    cin >> R >> C >> T;
    
    for(int i=0; i != R; ++i){
        for(int j=0; j!=C; ++j){
            cin >> map[i][j];
            if(map[i][j] == -1 && machine[0] == 0){
                machine[0] = i;
                machine[1] = i+1;
            }
        }
    }
    
    cout << solution() << endl;
    
    return 0;
}


void machine0(){
    queue<int> wind;
    int m_r;    // machien r
    m_r = machine[0];
    
    // right
    for(int j=1; j < C-1; ++j){
        wind.push(map[m_r][j]);
    }
    map[m_r][1] = 0;
    for(int j=2; j < C-1; ++j){
        map[m_r][j] = wind.front();
        wind.pop();
    }

    // up
    for(int i=m_r; i > 0; --i){
        wind.push(map[i][C-1]);
    }
    for(int i=m_r; i > 0; --i){
        map[i][C-1] = wind.front();
        wind.pop();
    }
    
    // left
    for(int j=C-1; j > 0; --j){
        wind.push(map[0][j]);
    }
    for(int j=C-1; j > 0; --j){
        map[0][j] = wind.front();
        wind.pop();
    }

    // down
    for(int i=0; i < m_r; ++i){
        wind.push(map[i][0]);
    }
    for(int i=0; i < m_r; ++i){
        map[i][0] = wind.front();
        wind.pop();
    }

}


void machine1(){
    queue<int> wind;
    int m_r;    // machien r
    m_r = machine[1];
    
    // right
    for(int j=1; j < C-1; ++j){
        wind.push(map[m_r][j]);
    }
    map[m_r][1] = 0;
    for(int j=2; j < C-1; ++j){
        map[m_r][j] = wind.front();
        wind.pop();
    }
    
    // down
    for(int i=m_r; i < R-1; ++i){
       wind.push(map[i][C-1]);
    }
    for(int i=m_r; i < R-1; ++i){
       map[i][C-1] = wind.front();
       wind.pop();
    }

    // left
    for(int j=C-1; j > 0; --j){
        wind.push(map[R-1][j]);
    }
    for(int j=C-1; j > 0; --j){
        map[R-1][j] = wind.front();
        wind.pop();
    }
    // up
    for(int i=R-1; i > m_r; --i){
        wind.push(map[i][0]);
    }
    for(int i=R-1; i > m_r; --i){
        map[i][0] = wind.front();
        wind.pop();
    }
    
}
