class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        const map = new Map();
        let L = 0;
        let maxFreq = 0;
        let best = 0;
        for(let R = 0; R<s.length; R++){
            map.set(s[R], map.has(s[R]) ? map.get(s[R]) + 1 : 1);
            maxFreq = Math.max(maxFreq, map.get(s[R]));
            while((R - L + 1) - maxFreq > k){
                map.set(s[L], map.get(s[L]) - 1);
                L++;
            }
            best = Math.max(best, R - L + 1);

        }
        return best;
    }
}
