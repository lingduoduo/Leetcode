"""
Provides word lists with frequency data.
get_test_dictionary() is useful when developing your Checker.
"""

from typing import Dict


def get_test_dictionary() -> Dict[str, int]:
    return {
        "the": 69970, "be": 36410, "to": 26150, "of": 25460,
        "and": 22860, "a": 21900, "in": 18960, "that": 12530,
        "have": 11990, "i": 10930, "it": 10760, "for": 9490,
        "not": 9440, "on": 7870, "with": 7290, "he": 7030,
        "as": 6530, "you": 6120, "do": 5860, "at": 5510,
        "this": 5340, "but": 4950, "his": 4940, "by": 4390,
        "from": 4310, "they": 3960, "we": 3810, "her": 3400,
        "she": 3310, "or": 3230, "an": 3130, "will": 2990,
        "my": 2610, "one": 2540, "all": 2470, "had": 2350,
        "there": 2310, "been": 2250, "if": 2200, "more": 2160,
        "when": 2100, "no": 2060, "who": 1960, "out": 1910,
        "so": 1890, "up": 1850, "said": 1810, "what": 1790,
        "its": 1760, "about": 1710, "into": 1660, "them": 1610,
        "than": 1570, "then": 1530, "now": 1490, "come": 1370,
        "make": 1340, "like": 1310, "time": 1290, "just": 1250,
        "know": 1200, "take": 1160, "people": 1040, "could": 1010,
        "your": 980, "some": 960, "other": 930, "these": 880,
        "thing": 740, "think": 720, "those": 690, "house": 540,
        "horse": 390, "hose": 310, "hope": 290, "hole": 270,
        "home": 520, "hello": 210, "help": 450, "here": 680,
        "hear": 320, "heat": 240, "heap": 110, "heal": 90,
        "head": 460, "heart": 380, "heavy": 200, "hence": 80,
    }


def get_large_dictionary() -> Dict[str, int]:
    base = get_test_dictionary()
    for i in range(50000):
        base[f"xword{i}"] = i + 1
    return base
