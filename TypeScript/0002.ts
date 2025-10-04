// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

class Solution {
    addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
        let dummy = new ListNode(-1, null)
        let p = dummy
        let carry = 0

        while (l1 || l2) {
            let val = carry
            if (l1) {
                val += l1.val
                l1 = l1.next
            }
            if (l2) {
                val += l2.val
                l2 = l2.next
            }

            carry = Math.floor(val / 10)
            val = val % 10

            p.next = new ListNode(val)
            p = p.next
        }

        if (carry > 0) {
            p.next = new ListNode(carry)
        }

        return dummy.next
    }
}

// ---------- TEST ----------
function buildList(arr: number[]): ListNode | null {
    let dummy = new ListNode(0)
    let curr = dummy
    for (let num of arr) {
        curr.next = new ListNode(num)
        curr = curr.next
    }
    return dummy.next
}

function printList(head: ListNode | null): number[] {
    const result: number[] = []
    while (head) {
        result.push(head.val)
        head = head.next
    }
    return result
}

// Example test case
const sol = new Solution()
const l1 = buildList([2, 4, 3]) // represents 342
const l2 = buildList([5, 6, 4]) // represents 465
console.log(printList(sol.addTwoNumbers(l1, l2))) // [7, 0, 8] -> 807
