#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int n_days = days.size();

        vector<int> dp(n_days);

        for (int i = 0; i< n_days; i++){
            if (i ==0){
                dp[i] = min(costs[0], costs[1]);
                dp[i] = min(costs[2], dp[i]);
                continue;
            }

            int this_day = days[i];

            int single_ticket_cost, week_ticket_cost, month_ticket_cost;

            week_ticket_cost = 10000;
            month_ticket_cost = 10000;
            single_ticket_cost = min(dp[i-1] + costs[0], dp[i-1] + costs[1]);

            bool check_weekly = true;
            bool check_monthly = true;

            if (this_day <= 7){
                week_ticket_cost = costs[1];
                check_weekly = false;
            }

            if (this_day <= 30){
                month_ticket_cost = costs[2];
                check_monthly = false;
            }

            for (int j = i-1; j >= 0 ; j--){
                int another_day = days[j];

                if (this_day - another_day < 7 && check_weekly){
                    if (j > 0)
                        week_ticket_cost = dp[j-1] + costs[1];
                    else
                        week_ticket_cost = costs[1];
                }


                if (this_day - another_day < 30 && check_monthly){
                    if (j > 0)
                        month_ticket_cost = dp[j-1] + costs[2];

                    else
                        month_ticket_cost = costs[2];
                }

                if (this_day - another_day >= 30) break;
            }

            dp[i] = min(single_ticket_cost, week_ticket_cost);
            dp[i] = min(dp[i], month_ticket_cost);



        }
        return dp[n_days-1];
    }

};