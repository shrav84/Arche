# core/symbols.py

class SymbolTable:
    def __init__(self):
        self.symbol_map = {}
        self.counter = 1 
    def assign_symbol(self, stimulus_type):
        """Assign or retrieve a symbolic name for a stimulus type."""
        if stimulus_type not in self.symbol_map:
            symbol = f"Σ{self.counter}"  # Σ = Symbolic prefix
            self.symbol_map[stimulus_type] = symbol
            self.counter += 1
        return self.symbol_map[stimulus_type]

    def get_all_symbols(self):
        return dict(self.symbol_map)
