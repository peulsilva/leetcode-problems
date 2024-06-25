#include <bits/stdc++.h>

using namespace std;
class Solution {
public:

    bool subset_sum(int target, vector<int>& nums){
        vector<bool> has_sum(target+1, 0);

        has_sum[0] = true;
        for (auto& v: nums){
            for (int r = target; r >= v; r--){
                has_sum[r] = has_sum[r] || has_sum[r-v];
            }
        }

        return has_sum[target];
    }
    bool canPartition(vector<int>& nums) {
        int sum = 0;

        for (auto& el : nums){
            sum+= el;
        }

        if (sum % 2)
            return false;

        return subset_sum(sum/2, nums);
    }
};