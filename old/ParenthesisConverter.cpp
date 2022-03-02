#include <iostream>
#include <string>

using namespace std;

int main(void){
    string before = "[hot, dot, dog, lot, log, cog]";
    string after = "";

    for(int i=0; i<before.size(); i++){
        if(before[i] == '[')
            after += '{';
        else if(before[i] == ']')
            after += '}';
        else
            after += before[i];
    }

    std::string result = after;
    std::string::size_type pos = 0;
    std::string::size_type offset = 0;
    string pattern = ", ";
    string replace = "\", \"";
    while ((pos = result.find(pattern, offset)) != std::string::npos){
        result.replace(result.begin() + pos, result.begin() + pos + pattern.size(), replace);
        offset = pos + replace.size(); 
    }
    printf("%s\n", result.c_str());

    printf("%s\n", after.c_str());
    return 0;

}