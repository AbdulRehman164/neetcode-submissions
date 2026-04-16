class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        const quickSort = (nums, s = 0, e = nums.length - 1)=>{
            if(e - s + 1 <= 1){
                return nums;
            }
            let pivot = nums[e];
            let left = s;
            let tmp;
            for(let i = s; i<=e;i++){
                if(nums[i] < pivot){
                    tmp = nums[left];
                    nums[left] = nums[i];
                    nums[i] = tmp
                    left++;
                }
            }
            nums[e] = nums[left];
            nums[left] = pivot;

            quickSort(nums, s, left - 1);
            quickSort(nums, left + 1, e);
        }
        quickSort(nums);
        let left;
        let right;
        let sum;
        let result = [];
        for(let i = 0; i<nums.length; i++){
            if(i > 0 && nums[i] === nums[i - 1]) continue;
            left = i + 1;
            right = nums.length -1;
            while(left < right){
                sum = nums[left] + nums[right] + nums[i];
                if(sum < 0){
                    left++;
                }else if(sum > 0){
                    right--;
                }else{
                    result.push([nums[left], nums[right], nums[i]]);
                    while(left < right && nums[left] === nums[left + 1]) left++;
                    while(left < right && nums[right] === nums[right - 1]) right--;
                    left++;
                    right--;
                }
            }
        }
        return result;
    }
}
