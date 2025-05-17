
from datetime import datetime
import uuid

class Memory:
    def __init__(self):
        self.trace = []

    def store(self, stimulus):
        """Store stimulus in memory with a unique ID and timestamp."""
        memory_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()

        entry = {
            "id": memory_id,
            "timestamp": timestamp,
            "stimulus": stimulus
        }

        self.trace.append(entry)
        return entry

    def recall_recent(self, n=5):
        """Recall the last n stored stimuli."""
        return self.trace[-n:]
