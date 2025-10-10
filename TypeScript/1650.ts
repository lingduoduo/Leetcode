function lowestCommonAncestor(p: _Node | null, q: _Node | null): _Node | null {
    let p1 = p;
    let p2 = q;
    while (p1 !== p2) {
        p1 = p1 ? p1.parent : q;
        p2 = p2 ? p2.parent : p;
    }
    return p1;
};