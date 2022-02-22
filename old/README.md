# StudyAlgorithm
This is a self-study record for problem solving.


## DFS 문
## DFS 문제 (BruteForce)
--  Algorithmic Problem Solving
- Boggle: 8 방향 체크 하는데 새로운 position을 DFS 인자로 넣어서 사용.
```cpp
const  int  dy[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dx[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
bool has_word(int y, int x, const string& word){
	if(y == 5 || x == 5 || y == -1 || x == -1) return false;
	if(maps[y][x] != word[0]) return false;
	if(word.size() == 1) return true;
	for(int i=0; i<8; i++){
		int nextY = y + dy[i];
		int nextX = x + dx[i];
		if(has_word(nextY, nextX, word.substr(1)))
			return true;
	}
	return false;
}
```
- Picnic: 두 명씩 짝 지어주기 bool type인 areFriends 배열로 짝을 지어주고 taken 배열로 이미 짝이 있는 사람을 제외 시킴
먼저 선택되는 친구를 의미하는 `firstFree` 변수를 사용함
```cpp
int  countParing(bool  taken[]){
	int firstFree =  -1;
	for(int i=0; i<N; i++){
		if(!taken[i]){
			firstFree = i;
			break;
		}
	}
	
	if(firstFree ==  -1) return  1;
	int ret =  0;
	for(int who=firstFree+1; who < N; who++){
		if(!taken[who] &&  areFriends[firstFree][who]){
			taken[firstFree] =  taken[who] =  true;
			ret +=  countParing(taken);
			taken[firstFree] =  taken[who] =  false;
		}
	}
	return ret;
}
```
-- Beakjoon 삼성역량테스트 기출 문제집
- 2048 Easy(#12100): 5번 움직일 수 있으므로 DFS를 이용한 모든 경우를 만들고 블록을 이동시켜 최댓값을 구함.
```cpp
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
```

## BFS 문제
-- Beakjoon 삼성역량테스트 기출 문제집
- 구슬 탈출2(#13460): 게임판을 4방면으로 기울이며 구슬을 구멍에 넣는 문제, 구슬을 이동이 불가능할 때까지 이동시켜야 하는데 이 부분이 가장 코드가 길었다. BFS를 적용하는 부분은 큰 어려움이 없었음.

##  시뮬레이션 문제
-- Beakjoon 삼성역량테스트 기출 문제집
- 뱀 (#3190): 뱀의 이동경로가 나타나고 게임 조건에 의해서 끝날때 까지 진행하는 문제. 문제 설명을 읽어만 보고는 종료조건을 정확하게 파악하기가 어려웠음.
- 이차원 배열
- 주사위 굴리기 (#14499): 주사위의 전개도를 그대로 두고 주사위를 굴릴 때 마다 전개도에 새로운 값을 입히듯이 구현함. 주사위는 6면체 밖에 되지 않기 때문에 한번의 이동으로 변경되는 면은 4개 밖에 없어서 경우에 따라 숫자를 연산하기 보다는 하드코딩 하는 것이 시간 단축에 더 좋을 듯.
```c
switch(dir){
case 0: // EAST
	dices[1] = tmp[4];
	dices[3] = tmp[1];
	dices[4] = tmp[6];
	dices[6] = tmp[3];
	break;
	
case 1: // WEST
	dices[1] = tmp[3];
	dices[3] = tmp[6];
	dices[4] = tmp[1];
	dices[6] = tmp[4];
	break;

case 2: // NORTH
	dices[1] = tmp[5];
	dices[2] = tmp[1];
	dices[5] = tmp[6];
	dices[6] = tmp[2];
	break;

case 3: // SOUTH
	dices[1] = tmp[2];
	dices[2] = tmp[6];
	dices[5] = tmp[1];
	dices[6] = tmp[5];
	break;
}
```
## 수학이 가미된 문제
-- Beakjoon 삼성역량테스트 기출 문제집
- 시험감독 (#13456): 처음에 이진탐색으로 최소값을 찾는 방법으로 잘못 접근한 문제. 나눗셈이 뭔지 알면 쉽게 해결할 수 있다.
```c
for(long long i=0; i != N; ++i){
        A[i] -= B;
        answer++;
        if(A[i] < 1)
            continue;

        if(A[i] % C == 0)
            answer += (A[i] / C);
        else
            answer += (A[i] / C + 1);
}
```제 (BruteForce)
--  Algorithmic Problem Solving
- Boggle: 8 방향 체크 하는데 새로운 position을 DFS 인자로 넣어서 사용.
```cpp
const  int  dy[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dx[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
bool has_word(int y, int x, const string& word){
	if(y == 5 || x == 5 || y == -1 || x == -1) return false;
	if(maps[y][x] != word[0]) return false;
	if(word.size() == 1) return true;
	for(int i=0; i<8; i++){
		int nextY = y + dy[i];
		int nextX = x + dx[i];
		if(has_word(nextY, nextX, word.substr(1)))
			return true;
	}
	return false;
}
```
- Picnic: 두 명씩 짝 지어주기 bool type인 areFriends 배열로 짝을 지어주고 taken 배열로 이미 짝이 있는 사람을 제외 시킴
먼저 선택되는 친구를 의미하는 `firstFree` 변수를 사용함
```cpp
int  countParing(bool  taken[]){
	int firstFree =  -1;
	for(int i=0; i<N; i++){
		if(!taken[i]){
			firstFree = i;
			break;
		}
	}
	
	if(firstFree ==  -1) return  1;
	int ret =  0;
	for(int who=firstFree+1; who < N; who++){
		if(!taken[who] &&  areFriends[firstFree][who]){
			taken[firstFree] =  taken[who] =  true;
			ret +=  countParing(taken);
			taken[firstFree] =  taken[who] =  false;
		}
	}
	return ret;
}
```
-- Beakjoon 삼성역량테스트 기출 문제집
- 2048 Easy: 5번 움직일 수 있으므로 DFS를 이용한 모든 경우를 만들고 블록을 이동시켜 최댓값을 구함.
```cpp
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
```

## BFS 문제
-- Beakjoon 삼성역량테스트 기출 문제집
- 구슬 탈출2: 게임판을 4방면으로 기울이며 구슬을 구멍에 넣는 문제, 구슬을 이동이 불가능할 때까지 이동시켜야 하는데 이 부분이 가장 코드가 길었다. BFS를 적용하는 부분은 큰 어려움이 없었음.

##  시뮬레이션 문제
-- Beakjoon 삼성역량테스트 기출 문제집
- 뱀 (#3190): 뱀의 이동경로가 나타나고 게임 조건에 의해서 끝날때 까지 진행하는 문제. 문제 설명을 읽어만 보고는 종료조건을 정확하게 파악하기가 어려웠음.
- 이차원 배열
- 주사위 굴리기 (#14499): 주사위의 전개도를 그대로 두고 주사위를 굴릴 때 마다 전개도에 새로운 값을 입히듯이 구현함. 주사위는 6면체 밖에 되지 않기 때문에 한번의 이동으로 변경되는 면은 4개 밖에 없어서 경우에 따라 숫자를 연산하기 보다는 하드코딩 하는 것이 시간 단축에 더 좋을 듯.
```c
switch(dir){
case 0: // EAST
	dices[1] = tmp[4];
	dices[3] = tmp[1];
	dices[4] = tmp[6];
	dices[6] = tmp[3];
	break;
	
case 1: // WEST
	dices[1] = tmp[3];
	dices[3] = tmp[6];
	dices[4] = tmp[1];
	dices[6] = tmp[4];
	break;

case 2: // NORTH
	dices[1] = tmp[5];
	dices[2] = tmp[1];
	dices[5] = tmp[6];
	dices[6] = tmp[2];
	break;

case 3: // SOUTH
	dices[1] = tmp[2];
	dices[2] = tmp[6];
	dices[5] = tmp[1];
	dices[6] = tmp[5];
	break;
}
```
## 수학이 가미된 문제
-- Beakjoon 삼성역량테스트 기출 문제집
- 시험감독 (#13456): 처음에 이진탐색으로 최소값을 찾는 방법으로 잘못 접근한 문제. 나눗셈이 뭔지 알면 쉽게 해결할 수 있다.
```c
for(long long i=0; i != N; ++i){
        A[i] -= B;
        answer++;
        if(A[i] < 1)
            continue;

        if(A[i] % C == 0)
            answer += (A[i] / C);
        else
            answer += (A[i] / C + 1);
}
```