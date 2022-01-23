from cdv.util.load_clvm import load_clvm

# load the clvm hex code (needs to be compiled first)
PIGGYBANK_PUZZLE = load_clvm("piggybank.clsp", "clsptest")

print(PIGGYBANK_PUZZLE)
