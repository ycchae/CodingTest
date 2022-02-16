#include <iostream>

using namespace std;

int solution(long long &A, long long &B){
    int day =0;
    do{
        A *= 2;
        B *= 3;
        day++;
    }while(A > B);

    return day;
}
int main(void){
    int n;
    long long A, B;
    // freopen("input.txt","r",stdin);
    
    cin >> n;
    while(n-- != 0){
        cin >> A >> B;
        cout << solution(A, B) << endl;
    }
}

/* input
4
7 1
8 3
4 4
4500 2
*/
