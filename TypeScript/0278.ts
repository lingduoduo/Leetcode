var solution = function(isBadVersion: any) {
    return function(n: number): number {
        let l = 1, r = n; 
        while (l < r){
            let m = l + Math.floor((r - l) / 2);
            if (isBadVersion(m)) r = m;
            else l = m + 1;
        }
        return l;
    };
};