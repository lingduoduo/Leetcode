
// Definition for _Node.
class _Node {
    val: number
    next: _Node | null
    random: _Node | null

    constructor(val?: number, next?: _Node, random?: _Node) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
        this.random = (random===undefined ? null : random)
    }
}



function copyRandomList(head: _Node | null): _Node | null {
    if (head === null) return null
    const d: Map<_Node, _Node> = new Map();
    let p: _Node | null = head;
    while (p !== null) {
        d.set(p, new _Node(p.val, null, null));
        p = p.next;
    }

    let p: _Node | null = head;
    while (p !== null) {
        const node = d.get(p)!;
        if (p.next) node.next = d.get(p.next)!;
        if (p.random) node.random = d.get(p.random)!;
        p = p.next;
     }
     return d.get(head)!;
};