class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map();
        let difference;
        for(let i = 0; i < nums.length; i++){
            difference = target - nums[i];
            if(map.get(difference) !== undefined) return [i, map.get(difference)];
            if(map.get(nums[i]) === undefined)map.set(nums[i], i);
        }
    }
}
