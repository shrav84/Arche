# main.py

from core import stimuli, memory, associator, introspection, symbols, visualizer, patterns
import time
import json
import os

# Initialize core modules
mind_memory = memory.Memory()
mind_associator = associator.Associator()
mind_symbols = symbols.SymbolTable()
mind_patterns = patterns.PatternDetector()
log_path = "logs/experiences"
os.makedirs(log_path, exist_ok=True)

def simulate_experience(cycles=10):
    
    print("[ Digital Mind Active ]")
    for i in range(cycles):
        stimulus = stimuli.generate_random_stimulus()
        memory_entry = mind_memory.store(stimulus)
        mind_associator.observe(stimulus)

        symbol = mind_symbols.assign_symbol(stimulus["type"])
        print(f"Cycle {i+1}: Felt {stimulus['type']} ({symbol}) with intensity {stimulus['intensity']}")


        # Log each experience
        with open(f"{log_path}/exp_{i+1}.json", "w") as f:
            json.dump(memory_entry, f, indent=4)

        time.sleep(0.5)
        

    # Reflect at the end
    top_associations = mind_associator.get_strongest_associations()
    introspection.reflect(mind_memory.trace, top_associations)

    # Pattern detection from memory trace
    mind_patterns.observe_sequence(mind_memory.trace)
    mind_patterns.summarize_patterns(mind_symbols.get_all_symbols())

    # Build symbol table for visualization
    symbol_map = mind_symbols.get_all_symbols()
    G = visualizer.build_memory_graph(mind_memory.trace, symbol_map)
    visualizer.draw_graph(G)
    # Print symbols
    print("[ Symbol Table ]")
    for stim_type, sym in mind_symbols.get_all_symbols().items(): 
        print(f" - {stim_type} → {sym}")


if __name__ == "__main__":
    simulate_experience(cycles=10)
