# core/preferences.py

from collections import defaultdict

class PreferenceSystem:
    def __init__(self):
        self.preference_scores = defaultdict(float)

    def update_preferences(self, memory_trace):
        """
        Update preference scores based on recent memory trace.
        Score = cumulative weight of each stimulus type.
        """
        for mem in memory_trace:
            stim_type = mem["stimulus"]["type"]
            weight = mem.get("weight", 1.0)
            self.preference_scores[stim_type] += weight

    def get_top_preferences(self, top_n=3):
        sorted_prefs = sorted(self.preference_scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_prefs[:top_n]

    def print_preferences(self):
        print("\n[ Proto-Preferences Forming ]")
        if not self.preference_scores:
            print(" - No preferences detected yet.")
            return
        for stim, score in sorted(self.preference_scores.items(), key=lambda x: x[1], reverse=True):
            print(f" - Prefers {stim} (Score: {score:.2f})")
