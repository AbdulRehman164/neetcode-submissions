class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
    const seen = new Set();
    let length = -Infinity;
    let L = 0;
    for (let R = 0; R < s.length; R++) {
        while (seen.has(s[R])) {
            seen.delete(s[L]);
            L++;
        }
        seen.add(s[R]);
        length = Math.max(length, R - L + 1);
    }
    return length === -Infinity ? 0 : length;
}
}
