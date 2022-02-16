#include <iostream>
#include <vector>
#include <cstring>
#include <climits>

using namespace std;

typedef struct _cctv{
    int type;
    int r;
    int c;
    int dir;
}cctv;

vector<cctv> cctvs;
vector<cctv> cctvs5;

int cp_map[8][8];
int map[8][8];

int R, C;

int answer = INT_MAX;
int wall_cnt = 0;
int cctv5_cnt = 0;
int ans;

int cctv1(int, int, int dir, int map[][8]);
int cctv2(int, int, int dir, int map[][8]);
int cctv3(int, int, int dir, int map[][8]);
int cctv4(int, int, int dir, int map[][8]);
int cctv5();

void dfs(int depth){
    
    if(depth == cctvs.size()){
        int new_ans = ans;
        
        for(int i=0; i != R; ++i)
            memcpy(cp_map[i], map[i], sizeof(map[i]));

        for(int i=0; i<depth; i++){
            cctv cur = cctvs[i];
            switch(cur.type){
                case 1:
                    new_ans -= cctv1(cur.r, cur.c, cur.dir, cp_map);
                    break;
                case 2:
                    new_ans -= cctv2(cur.r, cur.c, cur.dir, cp_map);
                    break;
                case 3:
                    new_ans -= cctv3(cur.r, cur.c, cur.dir, cp_map);
                    break;
                case 4:
                    new_ans -= cctv4(cur.r, cur.c, cur.dir, cp_map);
                    break;
            }
        }
        if(answer > new_ans)
            answer = new_ans;
        
        return;
    }
    
    switch(cctvs[depth].type){
        case 1:
        case 3:
        case 4:
            for(int i=0; i<4; ++i){
                cctvs[depth].dir = i;
                dfs(depth+1);
                cctvs[depth].dir = -1;
            }
            break;
        case 2:
            for(int i=0; i<2; ++i){
                cctvs[depth].dir = i;
                dfs(depth+1);
                cctvs[depth].dir = -1;
            }
            break;
    }
}
int main(void){
    cin >> R >> C;
    for(int i=0; i!=R; ++i){
        for(int j=0; j!=C; ++j){
            cin >> map[i][j];
            if(map[i][j] > 0 && map[i][j] < 5)
                cctvs.push_back({map[i][j], i, j, -1});
            if(map[i][j] == 6)
                ++wall_cnt;
            if(map[i][j] == 5)
                cctvs5.push_back({5, i, j, -1});
        }
    }
    
    cctv5_cnt = cctv5();
    ans = R*C - wall_cnt - (int)cctvs.size() - (int)cctvs5.size() - cctv5_cnt;
    dfs(0);
    if(answer > ans){
        answer = ans;
    }
    
    cout << answer << endl;
}

int checkUp(int r, int c, int type, int map[][8]){
    int cnt=0;
    for(int i=r-1; i>=0; --i){
        if(map[i][c] == 6)
            break;
        if(map[i][c] == 0){
            ++cnt;
        }
        map[i][c] = type;
    }
    return cnt;
}
int checkDown(int r, int c, int type, int map[][8]){
    int i, cnt=0;
    for(i=r+1; i<R; ++i){
        if(map[i][c] == 6)
            break;
        if(map[i][c] == 0){
            ++cnt;
        }
        map[i][c] = type;
    }
    return cnt;
}
int checkRight(int r, int c, int type, int map[][8]){
    int cnt =0, j;
    for(j=c+1; j<C; ++j){
        if(map[r][j] == 6)
            break;
        if(map[r][j] == 0){
            ++cnt;
        }
        map[r][j] = type;
    }
    return cnt;
}
int checkLeft(int r, int c, int type, int map[][8]){
    int cnt=0, j;
    for(j=c-1; j>=0; --j){
        if(map[r][j] == 6)
            break;
        if(map[r][j] == 0){
            ++cnt;
        }
        map[r][j] = type;
    }
    return cnt;
}

int cctv1(int r, int c, int dir, int map[][8]){
    int cnt=0;
    switch(dir){
        case 0:
            cnt += checkUp(r, c, 1, map);
            break;
        case 1:
            cnt+= checkDown(r, c, 1, map);
            break;
        case 2:
            cnt += checkRight(r, c, 1, map);
            break;
        case 3:
            cnt += checkLeft(r, c, 1, map);
            break;
    }

    return cnt;
}
int cctv2(int r, int c, int dir, int map[][8]){
    int cnt=0;
    switch(dir){
        case 0:
            cnt += checkLeft(r, c, 2, map);
            cnt += checkRight(r, c, 2, map);
            break;
        case 1:
            cnt += checkUp(r, c, 2, map);
            cnt += checkDown(r, c, 2, map);
        break;
    }
    return cnt;
}
int cctv3(int r, int c, int dir, int map[][8]){
    int cnt=0;
    switch(dir){
        case 0:
            cnt += checkUp(r, c, 3, map);
            cnt += checkRight(r, c, 3, map);
            break;
        case 1:
            cnt += checkUp(r, c, 3, map);
            cnt += checkLeft(r, c, 3, map);
        break;
        case 2:
            cnt += checkRight(r, c, 3, map);
            cnt += checkDown(r, c, 3, map);
        break;
        case 3:
            cnt += checkLeft(r, c, 3, map);
            cnt += checkDown(r, c, 3, map);
        break;
    }
    return cnt;
}
int cctv4(int r, int c, int dir, int map[][8]){
    int cnt=0;
    switch(dir){
        case 0:
            cnt += checkUp(r, c, 4, map);
            cnt += checkDown(r, c, 4, map);
            cnt += checkLeft(r, c, 4, map);
            break;
        case 1:
            cnt += checkUp(r, c, 4, map);
            cnt += checkDown(r, c, 4, map);
            cnt += checkRight(r, c, 4, map);
            break;
        case 2:
            cnt += checkUp(r, c, 4, map);
            cnt += checkRight(r, c, 4, map);
            cnt += checkLeft(r, c, 4, map);
            break;
        case 3:
            cnt += checkDown(r, c, 4, map);
            cnt += checkRight(r, c, 4, map);
            cnt += checkLeft(r, c, 4, map);
            break;
    }
    return cnt;
}
int cctv5(){
    int cnt=0;
    for(int k=0; k<cctvs5.size(); ++k){
        cctv cur = cctvs5[k];
        cnt += checkUp(cur.r, cur.c, 5, map);
        cnt += checkDown(cur.r, cur.c, 5, map);
        cnt += checkRight(cur.r, cur.c, 5, map);
        cnt += checkLeft(cur.r, cur.c, 5, map);
    }

    return cnt;
}
