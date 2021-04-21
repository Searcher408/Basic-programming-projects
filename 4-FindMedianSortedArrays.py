# Python3 归并排序，时间复杂度O(m + n), 空间复杂度O(m + n)
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        nums = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i = i + 1
            else:
                nums.append(nums2[j])
                j = j + 1

        while i < m:
            nums.append(nums1[i])
            i = i + 1

        while j < n:
            nums.append(nums2[j])
            j = j + 1

        t = len(nums)
        if t%2 == 0:   
            res = (nums[t//2] + nums[t//2 - 1]) / 2.0
        else:
            res = nums[t//2]

        #return format(res, '.5f')
        return res

def main():
    test = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    ans = test.findMedianSortedArrays(nums1, nums2)
    #print("%.5f" % ans)
    print(ans)

if __name__ == "__main__":
	main()

# Python3 二分查找 时间复杂度O(log(m+n)), 其中m和n分别是数组长度，空间复杂度O(1)
class Solution2:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1: #奇数
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

        def getKthElement(k):
            """
            - 思路：要找到第k(k>1)小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的"/"表示整除，初始 k = (m+n)/2 或 k = (m+n)/2+1 , 每轮循环可以将查找范围减半
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2), 两个数组中小于等于 pivot 的元素共计不会超过 k-2 个
            - 因此 pivot 最大只能是第 k-1 小的元素
            - 如果 pivot = pivot1, 那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素，排除后剩余的作为新的 nums1 数组
            - 如果 pivot = pivot2, 那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素，排除后剩余的作为新的 nums2 数组
            - 由于排除了上述比第 k 小的元素，所以需要更新 k 的值，减去排除的元素个数
            """

            index1, index2 = 0, 0

            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k -1]
                if k == 1:
                    return min(nums2[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m-1)
                newIndex2 = min(index2 + k // 2 - 1, n-1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

# C++ 二分查找
class Solution {
public:
    int getKthElement(const vector<int>& nums1, const vector<int>& nums2, int k) {
        int m = nums1.size();
        int n = nums2.size();
        int index1 = 0, index2 = 0;

        while (true) {
            if (index1 == m) {
                return nums2[index2 + k - 1];
            }
            if (index2 == n) {
                return nums1[index1 + k - 1];
            }
            if (k == 1) {
                return min(nums1[index1], nums2[index2]);
            }

            int newIndex1 = min(index1 + k / 2 - 1, m - 1);
            int newIndex2 = min(index2 + k / 2 - 1, n - 1);
            int pivot1 = nums1[newIndex1];
            int pivot2 = nums2[newIndex2];
            if (pivot1 <= pivot2) {
                k -= newIndex1 - index1 + 1;
                index1 = newIndex1 + 1;
            }
            else {
                k -= newIndex2 - index2 + 1;
                index2 = newIndex2 + 1;
            }
        }
    }

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int totalLength = nums1.size() + nums2.size();
        if (totalLength % 2 == 1) {
            return getKthElement(nums1, nums2, (totalLength + 1) / 2);
        }
        else {
            return (getKthElement(nums1, nums2, totalLength / 2) + getKthElement(nums1, nums2, totalLength / 2 + 1)) / 2.0;
        }
    }
};


