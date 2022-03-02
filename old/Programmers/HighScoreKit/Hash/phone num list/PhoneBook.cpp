#include <string>
#include <vector>

using namespace std;

bool prefix_check(string str1, string str2){
    int len1 = str1.length();
    int len2 = str2.length();
    
    if(len1 < len2){
        if(str2.compare(0, len1, str1) == 0)
            return false;
    }else{
        if(str1.compare(0, len2, str2) == 0)
            return false;
    }
    
    return true;
}

bool solution(vector<string> phone_book) {
    for(int i=0; i<phone_book.size()-1; ++i){
        for(int j=i+1; j<phone_book.size(); ++j){
            if(prefix_check(phone_book[i], phone_book[j]) == false)
                return false;
        }
    }
    
    return true;
}