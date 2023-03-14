class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:]
        i, n1, n2 = 0, 0, 0
        while n1 < m and n2 < n:
            if nums1_copy[n1] < nums2[n2]:
                nums1[i] = nums1_copy[n1]
                n1 += 1
            else:
                nums1[i] = nums2[n2]
                n2 += 1
            i += 1

        if n1 != m:
            while n1 != m:
                nums1[i] = nums1_copy[n1]
                n1 += 1
                i += 1
        if n2 != n:
            while n2 != n:
                nums1[i] = nums2[n2]
                n2 += 1
                i += 1

