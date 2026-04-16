class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const obj = {};
        for(const num of nums){
            if(num in obj) return true;
            obj[num] = 1;
        }
        return false;
    }
}
