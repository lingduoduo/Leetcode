class ListNode {
 val: number
 next: ListNode | null
 constructor(val?: number, next?: ListNode | null) {
     this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


function rotateRight(head: ListNode | null, k: number): ListNode | null {
    if (head === null || head.next === null) return head;

    let dummy = new ListNode(-1);
    dummy.next = head;

    let n = 0;
    let p = dummy;
    while (p.next){
        p = p.next;
        n += 1;
    }

    k = k % n;
    if (k === 0) return head;

    let fast = dummy.next;
    let slow = dummy.next;

    for (let i = 0; i < k; i++){
        fast = fast.next!;
    }

    while (fast.next){
        fast = fast.next;
        slow = slow.next!;
    }

    fast.next = dummy.next;
    dummy.next = slow.next;
    slow.next = null;

    return dummy.next;
};