// Use C++'s ordered map's method upper_bound to keep tracing the max value and put the max value to result vector
// time is O(nlogn), space is O(n)
class Solution {
public:
    vector<int> fallingSquares(vector<vector<int>>& positions) {
        vector<int> res;
        map<pair<int, int>, int> m;
        int curMax = 0;
        for (auto &pos : positions) {
            vector<vector<int>> t;
            int len = pos[1];
            int start = pos[0];
            int end = start + len;
            int h = 0;
            auto iter = m.upper_bound({start, start});
            if (iter != m.begin() && (--iter)->first.second <= start) 
                ++iter;
            while (iter != m.end() && iter->first.first < end) {
                if (start > iter->first.first)
                    t.push_back({iter->first.first, start, iter->second});
                if (end < iter->first.second)
                    t.push_back({end, iter->first.second, iter->second});
                h = max(h, iter->second);
                iter = m.erase(iter);
            }
            m[{start, end}] = h + len;
            for (auto &a : t) {
                m[{a[0], a[1]}] = a[2];
            }
            curMax = max(curMax, h + len);
            res.push_back(curMax);
        }
        return res;
    }
};
