#include <iostream>

using namespace std;

int N, M, H, Answer;
int MAP[11][30];
bool Visit[11][30];
bool available = false;

int Min(int A, int B) { if (A < B) return A; return B; }
bool Ladder_Game()
{
    for (int i = 1; i <= N; i++)
    {
        int Current_Num = i;
        for (int j = 1; j <= H; j++)
        {
            if (Visit[Current_Num][j] == true) Current_Num = Current_Num + 1;
            else if (Visit[Current_Num-1][j] == true) Current_Num = Current_Num - 1;
        }

        if (Current_Num != i) return false;
    }
    return true;
}

void Select_Line(int Idx, int Cnt)
{
    if (Cnt > 3) return;
    if (available == true) return;

    if (Ladder_Game() == true){
        Answer = Min(Answer, Cnt);
        return;
    }

    for (int i = Idx; i <= H; i++)
    {
        for (int j = 1; j < N; j++)
        {
            if (Visit[j][i] == true) continue;
            if (Visit[j - 1][i] == true) continue;
            if (Visit[j + 1][i] == true) continue;

            Visit[j][i] = true;
            Select_Line(i, Cnt + 1);
            Visit[j][i] = false;
        }
    }
}

int main(void){
    cin >> N >> M >> H;
    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        Visit[b][a] = true;
    }

    Select_Line(1, 0);

    if (available == false)
       Answer = -1;

   cout << Answer << endl;

    return 0;
}
