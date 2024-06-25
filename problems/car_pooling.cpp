#include <bits/stdc++.h>
using namespace std;
bool comp(vector<int>& a, vector<int>&b){
    return a[1] < b[1];
}
class Solution {
public:
    
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        sort(trips.begin(), trips.end(), comp);
        map<int,int> m; // m[i] : number of people leaving on destination i
        for (auto& t : trips){
            int position = t[1];
            int destination = t[2];
            for (auto it = m.begin(); it != m.end(); it++){
                if (it->first <= position){
                    capacity += it->second;
                    m.erase(it);
                }

                else
                    break;
            }
            capacity -= t[0];
            if (capacity < 0) return false;
            m[destination] += t[0];
        }
        return true;
    }
};