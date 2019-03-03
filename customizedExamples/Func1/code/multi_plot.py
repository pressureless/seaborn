import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
from itertools import repeat
import seaborn as sns
import matplotlib.patches as mpatches
from seaborn3 import categorical
from matplotlib.font_manager import FontProperties
from matplotlib import rc
from PIL import Image
import cStringIO

mpl.rcParams['figure.dpi']= 300
mpl.rcParams['axes.linewidth'] = 1.5
plt.rcParams["font.family"] = "Times New Roman"
# rc('font', weight='bold')



# rc('font',**{'family':'Times New Roman'})
# rc('text', usetex=True)
# plt.rcParams['text.latex.preamble'] = [r'\boldmath']
# plt.rcParams["font.size"] = 12
# plt.rc('text', usetex=True)
# plt.rcParams["font.family"] = "sans-serif"

def patch_violinplot(ax):
    from matplotlib.collections import PolyCollection
    # ax = plt.gca()
    index = 0
    for art in ax.get_children():
        if isinstance(art, PolyCollection):
            if index%2 == 0:
                #set red border
                art.set_edgecolor("#F0BCB9")
            else:
                #set blue border
                art.set_edgecolor("#BACCDC")
            index = index + 1


# mpl.rcParams['figure.subplot.top'] = 0.5

fig, axes = plt.subplots(2, 2, facecolor='white')
# fig.tight_layout(rect=[0, 0.03, 0.4, 0.5])
# fig.tight_layout()
# fig.subplots_adjust(left=0.4, right=0.6)
# plt.subplots_adjust(left=0, bottom=0, right=1, top=0.5, wspace=0, hspace=0)
# fig, axes = plt.subplots(2, 2, facecolor='white')
# fig.set_size_inches(10, 5)

fig.subplots_adjust(top=0.9, wspace=0.45, right=0.8)


space = 0.15

data_gE = pd.read_table("~/Downloads/data_gE.txt",sep=';')
data_Cp = pd.read_table("~/Downloads/data_Cp.txt",sep=';')
data_locE = pd.read_table("~/Downloads/data_locE.txt",sep=';')
data_Lp = pd.read_table("~/Downloads/data_Lp.txt",sep=';')
# ax = sns.violinplot(x="variable", y="value", hue="smoker", data=bb, palette="Pastel1",  size=3,
# patch_violinplot()



axes[0, 0].plot([-0.15, 0.15], [0.779, 0.779],color="#7A7A7A")
axes[0, 0].plot([-0.15, -0.15], [0.778, 0.78],color="#7A7A7A")
axes[0, 0].plot([0.15, 0.15], [0.778, 0.78],color="#7A7A7A")
axes[0, 0].text(0, 0.78, "***",horizontalalignment='center',color="#7A7A7A")
ax1 = categorical.violinplot(x="Type", y="Value", hue="Height", data=data_gE, palette="Pastel1",  size=3,
linewidth=3,  ax=axes[0, 0], width=0.35,scale_hue=True, scale="area")
ax1.legend().set_visible(False)
patch_violinplot(axes[0, 0])
# axes[0, 0].legend(loc=10)
axes[0, 0].set_ylabel(r'$\mathregular{E_{glob}}$',fontsize=15)
# axes[0, 0].set_ylabel(r'$\mathregular{E_{glob}}$',fontsize=15, fontweight='bold')
axes[0, 0].set_xlabel('')
axes[0, 0].set_xticks([-0.15, 0.15])
axes[0, 0].set_xticklabels([])
axes[0, 0].set_yticks(np.arange(0.68,0.81,0.03))

label = [r'$\mathregular{RSN_{spon}}$', r'$\mathregular{RSN_{remain}}$']
# label = [r'$RSN_{spon}$', r'RSN']
fake_handles = (mpatches.Patch(color="#F0BCB9"), mpatches.Patch(color="#BACCDC"))

ax1 = categorical.violinplot(x="Type", y="Value", hue="Height", data=data_Cp, palette="Pastel1",  size=3,
linewidth=3, scale="count", ax=axes[1, 0], width=0.3)
ax1.legend().set_visible(False)
patch_violinplot(axes[1, 0])
axes[1, 0].set_xlabel('')
axes[1, 0].set_ylabel(r'$\mathregular{C_w}$',fontsize=15)
# axes[1, 0].set_ylabel(r'$\mathregular{C_w}$',fontsize=15, fontweight='bold')
axes[1, 0].set_xlabel('')
axes[1, 0].set_xticks([-space, space])
axes[1, 0].set_xticklabels([])


ax1 = categorical.violinplot(x="Type", y="Value", hue="Height", data=data_locE, palette="Pastel1",  size=3,
linewidth=3, scale="count", ax=axes[0, 1], width=0.3)
ax1.legend().set_visible(False)
patch_violinplot(axes[0, 1])

font0 = FontProperties()
font = font0.copy()
font.set_family('Times New Roman')
# font.set_weight('bold')
font.set_size(15)

leg = axes[0, 1].legend(fake_handles, label,bbox_to_anchor=(1.02, 0.92),
           bbox_transform=plt.gcf().transFigure,prop=font)
leg.get_frame().set_edgecolor('w')
axes[0, 1].set_xlabel('')
axes[0, 1].set_ylabel(r'$\mathregular{E_{loc}}$',fontsize=15)
# axes[0, 1].set_ylabel(r'$\mathregular{E_{loc}}$',fontsize=15, fontweight='bold')
axes[0, 1].set_xlabel('')
axes[0, 1].set_xticks([-space, space])
axes[0, 1].set_xticklabels([])



axes[1, 1].plot([-space, space], [1.46, 1.46],color="#7A7A7A")
axes[1, 1].plot([-space, -space], [1.459, 1.461],color="#7A7A7A")
axes[1, 1].plot([space, space], [1.459, 1.461],color="#7A7A7A")
axes[1, 1].text(0, 1.461, "***",horizontalalignment='center',color="#7A7A7A")
ax1 = categorical.violinplot(x="Type", y="Value", hue="Height", data=data_Lp, palette="Pastel1",  size=3,
linewidth=3, scale="count", ax=axes[1, 1], width=0.3)
ax1.legend().set_visible(False)
patch_violinplot(axes[1, 1])
axes[1, 1].set_xlabel('')
axes[1, 1].set_ylabel(r'$L_w$',fontsize=15)
# axes[1, 1].set_ylabel(r'$\mathregular{L_w}$',fontsize=15)
# axes[1, 1].set_ylabel(r'$\mathregular{L_w}$',fontsize=15, fontweight='bold')
axes[1, 1].set_xticklabels([])
axes[1, 1].set_ylim(1.28,1.46)
axes[1, 1].set_yticks(np.arange(1.28,1.50,0.05))
axes[1, 1].set_xticks([-space, space])


# sns.despine()
# plt.savefig('gender____.png')
# plt.show()



png1 = cStringIO.StringIO()
fig.savefig(png1, format="png", dpi=300)
png2 = Image.open(png1)
png2.save("python_norm.tiff")
# png2.save("python_bold.tiff")
png1.close()
