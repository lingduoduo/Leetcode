"""You'll implement this."""

from typing import List

from word_list import WordList


class MaxUniqueSolver:
    """Finds the subset of valid words that maximizes total unique characters."""

    def __init__(self, word_list: WordList):
        self.word_list = word_list

    def solve(self) -> List[str]:
        """Find the subset of words that maximizes total unique characters.
        
        Uses optimized DP with pruning for efficiency.
        """
        valid_words = self.word_list.valid_words()
        if not valid_words:
            return []
        
        # Convert alphabet to list for bit indexing
        alphabet = sorted(list(self.word_list.alphabet()))
        char_to_bit = {char: i for i, char in enumerate(alphabet)}
        
        # Convert words to (mask, char_count, word_index)
        word_data = []
        for i, word in enumerate(valid_words):
            mask = 0
            char_count = 0
            for char in self.word_list.char_set(word):
                if char in char_to_bit:
                    mask |= (1 << char_to_bit[char])
                    char_count += 1
            word_data.append((mask, char_count, i))
        
        # Sort by efficiency (chars per word) descending
        word_data.sort(key=lambda x: x[1], reverse=True)
        
        # Use iterative deepening with early termination
        best_result = []
        best_chars = 0
        
        # Try greedy first for a good baseline
        used_chars = set()
        greedy_result = []
        for mask, char_count, word_idx in word_data:
            word_chars = self.word_list.char_set(valid_words[word_idx])
            if not (word_chars & used_chars):
                greedy_result.append(word_idx)
                used_chars |= word_chars
                best_chars += char_count
        
        best_result = greedy_result
        
        # Now try DP with limited states to improve on greedy
        max_states = 50000  # Limit memory usage
        dp = {0: (0, [])}  # mask -> (max_chars, word_indices)
        
        for mask, char_count, word_idx in word_data:
            if len(dp) > max_states:
                # Keep only the best states
                sorted_states = sorted(dp.items(), key=lambda x: x[1][0], reverse=True)
                dp = dict(sorted_states[:max_states//2])
            
            new_dp = {}
            
            for used_mask, (max_chars, word_indices) in dp.items():
                # Keep existing state
                if used_mask not in new_dp or new_dp[used_mask][0] < max_chars:
                    new_dp[used_mask] = (max_chars, word_indices)
                
                # Try adding current word if no conflict
                if used_mask & mask == 0:
                    new_mask = used_mask | mask
                    new_chars = max_chars + char_count
                    new_indices = word_indices + [word_idx]
                    
                    if new_mask not in new_dp or new_dp[new_mask][0] < new_chars:
                        new_dp[new_mask] = (new_chars, new_indices)
                        
                        # Update best result if improved
                        if new_chars > best_chars:
                            best_chars = new_chars
                            best_result = new_indices
            
            dp = new_dp
        
        return [valid_words[i] for i in best_result]