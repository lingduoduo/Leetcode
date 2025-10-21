function canCompleteCircuit(gas: number[], cost: number[]): number {
    let cum = 0;
    let tot = 0;
    let res = 0;

    for (let i=0; i<gas.length; i++){
        cum += gas[i] - cost[i];
        tot += gas[i] - cost[i];

        if (cum < 0){
            cum = 0;
            res = i+1;
        }
    }

    if (tot < 0) return -1;
    else return res;
};