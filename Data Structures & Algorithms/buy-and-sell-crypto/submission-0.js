class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let max = 0;
        let L = 0;
        for(let R = 0;R<prices.length; R++){
            max = Math.max(max,prices[R] - prices[L]);
            if(prices[R] < prices[L]){
                L = R;
            }
        }
        return max;
    }

}
