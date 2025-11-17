function validIPAddress(queryIP: string): string {
    // Try IPv4
    if (queryIP.includes(".")) {
        const nums = queryIP.split(".");

        // IPv4 must have exactly 4 parts
        if (nums.length !== 4) return "Neither";

        for (const part of nums) {
            // Part cannot be empty
            if (part.length === 0) return "Neither";

            // No leading zeros unless the part is exactly "0"
            if (part.length > 1 && part[0] === "0") return "Neither";

            // All characters must be digits
            if (!/^\d+$/.test(part)) return "Neither";

            const val = Number(part);
            if (val < 0 || val > 255) return "Neither";
        }

        return "IPv4";
    }

    // Try IPv6
    if (queryIP.includes(":")) {
        const nums = queryIP.split(":");
        const hexdigits = "0123456789abcdefABCDEF";

        // IPv6 must have exactly 8 parts
        if (nums.length !== 8) return "Neither";

        for (const part of nums) {
            // Each group must be 1–4 hex digits
            if (part.length === 0 || part.length > 4) return "Neither";

            // Check each character is valid hex
            for (const ch of part) {
                if (!hexdigits.includes(ch)) return "Neither";
            }
        }

        return "IPv6";
    }

    // Neither IPv4 nor IPv6 format
    return "Neither";
}
