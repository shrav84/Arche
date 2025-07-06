# main.py

from core import stimuli, memory, associator, introspection, symbols, visualizer, patterns
import time
import json
import os

# === Initialize Core Modules === #
mind_memory = memory.Memory(decay_rate=0.05, min_weight=0.2)
mind_associator = associator.Associator()
mind_symbols = symbols.SymbolTable()
mind_patterns = patterns.PatternDetector()

log_path = "logs/experiences"
os.makedirs(log_path, exist_ok=True)

# === Experience Simulation Loop === #
def simulate_experience(cycles=10):
    print("[ Digital Mind Active ]\n")

    for i in range(cycles):
        # Generate and store stimulus
        stimulus = stimuli.generate_random_stimulus()
        memory_entry = mind_memory.store(stimulus)
        mind_associator.observe(stimulus)

        # Assign or retrieve symbol
        symbol = mind_symbols.assign_symbol(stimulus["type"])
        print(f"Cycle {i+1}: Felt {stimulus['type']} ({symbol}) with intensity {stimulus['intensity']:.2f} | Weight: {memory_entry['weight']:.2f}")

        # Log experience to disk
        with open(f"{log_path}/exp_{i+1}.json", "w") as f:
            json.dump(memory_entry, f, indent=4)

        # Simulate time passing (and decay happening)
        time.sleep(0.5)

    # === Introspection & Analysis === #
    print("\n[ Reflecting on Experience ]")
    top_associations = mind_associator.get_strongest_associations()
    introspection.reflect(mind_memory.trace, top_associations)

    # Detect patterns from memory trace
    mind_patterns.observe_sequence(mind_memory.trace)
    mind_patterns.summarize_patterns(mind_symbols.get_all_symbols())

    # Visualize memory graph
    symbol_map = mind_symbols.get_all_symbols()
    G = visualizer.build_memory_graph(mind_memory.trace, symbol_map)
    visualizer.draw_graph(G)

    # Print symbol table
    print("\n[ Symbol Table ]")
    for stim_type, sym in symbol_map.items():
        print(f" - {stim_type} → {sym}")

    # Show top-weighted memories
    print("\n[ Strongest Memories ]")
    for mem in mind_memory.recall_strongest(n=5):
        print(f" - {mem['stimulus']['type']} (Weight: {mem['weight']:.2f}) at {mem['timestamp']}")


if __name__ == "__main__":
    simulate_experience(cycles=10)
