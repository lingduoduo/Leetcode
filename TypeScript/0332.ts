function findItinerary(tickets: string[][]): string[] {
  // Create adjacency list similar to defaultdict(list)
  const targets: Record<string, string[]> = {};

  // Build the mapping
  for (const [src, dst] of tickets) {
    if (!targets[src]) targets[src] = [];
    targets[src].push(dst);
  }

  // Sort destinations in reverse lexicographic order
  for (const key in targets) {
    targets[key].sort((a, b) => b.localeCompare(a));
  }

  const result: string[] = [];

  // Define the recursive backtracking function
  function dfs(airport: string) {
    while (targets[airport] && targets[airport].length > 0) {
      const nextAirport = targets[airport].pop()!; // take the smallest lexicographic destination
      dfs(nextAirport);
    }
    result.push(airport);
  }

  // Start DFS from "JFK"
  dfs("JFK");

  // Return reversed itinerary
  return result.reverse();
}
