from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        bit_skills = {}
        for i, skill in enumerate(req_skills): 
            bit_skills[skill] = 1 << i
  
        target_skills = (1 << len(req_skills)) - 1
        dp = [None] * (target_skills + 1)
        dp[0] = []

        for i, person_skills in enumerate(people):
            person_bitmask = sum(bit_skills[skill] for skill in person_skills)
            for covered_skills, team in enumerate(dp):
                if team is None: 
                    continue
                new_skills = covered_skills | person_bitmask
                if new_skills == covered_skills: 
                    continue
                if dp[new_skills] is None or len(dp[new_skills]) > len(team) + 1 : dp[new_skills] = team + [i]

        return dp[target_skills]      