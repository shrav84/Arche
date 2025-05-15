# core/introspection.py

def reflect(memory_trace, associations):
    total = len(memory_trace)
    unique_stimuli = list({entry['stimulus']['type'] for entry in memory_trace})

    print("\n[ Introspection Report ]")
    print(f"Total experiences: {total}")
    print(f"Unique sensations: {', '.join(unique_stimuli)}")

    if associations:
        print("Frequently felt stimuli:")
        for stim, count in associations:
            print(f" - {stim}: {count} times")
    print()
