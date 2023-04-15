#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map<string, int> cache;

int waysToMakeChange(int amount, const vector<int>& coins, int denom, vector<int>& way){
    string key = to_string(amount) + "," + to_string(denom);
    if(cache.find(key) != cache.end())return cache[key];
    if(amount == 0){
        for( auto x : way)cout << x << ",";
        cout << endl;
        return 1;
    }
    if(amount < 0)return 0;
    if(denom >= coins.size())return 0;
    int ways = 0;
    int coin = coins[denom];
    for(int i=0; (i*coin) <= amount; i++){
        vector<int> nw(way);
        for(int j=0; j<i;j++)nw.push_back(coin);
        ways += waysToMakeChange( amount - (i*coin), coins, denom+1, nw);            
    }
    cache[key] = ways;
    return ways;
}


int main(){
    vector<int> c;
    cout << "ways: " << waysToMakeChange(4, vector<int>{1,2,3}, 0, c ) << endl;

    cout << endl;
    cout << "ways: " << waysToMakeChange(56, vector<int>{1,5,10}, 0, c ) << endl;

    return 0;
}