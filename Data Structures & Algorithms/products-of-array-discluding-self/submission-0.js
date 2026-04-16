class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const solution = [];
        for(let i = 0; i<nums.length; i++){
            let product = 1;
            for(let j = 0; j<nums.length; j++){
                if(j === i) continue;
                product *= nums[j];
            }
            solution.push(product);
        }
        return solution;
    }
}
