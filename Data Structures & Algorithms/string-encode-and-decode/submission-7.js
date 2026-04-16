class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded = '';
        for(const str of strs){
            encoded += str.length + "#" + str;
        }
        return encoded;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        const result = [];
        let i = 0;
        while(i<str.length){
            let j = i;
            while(str[j++] !== "#");
            const len = Number(str.slice(i,j - 1));
            result.push(str.slice(j, j+len));
            i = j + len;
        }
            return result;
    }

}
