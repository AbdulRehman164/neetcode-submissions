class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const prefixArr = [];
        let total = 1;
        let zeros = 0;
        for(let i = 0; i<nums.length;i++){
            if(zeros === 1 && nums[i] === 0){
                zeros++;
                break;
            }
            if(nums[i] === 0){
                zeros++;
                total *= 1;
            }else{
                total *= nums[i];
            }
            prefixArr.push(total);
        }

        const solution = [];
        for(let i = 0; i<nums.length; i++){
            if(zeros >= 2){
                solution.push(0);
            }
            else if(nums[i] === 0)
                solution.push(prefixArr[prefixArr.length - 1]);
            else if(zeros >= 1)
                solution.push(0);
            else
                solution.push(prefixArr[prefixArr.length - 1] / nums[i]);
        }
        return solution;
    }
}
