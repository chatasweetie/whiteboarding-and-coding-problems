#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int largest_number(const vector<int>& nums){
    vector<string> lex(nums.size());
    for(int i=0; i<nums.size(); i++)lex[i] = to_string(nums[i]);
    sort(lex.begin(), lex.end(), [](const string& a, const string& b){
        if(a.size() && b.size() && a[0] == b[0]){
            if(a.size() > b.size()){
                string pad = b;
                for(int i=b.size(); i<a.size(); i++)pad += '0';
                return a > pad;
            }else{
                string pad = a;
                for(int i=a.size(); i<b.size(); i++)pad += '0';
                return pad >= b;
            }
        }
        return a > b;
    } );
    string ret = accumulate(lex.begin(), lex.end(), string("") );
    return stoi(ret);
}


int main(){
    cout << "largest: " << largest_number(vector<int>{3,30,34,5,9}) << endl;
    cout << "largest: " << largest_number(vector<int>{330,33,34,5,9}) << endl;
    return 0;
}