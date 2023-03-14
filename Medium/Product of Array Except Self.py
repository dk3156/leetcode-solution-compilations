class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #iterate through every element and record each number in dictionary with index
        #next time you get the products, you know the values on the left,
        #iterate through the right part and make the product of left and right side. 
    
        #reverse the original list, and store the index of each element with the product
        #on the right
        #iterate the list again, find out the product for each index
        #store the product in result with the right product.
        #create the right product the same way.

        r_product = {}
        l_product = {}
        rev = nums[-1::-1]
        res = []
        right = 1
        left = 1
        for i in range(len(rev)):
            if i == 0:
                r_product[len(rev) - 1 - i] = 1
            else:
                right *= rev[i - 1]
                r_product[len(rev) - 1 - i] = right
        
        print(r_product)

        for i in range(len(nums)):
            if i == 0:
                l_product[i] = 1
            else:
                left *= nums[i - 1]
                l_product[i] = left

        print(l_product)

        for i in range(len(nums)):
            res.append(l_product[i] * r_product[i])

        return res

        
            
