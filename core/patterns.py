
from collections import defaultdict, Counter

class PatternDetector:
    def __init__(self):
        self.transitions = defaultdict(Counter)


    def observe_sequence(self, trace):
        for i in range(len(trace) - 1):
            current = trace[i]['stimulus']['type']
            next_ = trace[i + 1]['stimulus']['type']
            self.transitions[current][next_] += 1

    def get_frequent_patterns(self, threshold=2):
        patterns = []
        for stim_type, counter in self.transitions.items():
            for next_stim, count in counter.items():
                if count >= threshold:
                    patterns.append((stim_type, next_stim, count))
        return patterns

    def summarize_patterns(self, symbol_table):
        patterns = self.get_frequent_patterns()
        if not patterns:
            print("[ Pattern Detection ] No strong sequential patterns found.")
        else:
            print("\n[ Pattern Detection ]")
            for a, b, count in patterns:
                sym_a = symbol_table.get(a, "?")
                sym_b = symbol_table.get(b, "?")
                print(f" - {a} ({sym_a}) is often followed by {b} ({sym_b}) [{count} times]")
