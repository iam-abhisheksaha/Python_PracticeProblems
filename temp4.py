from gettext import find


def findMedianSortedArrays(nums1, nums2):
        nums1 = nums1+nums2
        nums1.sort()
        if(len(nums1)%2==0):
            index = int(len(nums1)/2)
            sum = nums1[index] + nums1[index-1]
            sums = sum/2
            return sums
        else:
            index = int(len(nums1)/2)
            return nums1[index]


double 
