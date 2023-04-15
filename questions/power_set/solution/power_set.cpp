#include <vector>
#include <iostream>

using namespace std;

template<typename T>
vector<vector<T>> powSet(vector<T> set, int n){    
    if(n == set.size()){
        return vector<vector<T>>{ vector<T>() };
    }
    vector<vector<T>> all;
    vector<vector<T>> sets = powSet(set, n+1);
    int val = set[n];
    for(auto s: sets){
        vector<T> cp(s);
        cp.push_back(val);
        all.push_back(s);
        all.push_back(cp);
    }
    return all;
}

template<typename T>
void print(const vector<vector<T>>& powset){
    cout << "power set: " << endl;
    for(vector<T> s : powset){
        cout << "{";
        for(T i : s)cout << i << ",";
        cout << "}, ";
    }
    cout << endl;
}

int main(){
    auto ps = powSet<int>(vector<int>{1, 2, 3, 4}, 0 );
    print<int>(ps);

    auto chps = powSet<char>(vector<char>{'a', 'b', 'c', 'd'}, 0 );
    print<char>(chps);
    return 0;
}
