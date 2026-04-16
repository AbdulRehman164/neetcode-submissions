class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let left = 0;
        let right = heights.length - 1;
        let max = -Infinity;
        while(left < right){
            max = Math.max(Math.min(heights[left], heights[right]) * (right - left), max);
            if(heights[left] < heights[right])left++;
            else right--;
        }
        return max;
    }
}
