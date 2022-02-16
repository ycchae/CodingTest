#include <iostream>
#include <cstring>

using namespace std;

int N, L;
int map[100][100];

bool canBuild(const int map[], int base){
    int cnt = 1;
    
    for(int i=base; i < N-1; i++){
        if(map[i] == map[i+1])
            cnt++;
        else
            break;
    }
    
    if(cnt >= L)
        return true;
    else
        return false;
}

int solution(){
    int answer = 0;
    int cur_height = 0;
    int cnt = 0;
    int i, j;
    bool built[100];
    
    // horizontal
    for(i=0; i<N; ++i){
        memset(built, false, sizeof(built));
        cnt = 1;

        for(j=0; j<N-1; ++j){
            cur_height = map[i][j];
            if(cur_height == map[i][j+1]){
                cnt++;
                continue;
            }else if(cur_height - map[i][j+1] == 1 && !built[j+1]){        // down hill
                cnt = 1;
                if(canBuild(map[i], j+1)){
                    int b;
                    for(b=0; b != L; ++b){   // if overflow <- can't built so don't care
                        if(!built[j+1+b])
                            built[j+1+b] = true;
                        else
                            break;
                    }
                    if(b != L)
                        break;
                    j = j + L -1;
                    continue;
                }
                else break;
            }else if(cur_height - map[i][j+1] == -1 && !built[j]){       // up hill
                if(cnt >= L){
                    cnt = 1;
                    int b;
                    for(b=0; b != L; ++b){
                        if(!built[j-b])
                            built[j-b] = true;
                        else
                            break;
                    }
                    if(b != L)
                        break;
                    continue;
                }else{
                    cnt = 1;
                    break;
                }
            }else
                break;  // height diff > 1
            
        }   // j loop
        
        if(j == N-1){
            answer++;
        }
    }
    
    // vertical
    for(j=0; j<N; ++j){
        memset(built, false, sizeof(built));
        cnt = 1;
        
        for(i=0; i<N-1; ++i){
                cur_height = map[i][j];
                if(cur_height == map[i+1][j]){
                    cnt++;
                    continue;
                }else if(cur_height - map[i+1][j] == 1  && !built[i+1]){        // down hill
                    cnt = 1;
                    // copy one column to an array
                    int tmp_map[100];
                    for(int t=0; t < N; ++t){
                        tmp_map[t] = map[t][j];
                    }
                    // check construction availability
                    if(canBuild(tmp_map, i+1)){
                        int b;
                        for(b=0; b != L; ++b){
                            if(!built[i+1+b])
                                built[i+1+b] = true;
                            else
                                break;
                        }
                        if(b != L)
                            break;
                        
                        i = i + L -1;
                        continue;
                    }else
                        break;
                }else if(cur_height - map[i+1][j] == -1  && !built[i]){       // up hill
                    if(cnt >= L){
                        cnt = 1;
                        int b;
                        for(b=0; b != L; ++b){
                            if(!built[i-b])
                                built[i-b] = true;
                            else
                                break;
                        }
                        if(b != L)
                            break;
                        
                        continue;
                    }else{
                        cnt = 1;
                        break;
                    }
                    
                    
                }else  // hight diff > 1
                    break;
                
            }
            
            if(i == N-1){
                answer++;
            }
        }
    
    
    return answer;
}
int main(void){
    cin >> N >> L;
    
    for(int i=0; i != N; ++i){
        for(int j=0; j != N; ++j){
            cin >> map[i][j];
        }
    }
    
    cout << solution() << endl;
    return 0;
}
