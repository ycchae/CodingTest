#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct st{
    int t1;
    int t2;
    inline bool operator<(const struct st& a){
        if(t1 == a.t1) return t2 < a.t2;
        else return t1 < a.t1;
    }
};

bool comp1(const struct st &a, const struct st &b){
    if(a.t1 == b.t1) return a.t2 < b.t2;
    else return a.t1 < b.t1;
}
bool operator<(const struct st& a, const struct st& b){
    if(a.t1 == b.t1) return a.t2 < b.t2;
    else return a.t1 < b.t1;
}

int main(){
    vector<struct st> v;
    struct st e1 = {1, 3};
    v.push_back(e1);
    struct st e2 = {1, 1};
    v.push_back(e2);

    sort(v.begin(), v.end());
    
    for(auto i = v.begin(); i != v.end(); i++){
        cout << (*i).t1 <<' ' << (*i).t2  << endl;
    }
    cout << (v[0] < v[1]) << endl;
}
