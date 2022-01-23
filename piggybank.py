from cdv.util.load_clvm import load_clvm

# load the clvm hex code (needs to be compiled first)
PIGGYBANK_PUZZLE = load_clvm("piggybank.clsp", "clsptest")

# create the piggybank coin
def create_piggybank(savings_goal, payout_puzzlehash):
    return PIGGYBANK_PUZZLE.curry(savings_goal, payout_puzzlehash)
