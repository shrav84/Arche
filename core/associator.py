from collections import defaultdict

class Associator:
    def __init__(self):
        self.associations = defaultdict(int)

    def observe(self, stimulus):
        key = stimulus["type"]
        self.associations[key] += 1

    def get_strongest_associations(self, top_n=3):
        sorted_items = sorted(self.associations.items(), key=lambda x: x[1], reverse=True)
        return sorted_items[:top_n]
