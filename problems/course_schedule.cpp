#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    // vector<bool> get_neighbors(int i, vector<vector<int>>& prerequisites){
    //     for (int i = 0; i < prerequisites[0].size(); i++)
    // }
    vector<int> topological_sort(unordered_map<int, vector<int>>& dependence_graph, int n_courses) {
        int n = dependence_graph.size();
        vector<int> result;
        unordered_map<int, int> in_degree;

        // Calculate the in-degree of each vertex
        for (auto& [k, vec] : dependence_graph) {
            for (auto v : dependence_graph[k]) {
                in_degree[v]++;
            }
        }

        // Enqueue all the vertices with in-degree 0
        queue<int> q;
        for (auto& [u, _] :dependence_graph) {
            if (in_degree[u] == 0) {
                q.push(u);
            }
        }

        // Perform topological sorting
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            result.push_back(u);

            for (auto v : dependence_graph[u]) {
                in_degree[v]--;
                if (in_degree[v] == 0) {
                    q.push(v);
                }
            }
        }

        return result;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {

        // graph[i] := courses that you must take i before
        unordered_map<int, vector<int>> graph;

        if (prerequisites.size() ==0)
            return true;

        for (int i =0 ; i <numCourses; i++)
            graph[i] = {};

        for (int i = 0; i < prerequisites.size(); i++){
            int a_i = prerequisites[i][0];
            int b_i = prerequisites[i][1];

            graph[b_i].push_back(a_i);
        }
        // vector<vector<bool>> visited (prerequisites.size(), vector<bool>(prerequisites[0].size()));
        vector<bool> visited(numCourses);

        vector<int> tsort = topological_sort(
            graph,
            numCourses
        );

        if (tsort.size() != numCourses)
            return false;

        return true;

    }
};