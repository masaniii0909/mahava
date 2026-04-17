import argparse as ap
from ddgs import DDGS
parser = ap.ArgumentParser()
parser.add_argument('--prompt')
args = parser.parse_args()

results = DDGS().text(f"{args.prompt}", max_results=1)
results = str(results)
results = results.split('body')
print(results[1])
