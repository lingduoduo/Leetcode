function removeKdigits(num: string, k: number): string {
  if (k >= num.length) return "0";

  const stack: string[] = [];

  for (let i = 0; i < num.length; i++) {
    const ch = num[i];
    while (k > 0 && stack.length && stack[stack.length - 1] > ch) {
      stack.pop();
      k--;
    }
    stack.push(ch);
  }

  // If k remains, remove from the end
  while (k > 0 && stack.length) {
    stack.pop();
    k--;
  }

  // Remove leading zeros
  let start = 0;
  while (start < stack.length && stack[start] === "0") start++;

  const res = stack.slice(start).join("");
  return res.length ? res : "0";
}
