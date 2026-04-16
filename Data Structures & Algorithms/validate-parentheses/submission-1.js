class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const map = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        };
        const stack = [];
        for(let i = 0; i<s.length; i++){
            if(map[s[i]] !== undefined) // checking wether it is opening bracket or not
                stack.push(s[i]);
            else if(map[stack.pop()] !== s[i]) // stack.pop automatically returns undefined on empty stack
                    return false;
        }
        if(stack.length <= 0){
            return true;
        }
        return false;

    }
}
