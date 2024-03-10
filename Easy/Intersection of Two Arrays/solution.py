class Solution(object):
    def __init__(self):
        pass

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        intersection = []
        for num in nums2:
            if num in nums1_set:
                intersection.append(num)
                nums1_set.remove(num)
        return intersection

def main():
    sol = Solution()
    # Test cases
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print("Intersection of", nums1, "and", nums2, ":", sol.intersection(nums1, nums2))

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print("Intersection of", nums1, "and", nums2, ":", sol.intersection(nums1, nums2))

    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print("Intersection of", nums1, "and", nums2, ":", sol.intersection(nums1, nums2))

if __name__ == "__main__":
    main()
