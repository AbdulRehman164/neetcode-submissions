class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */

    isPalindrome(s) {
        const isAlphanumeric = c => /^[a-zA-Z0-9]$/.test(c);

        let L = 0;
        let R = s.length - 1;
        
        while(L<R){
            while(L<R && !isAlphanumeric(s[L])) L++;
            while(L<R && !isAlphanumeric(s[R])) R--;
            if(s[L].toLowerCase() !== s[R].toLowerCase()) return false;
            L++;
            R--;
        }
        return true;
    }
}
