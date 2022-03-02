#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int N;
int board[20][20];
int copy_board[20][20];

int answer = -1;

int moves[5];

void moveUp(){
    vector<int> line;
    vector<int> new_line;
    
    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            if(copy_board[j][i] != 0)
                line.push_back(copy_board[j][i]);
        }
        while(!line.empty()){
            if(line.size() >= 2){
                if(*(line.begin()) == *(line.begin()+1)){
                    new_line.push_back(*(line.begin())*2);
                    line.erase(line.begin());
                    line.erase(line.begin());
                }else{
                    new_line.push_back(*(line.begin()));
                    line.erase(line.begin());
                }
            }else{
                new_line.push_back(*(line.begin()));
                line.erase(line.begin());
            }
        }
        int cnt = (int)new_line.size();
        for(int j=0; j<N; ++j){
            if(j < cnt){
                copy_board[j][i] = *(new_line.begin());
                new_line.erase(new_line.begin());
            }else{
                copy_board[j][i] = 0;
            }
        }
    }
}
void moveDown(){
    vector<int> line;
    vector<int> new_line;
    
    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            if(copy_board[j][i] != 0)
                line.push_back(copy_board[j][i]);
        }
        while(!line.empty()){
            if(line.size() >= 2){
                if(*(line.end()-1) == *(line.end()-2)){
                    new_line.insert(new_line.begin(), *(line.end()-1)*2);
                    line.pop_back();
                    line.pop_back();
                }else{
                    new_line.insert(new_line.begin(), *(line.end()-1));
                    line.pop_back();
                }
            }else{
                new_line.insert(new_line.begin(), *(line.end()-1));
                line.pop_back();
            }
        }
        int cnt = (int)new_line.size();
        for(int j=0; j<N; ++j){
            if(j < N-cnt){
                copy_board[j][i] = 0;
            }else{
                copy_board[j][i] = *(new_line.begin());
                new_line.erase(new_line.begin());
            }
        }
    }
}
void moveRight(){
    vector<int> line;
    vector<int> new_line;
    
    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            if(copy_board[i][j] != 0)
                line.push_back(copy_board[i][j]);
        }
        while(!line.empty()){
            if(line.size() >= 2){
                if(*(line.end()-1) == *(line.end()-2)){
                    new_line.insert(new_line.begin(), *(line.end()-1)*2);
                    line.pop_back();
                    line.pop_back();
                }else{
                    new_line.insert(new_line.begin(), *(line.end()-1));
                    line.pop_back();
                }
            }else{
                new_line.insert(new_line.begin(), *(line.end()-1));
                line.pop_back();
            }
        }
        int cnt = (int)new_line.size();
        for(int j=0; j<N; ++j){
            if(j < N-cnt){
                copy_board[i][j] = 0;
            }else{
                copy_board[i][j] = *(new_line.begin());
                new_line.erase(new_line.begin());
            }
        }
    }
}
void moveLeft(){
    vector<int> line;
    vector<int> new_line;
    
    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            if(copy_board[i][j] != 0)
                line.push_back(copy_board[i][j]);
        }
        while(!line.empty()){
            if(line.size() >= 2){
                if(*(line.begin()) == *(line.begin()+1)){
                    new_line.push_back(*(line.begin())*2);
                    line.erase(line.begin());
                    line.erase(line.begin());
                }else{
                    new_line.push_back(*(line.begin()));
                    line.erase(line.begin());
                }
            }else{
                new_line.push_back(*(line.begin()));
                line.erase(line.begin());
            }
        }
        int cnt = (int)new_line.size();
        for(int j=0; j<N; ++j){
            if(j < cnt){
                copy_board[i][j] = *(new_line.begin());
                new_line.erase(new_line.begin());
            }else{
                copy_board[i][j] = 0;
            }
        }
    }
}


void dfs(int depth){
    if(depth == 5){        
        for(int i=0; i<N; i++)
            memcpy(copy_board[i], board[i], sizeof(board[i]));
        
        for(int i=0; i<5; i++){     // 5 moves
            switch(moves[i]){
                case 0: moveUp(); break;
                case 1: moveRight(); break;
                case 2: moveDown(); break;
                case 3: moveLeft(); break;
            }
        }
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(answer == -1 || answer < copy_board[i][j])
                    answer = copy_board[i][j];
            }
        }
        
        return;
    }
    for(int i=0; i<4; i++){     // select moves
        moves[depth] = i;
        dfs(depth+1);
    }
}
int main(void){
    cin >> N;
    memset(board, 0, sizeof(board));
    memset(moves, -1, sizeof(moves));
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++)
            cin >> board[i][j];
    }
    dfs(0);
    cout << answer << endl;
}

