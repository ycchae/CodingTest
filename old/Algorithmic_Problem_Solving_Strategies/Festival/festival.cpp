#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

double min_price(int, int, vector<int>&);
int main(void){
    int ntest =0, N=0, L=0;
    vector<int> prices;
    //freopen("input.txt","r",stdin);
    cin >> ntest;
    while(ntest != 0){
        cin >> N >> L;
        for(int i=0; i != N; ++i){
            int p=0;
            cin >> p;
            prices.push_back(p);
        }

        printf("%.11lf\n", min_price(N, L, prices));
        
        prices.clear();
        ntest--;
    }
    return 0;
}

double min_price(int N, int L, vector<int>& prices){
    double min = 100000000;

    for(int i=0; i<N-L+1; i++){       // origin+2times expand
        int pSum = 0;
        for(int j=0; j<L+i; j++){       // cal
            pSum += prices[j];
        }
        for(int k=-1; k<N-(L+i); k++){   // origin+2move
            if(k != -1){
                pSum -= prices[k];
                pSum += prices[L+i+k];
            }
            double avg = (double) pSum/(L+i);
            if(min > avg)
                min = avg;
        }
    }
    return min;
}
/*
double min_price(int N, int L, vector<int>& prices){
    double min = 1000000000.0;
    for(int i=0; i<N-L+1; i++){       // origin+2times expand
        for(int j=0; j<N-(L+i)+1; j++){   // move
            int pSum = 0;
            for(int k=j; k<L+i+j; k++){       // cal
                pSum += prices[k];
            }
            double avg = (double)pSum/(L+i);
            if(min > avg)
                min = avg;
        }
    }
    return min;
}
*/
