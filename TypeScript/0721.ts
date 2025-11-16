function accountsMerge(accounts: string[][]): string[][] {
    let edge: { [key: string]: string[] } = {};
    let names: { [key: string]: string } = {};

    for (let account of accounts) {
        const name = account[0];

        // i = 1..end are emails
        for (let i = 1; i < account.length; i++) {
            const email = account[i];

            // ensure node exists in edge
            if (!(email in edge)) edge[email] = [];

            // map every email to its name
            names[email] = name;

            // connect consecutive emails in this account
            if (i > 1) {
                const prevEmail = account[i - 1];
                edge[email].push(prevEmail);
                edge[prevEmail].push(email);
            }
        }
    }

    let visited: Set<string> = new Set();
    let res: string[][] = [];

    // start DFS/BFS from each email we know a name for
    for (let email in names) {
        if (!visited.has(email)) {
            let emails: string[] = [email];
            visited.add(email);
            let q: string[] = [email];

            while (q.length > 0) {
                let e = q.pop()!;
                for (let neighbor of edge[e]) {
                    if (!visited.has(neighbor)) {
                        emails.push(neighbor);
                        visited.add(neighbor);
                        q.push(neighbor);
                    }
                }
            }

            emails.sort();
            res.push([names[email], ...emails]);
        }
    }

    return res;
}