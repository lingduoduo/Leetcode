function numberToWords(num: number): string {
  if (num === 0) return "Zero";

  const ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
  const teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
  const tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"];
  const suffixes = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion"];

  const words: string[] = [];
  let i = 0;

  while (num > 0) {
    const triplet = num % 1000;
    num = Math.floor(num / 1000);

    if (triplet !== 0) {
      const curr: string[] = [];

      const hundred = Math.floor(triplet / 100);
      const remainder = triplet % 100;

      if (hundred > 0) {
        curr.push(ones[hundred]);
        curr.push("Hundred");
      }

      if (remainder >= 10 && remainder <= 19) {
        curr.push(teens[remainder - 10]);
      } else {
        const ten = Math.floor(remainder / 10);
        const one = remainder % 10;
        if (ten > 0) curr.push(tens[ten]);
        if (one > 0) curr.push(ones[one]);
      }

      if (suffixes[i]) curr.push(suffixes[i]);
      words.unshift(curr.join(" "));
    }
    i++;
  }

  return words.join(" ").replace(/\s+/g, " ").trim();
}
