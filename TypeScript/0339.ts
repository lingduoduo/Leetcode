function depthSum(nestedList: NestedInteger[]): number {
  const stack: [NestedInteger, number][] = [];
  for (const num of nestedList) stack.push([num, 1]);

  let total = 0;

  while (stack.length > 0) {
    const [cur, depth] = stack.pop()!;

    if (cur.isInteger()) {
      total += cur.getInteger() * depth;
    } else {
      for (const child of cur.getList()) {
        stack.push([child, depth + 1]);
      }
    }
  }

  return total;
}
