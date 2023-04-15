#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool addCandy(vector<int>& jars, int n, int start, int end){
    if(end < start)return false;
    if(start < 0 || end >= jars.size() )return false;
    for(int i=start; i<=end; i++)
        jars[i] += n;    
    return true;
}

double jarMean(const vector<int>& jars){
    double sum = static_cast<double>(accumulate(jars.begin(), jars.end(), 0));
    return sum / jars.size();
}

int main(){
    //*Example Input:* [5,[1,2,100],[2,5,100],[3,4,100]]
    vector<int> jars(5,0);
    addCandy(jars, 100, 0, 1);
    addCandy(jars, 100, 1, 4);
    addCandy(jars, 100, 2, 3);
    cout << "average: " << jarMean(jars) << endl;
    return 0;
}