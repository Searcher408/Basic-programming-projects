# Python3
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans


# 双指针 时间复杂度O(N) 空间复杂度O(1)
# 双指针代表的是可以作为容器边界的所有位置的范围。在一开始，双指针指向数组的左右边界，表示数组
# 中所有的位置都可以作为容器的边界。之后每次将对应的数字较小的指针往另一个指针的方向移动一个位置。
# C++
class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size() - 1;
        int ans = 0;

        while (l < r) {
            int area = min(height[l], height[r]) * (r - l);
            ans = max(ans, area);

            if (height[l] <= height[r]) {
                l++;
            } else {
                r--;
            }
        }

        return ans;
    }
};

# Java
public class Solution {
    public int maxArea(int[] height) {
        int l = 0, r = height.length - 1;
        int ans = 0;
        while (l < r) {
            int area = Math.min(height[l], height[r]) * (r - l);
            ans = Math.max(area, ans);

            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return ans;
    }
}