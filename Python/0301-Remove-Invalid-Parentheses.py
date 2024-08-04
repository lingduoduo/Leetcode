class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        :type s: str
        :rtype: List[str]
        """

        left = 0
        right = 0

        # First, we find out the number of misplaced left and right parentheses.
        for char in s:
            # Simply record the left one.
            if char == "(":
                left += 1
            elif char == ")":
                # If we don't have a matching left, then this is a misplaced right, record it.
                right = right + 1 if left == 0 else right

                # Decrement count of left parentheses because we have found a right
                # which CAN be a matching one for a left.
                left = left - 1 if left > 0 else left

        result = {}

        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            # If we reached the end of the string, just check if the resulting expression is
            # valid or not and also if we have removed the total number of left and right
            # parentheses that we should have removed.
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)
                    result[ans] = 1
            else:
                # The discard case. Note that here we have our pruning condition.
                # We don't recurse if the remaining count for that parenthesis is == 0.
                if (s[index] == "(" and left_rem > 0) or (
                    s[index] == ")" and right_rem > 0
                ):
                    recurse(
                        s,
                        index + 1,
                        left_count,
                        right_count,
                        left_rem - (s[index] == "("),
                        right_rem - (s[index] == ")"),
                        expr,
                    )

                expr.append(s[index])

                # Simply recurse one step further if the current character is not a parenthesis.
                if s[index] != "(" and s[index] != ")":
                    recurse(
                        s, index + 1, left_count, right_count, left_rem, right_rem, expr
                    )
                elif s[index] == "(":
                    # Consider an opening bracket.
                    recurse(
                        s,
                        index + 1,
                        left_count + 1,
                        right_count,
                        left_rem,
                        right_rem,
                        expr,
                    )
                elif s[index] == ")" and left_count > right_count:
                    # Consider a closing bracket.
                    recurse(
                        s,
                        index + 1,
                        left_count,
                        right_count + 1,
                        left_rem,
                        right_rem,
                        expr,
                    )

                # Pop for backtracking.
                expr.pop()

                # Now, the left and right variables tell us the number of misplaced left and

        # right parentheses and that greatly helps pruning the recursion.
        recurse(s, 0, 0, 0, left, right, [])
        return list(result.keys())


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        lefts_to_remove, rights_to_remove = 0, 0
        lefts, rights = 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                lefts += 1
            elif s[i] == ")":
                if lefts > 0:
                    lefts -= 1
                else:
                    rights_to_remove += (
                        1  # if right doesn't have a matching left, it should be removed
                    )
        lefts_to_remove = (
            lefts  # if we have more lefts than rights, extra lefts should be removed
        )

        self.backtracking(0, 0, s, 0, "", res, lefts_to_remove, rights_to_remove)
        if not res:
            res.append("")

        return res

    def backtracking(
        self, lefts, rights, s, ind, cur_str, res, lefts_to_remove, rights_to_remove
    ):
        if ind == len(s):
            if (
                lefts == rights
                and lefts_to_remove == 0
                and rights_to_remove == 0
                and cur_str not in res
            ):
                res.append(cur_str)
            return

        if s[ind] == "(":
            if lefts_to_remove > 0:
                self.backtracking(
                    lefts,
                    rights,
                    s,
                    ind + 1,
                    cur_str,
                    res,
                    lefts_to_remove - 1,
                    rights_to_remove,
                )
            self.backtracking(
                lefts + 1,
                rights,
                s,
                ind + 1,
                cur_str + "(",
                res,
                lefts_to_remove,
                rights_to_remove,
            )

        elif s[ind] == ")":
            if (lefts == 0 or lefts >= rights) and rights_to_remove > 0:
                self.backtracking(
                    lefts,
                    rights,
                    s,
                    ind + 1,
                    cur_str,
                    res,
                    lefts_to_remove,
                    rights_to_remove - 1,
                )
            if lefts > rights:
                self.backtracking(
                    lefts,
                    rights + 1,
                    s,
                    ind + 1,
                    cur_str + ")",
                    res,
                    lefts_to_remove,
                    rights_to_remove,
                )

        else:
            self.backtracking(
                lefts,
                rights,
                s,
                ind + 1,
                cur_str + s[ind],
                res,
                lefts_to_remove,
                rights_to_remove,
            )
