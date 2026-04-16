class ListNode {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}
class LinkedList {
    constructor() {
        this.head = null;
        this.tail = this.head;
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        let i = 0;
        let cur = this.head;
        while (cur) {
            if (i === index) {
                return cur.val;
            }
            cur = cur.next;
            i++;
        }
        return -1;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        let newNode = new ListNode(val);
        if (!this.head) {
            this.tail = newNode;
        } else {
            newNode.next = this.head;
        }
        this.head = newNode;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        let newNode = new ListNode(val);
        if (!this.head) {
            this.head = newNode;
        } else {
            this.tail.next = newNode;
        }
        this.tail = newNode;
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    //[5,2,1,3,4]
    //[5,2,3,4]
    remove(index) {
        if (!this.head || index < 0) return false;

        if (index === 0) {
            this.head = this.head.next;
            if (!this.head) {
                this.tail = null;
            }
            return true;
        }

        let cur = this.head;
        let i = 0;
        while (cur && i < index - 1) {
            cur = cur.next;
            i++;
        }
        if (!cur || !cur.next) return false;
        if (cur.next === this.tail) {
            cur.next = null;
            this.tail = cur;
            return true;
        }

        cur.next = cur.next.next;
        return true;
    }

    /**
     * @return {number[]}
     */
    getValues() {
        let vals = [];
        let cur = this.head;
        while (cur) {
            if (cur.val !== undefined) vals.push(cur.val);
            cur = cur.next;
        }
        return vals;
    }
}
