from datetime import datetime, timedelta
import uuid

class Memory:
    def __init__(self, decay_rate=0.01, min_weight=0.1):
        self.trace = []
        self.decay_rate = decay_rate      # per access decay factor
        self.min_weight = min_weight      # threshold for pruning

    def store(self, stimulus):
        """Store or reinforce a stimulus in memory."""
        now = datetime.now().isoformat()

        # Check if similar stimulus exists already (reinforce)
        for entry in self.trace:
            if entry["stimulus"] == stimulus:
                entry["weight"] += 1.0
                entry["timestamp"] = now  # Update last reinforced
                return entry

        # Else, create new memory entry
        memory_id = str(uuid.uuid4())
        entry = {
            "id": memory_id,
            "timestamp": now,
            "stimulus": stimulus,
            "weight": 1.0
        }
        self.trace.append(entry)
        return entry

    def decay(self):
        """Apply decay to all memory entries."""
        for entry in self.trace:
            entry["weight"] *= (1 - self.decay_rate)
        self.prune()

    def prune(self):
        """Remove memories below weight threshold."""
        self.trace = [m for m in self.trace if m["weight"] >= self.min_weight]

    def recall_recent(self, n=5):
        """Recall most recent N memories (by timestamp)."""
        self.decay()  # Optional: apply decay on access
        sorted_trace = sorted(self.trace, key=lambda x: x["timestamp"], reverse=True)
        return sorted_trace[:n]

    def recall_strongest(self, n=5):
        """Recall top N strongest memories (by weight)."""
        self.decay()
        sorted_trace = sorted(self.trace, key=lambda x: x["weight"], reverse=True)
        return sorted_trace[:n]
