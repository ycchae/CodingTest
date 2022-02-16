#define FILE_PATH "/Users/pd3chae/Xcode/test/test2/test2/input.txt"
// 14:43~(15:18~15:22)~16:05 16:08
#include <iostream>
#include <deque>
#include <set>
#include <algorithm>

using namespace std;

typedef struct _tree{
    int age;
    int status; // 0 alive 1 dead
    
    inline bool erase_dead(){
        return status == 1;
    }
}tree;

typedef struct _land{
    int nutri;
    deque<tree> trees;
}land;

int N, M, K;
land map[11][11];
int s2d2[11][11];

void spring();
void summer();
void fall();
void winter();

// NW, N, NE, E, SE, S, SW, W
int dr[] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dc[] = {-1, 0, 1, 1, 1, 0, -1, -1};

set<pair<int, int>> pos;

bool comp (struct _tree a, struct _tree b){
    return a.age < b.age;
}

int solution(){
    int cnt = 0;
    int answer =0;
    while(cnt != K){
        spring();
        summer();
        fall();
        
        if(cnt == K-1){
            set<pair<int, int>>::iterator s;
            for(s = pos.begin(); s != pos.end(); ++s){
                int r = (*s).first;
                int c = (*s).second;
                land cur = map[r][c];
                
                answer += (int)cur.trees.size();
            }
            return answer;
        }
        
        winter();
        ++cnt;
        
        cout << "================" << endl;
        cout << cnt << endl;
        for(int i=1; i<=N; ++i){
            for(int j=1; j<=N; ++j){
                printf("%d %d %d  ", map[i][j].nutri, (int)map[i][j].trees.size(), (*map[i][j].trees.begin()).age);
            }
            cout << "\n";
        }
        cout << "\n";
    }
    
    return answer;
}
void tree_insert(int r, int c, int z){
    tree new_tree = {z, 0};
    deque<tree>::iterator iter = lower_bound(map[r][c].trees.begin(), map[r][c].trees.end(), new_tree, comp);
    map[r][c].trees.insert(iter, new_tree);
}
int main(void){
    freopen(FILE_PATH, "r", stdin);
    cin >> N >> M >> K;
    
    for(int i=1; i<=N; ++i){
        for(int j=1; j<=N; ++j){
            cin >> s2d2[i][j];
            map[i][j].nutri = 5;
        }
    }
    
    for(int i=0; i<M; ++i){
        int x, y, z;
        cin >> x >> y >> z;
        tree_insert(x, y, z);
        pos.insert(make_pair(x, y));
    }
    
    printf("%d\n", solution());
}

void spring(){
    set<pair<int, int>>::iterator s;
    for(s = pos.begin(); s != pos.end(); ++s){
        int r = (*s).first;
        int c = (*s).second;
        land cur = map[r][c];
        
        for(deque<tree>::iterator iter = cur.trees.begin(); iter != cur.trees.end(); ++iter){
            if(cur.nutri > 0){  // is nutri > 0
                if(cur.nutri < (*iter).age){  // die
                    (*iter).status = 1;
                }else{      // grow
                    cur.nutri -= (*iter).age;
                    ++(*iter).age;
                }
            }else{      // die all
                (*iter).status = 1;
            }
        }
        
        for(deque<tree>::iterator iter = cur.trees.begin(); iter != cur.trees.end();){
            if((*iter).status == 1){
                cur.nutri += (*iter).age / 2;
                iter = cur.trees.erase(iter);
            }else{
                ++iter;
            }
        }
        if(cur.trees.size() == 0)
            s = pos.erase(pos.find(make_pair(r, c)));
        else ++s;
    
        map[r][c] = cur;
    }
}
void summer(){
    set<pair<int, int>>::iterator s;
    for(s = pos.begin(); s != pos.end();){
        int r = (*s).first;
        int c = (*s).second;
        land cur = map[r][c];
        
        
        
        map[r][c] = cur;
    }
}
void fall(){
    set<pair<int, int>>::iterator s;
    for(s = pos.begin(); s != pos.end(); ++s){
        int r = (*s).first;
        int c = (*s).second;
        land cur = map[r][c];
        
        for(deque<tree>::iterator iter = cur.trees.begin(); iter != cur.trees.end(); ++iter){
            if((*iter).age % 5 == 0){   // make child
                for(int i=0; i<8; ++i){
                    int nr = r + dr[i];
                    int nc = c + dc[i];
                    if(nr < 1 || nr > N || nc < 1 || nc > N)
                        continue;
                    tree_insert(nr, nc, 1);
                    pos.insert(make_pair(nr, nc));
                }
            }
        }
        map[r][c] = cur;
    }
}

void winter(){
    for(int i=1; i<=N; ++i){
        for(int j=1; j<=N; ++j){
            map[i][j].nutri += s2d2[i][j];
        }
    }
}
