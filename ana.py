import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pyanatomogram as pgram
import argparse
import json

def load_data(parser):
    args = parser.parse_args()
    in_file = args.input
    f = open(in_file)
    return json.load(f)

def create_plot(data):
    dfs = []
    norms = []
    colors = ['Oranges', 'Blues', 'Reds','Purples',  'Greens', 'Greys']
    keys = data.keys()
    nrows = len(keys)

    gs = gridspec.GridSpec(nrows, 2)
    gram = pgram.Anatomogram('homo_sapiens.female')
    plt.figure()

    for i, key in enumerate(keys):
        di = pd.Series(data[key])
        ni = matplotlib.colors.Normalize()
        cmap = matplotlib.colormaps[colors[i]]

        ni.autoscale(di)
        dfs.append(di)
        norms.append(ni)

        ax = plt.subplot(gs[i, 0]) # row i, col 0
        ax.set_xlabel(key)
        ax.set_ylabel('organ')

        di.plot(kind='barh', ax=ax, color=colors[i][:-1])
        plt.colorbar(matplotlib.cm.ScalarMappable(norm=ni, cmap=cmap),  ax=ax, label='rel exp')
        gram.highlight_tissues(di.to_dict(), cmap=cmap, norm=ni)
        gram.to_matplotlib(ax=plt.subplot(gs[:, 1])) # span all rows, col 1

    plt.subplots_adjust(bottom=0.05, top=0.95, hspace=0.3)
    plt.savefig('plot.png', dpi=200)


def main():
    parser = argparse.ArgumentParser(prog='Anatamogram Script', description='Creates anatamograms')
    parser.add_argument("-i", "--input", required=True)
    data = load_data(parser)
    create_plot(data)

if __name__ == "__main__":
    main()