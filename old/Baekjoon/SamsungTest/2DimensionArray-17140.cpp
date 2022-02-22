#define FILE_PATH "/Users/pd3chae/Xcode/test/test2/test2/input.txt"
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

typedef struct _st{
    int num;
    int cnt;
}elem;

int A[100][100];
int r, c, k;
int r_size, c_size;

bool comp(elem a, elem b){
    if(a.cnt == b.cnt)
         return a.num < b.num;
    else
        return a.cnt < b.cnt;
}

void r_oper(){
    vector<elem> empty;
    int elems[101];
    for(int i=0; i < r_size; ++i){
        memset(elems, 0, sizeof(elems));
        
        for(int j=0; j<c_size; ++j){
            if(A[i][j] == 0)
                continue;
            ++elems[A[i][j]];
        }
        
        vector<elem> elements;
        for(int j=1; j<=100; ++j){
            if(elems[j] > 0){
                elements.push_back({j, elems[j]});
            }
        }
        sort(elements.begin(), elements.end(), comp);
        
        int new_idx=0;
        for(int j=0; j<elements.size(); ++j){
            if(new_idx <= 98){
                A[i][new_idx++] = elements[j].num;
                A[i][new_idx++] = elements[j].cnt;
            }
        }
        elements = empty;
        
        if(new_idx < c_size){
            int lp = c_size - new_idx;
            for(int c=0; c<lp; ++c){
                A[i][new_idx++] = 0;
            }
        }
        
        c_size = max(c_size, new_idx);
    }
    
}
void c_oper(){
    vector<elem> empty;
    int elems[101];
    for(int j=0; j < c_size; ++j){
        memset(elems, 0, sizeof(elems));
        
        for(int i=0; i<r_size; ++i){
            if(A[i][j] == 0)
                continue;
            ++elems[A[i][j]];
        }
        
        vector<elem> elements;
        for(int i=1; i<=100; ++i){
            if(elems[i] > 0){
                elements.push_back({i, elems[i]});
            }
        }
        sort(elements.begin(), elements.end(), comp);
        
        int new_idx = 0;
        for(int i=0; i<elements.size(); ++i){
            if(new_idx <= 98){
                A[new_idx++][j] = elements[i].num;
                A[new_idx++][j] = elements[i].cnt;
            }
        }
        elements = empty;
        
        if(new_idx < r_size){
            int lp = r_size - new_idx;
            for(int c=0; c<lp; ++c){
                A[new_idx++][j] = 0;
            }
        }
        
        r_size = max(r_size, new_idx);
    }
    
    
}
int solution(){
    int answer = 0;
    
    while(1){
        if(A[r][c] == k)
            return answer;
        if(answer > 100)
            return -1;
        
        if(r_size>=c_size){ // R operation
            r_oper();
        }else{  // C operation
            c_oper();
        }

        ++answer;
    }
    return answer;
}

int main(void){
    cin >> r >> c >> k;
    --r; --c;
    
    r_size = 3;
    c_size = 3;
    for(int i=0; i!=r_size; ++i){
        for(int j=0; j!=c_size; ++j){
            cin >> A[i][j];
        }
    }

    cout << solution() << endl;
    return 0;
}

