class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */

    isPalindrome(s) {
        let ss = '';
        for(const c of s){
            if(/^[a-zA-Z0-9]$/.test(c)) ss += c;
        }
        let L = 0;
        let R = ss.length - 1;
        while(L<R){
            if(ss[L].toLowerCase() !== ss[R].toLowerCase()) return false;
            L++;
            R--;
        }
        return true;
    }
}
