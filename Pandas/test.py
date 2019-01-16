import pandas as pd
import os
import pdb

os.chdir("/Users/dmadhok/Desktop/Pandas")
pokemondf = pd.read_csv("pokemon.csv")
print pokemondf
print pokemondf.Type.value_counts()
