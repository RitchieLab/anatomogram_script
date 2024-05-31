import json
import argparse
import matplotlib
import matplotlib.pyplot as plt
import pyanatomogram as pgram

parser = argparse.ArgumentParser(prog='Anatamogram Script', description='Creates anatamograms')
parser.add_argument("-i", "--input", required=True)
args = parser.parse_args()
in_file = args.input

f = open(in_file)
data = json.load(f)

gram = pgram.Anatomogram(data["species"])

for color in data["colors"]:
    gram.highlight_tissues(data["colors"][color], cmap=color)

fig, axes = matplotlib.pyplot.subplots(nrows=1, ncols=2)
axes[0].set_xlabel('Relative expression')
axes[0].set_ylabel('Organ')
gram.to_matplotlib(ax=axes[1])

plt.colorbar(ax=axes[1], orientation='horizontal', label='Relative expression')

plt.show()