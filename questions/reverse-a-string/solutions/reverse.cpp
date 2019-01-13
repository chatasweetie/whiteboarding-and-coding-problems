#include <iostream>
#include <string>

using namespace std;

string& reverse(string& str){
    auto fwd = str.begin();
    auto back = str.end() - 1;
    while(fwd != back){
        char tmp = *back;
        *back = *fwd;
        *fwd = tmp;
        fwd++; back--;
    }
    return str;
}

int main(){
    string test = "abcde";
    cout << reverse(test) << endl;
    return 0;
}