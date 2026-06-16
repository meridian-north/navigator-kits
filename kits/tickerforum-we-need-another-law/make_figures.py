#!/usr/bin/env python3
"""Generate the 3 TickerForum legal-corpus figures (deterministic, from the index)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import csv, os

BG="#0c0f14"; PANEL="#141a22"; INK="#e8eef5"; MUT="#8da0b4"; LINE="#26303c"
WARN="#ff6b6b"; CAUTION="#ffb454"; WATCH="#7aa2ff"; ACC="#5db0ff"
plt.rcParams.update({"figure.facecolor":BG,"savefig.facecolor":BG,"text.color":INK,
    "axes.facecolor":PANEL,"axes.edgecolor":LINE,"xtick.color":MUT,"ytick.color":MUT,
    "font.family":"DejaVu Sans","font.size":11})
HERE=os.path.dirname(os.path.abspath(__file__))

# ---------- FIG 1: enforcement gap ----------
rows=[
 ("15 USC §2 — criminal cases (first ~80 yr)",100,WARN,"100+"),
 ("15 USC §2 — criminal cases 1977→2022",0,WARN,"0"),
 ("15 USC §2 — persons serving 10-yr terms",0,WARN,"0"),
 ("8 USC §1324 — officers/directors imprisoned",0,WARN,"≈0"),
 ("CPT/CMS mandate — antitrust actions brought",0,WARN,"0"),
 ("AICOA / app-store bills — enacted into law",0,WATCH,"0"),
]
fig,ax=plt.subplots(figsize=(10,5.2))
labels=[r[0] for r in rows]; vals=[r[1] for r in rows]; cols=[r[2] for r in rows]
y=range(len(rows))[::-1]
ax.barh(list(y),[100]*len(rows),color=PANEL,height=0.55)
ax.barh(list(y),vals,color=cols,height=0.55,alpha=0.88)
for yi,r in zip(y,rows):
    ax.text(max(r[1],2)+2,yi,r[3],va="center",ha="left",color=r[2],fontweight="bold",fontsize=12)
ax.set_yticks(list(y)); ax.set_yticklabels(labels,fontsize=10)
ax.set_xlim(0,118); ax.set_xticks([])
for s in ["top","right","bottom"]: ax.spines[s].set_visible(False)
ax.spines["left"].set_color(LINE)
ax.set_title("Enforcement Gap — law on the books vs. law in action",fontsize=14,fontweight="bold",pad=14,loc="left")
fig.text(0.012,0.02,"Sherman §2: 100+ criminal cases in first ~80 yr, none 1977→2022; revival cases (Zito 2022, fuel-truck 2024) ended in probation, not 10-yr terms.\nWARN = binding law, ~0 criminal use · WATCH = pending bill. Illustrative of the documented record, not a litigation tally. Not legal advice.",
    fontsize=8,color=MUT)
fig.subplots_adjust(left=0.40,right=0.96,top=0.88,bottom=0.16)
fig.savefig(f"{HERE}/fig1_enforcement_gap.png",dpi=150); plt.close(fig)

# ---------- FIG 2: one-law-leads-to-another chain ----------
fig,ax=plt.subplots(figsize=(10,4.6)); ax.set_xlim(0,10); ax.set_ylim(0,6); ax.axis("off")
ax.text(0.2,5.6,"ALREADY ILLEGAL · in force · ~0 criminal use",color=MUT,fontsize=10,fontweight="bold")
ax.text(5.7,5.6,'PROPOSED "ANOTHER LAW" · not enacted',color=MUT,fontsize=10,fontweight="bold")
left=["15 USC §2 — monopolize\n(felony, 1890)","15 USC §2 — same\n(app-store conduct)","15 USC §2 — same\n(ad-tech conduct)"]
right=["AICOA S.4746\n(2026)","Open App Markets\nS.2153 (2025)","AMERICA Act —\nad-tech (2025)"]
ys=[4.2,2.6,1.0]
for t,yy in zip(left,ys):
    ax.add_patch(FancyBboxPatch((0.2,yy),4.0,1.1,boxstyle="round,pad=0.04,rounding_size=0.12",
        fc=PANEL,ec=WARN,lw=1.6))
    ax.text(0.35,yy+0.72,t,fontsize=9.5,color=INK,va="center")
    ax.text(0.35,yy+0.18,"WARN · dormant criminal statute",fontsize=7.5,color=WARN,family="monospace")
for t,yy in zip(right,ys):
    ax.add_patch(FancyBboxPatch((5.7,yy),4.0,1.1,boxstyle="round,pad=0.04,rounding_size=0.12",
        fc=PANEL,ec=WATCH,lw=1.6))
    ax.text(5.85,yy+0.72,t,fontsize=9.5,color=INK,va="center")
    ax.text(5.85,yy+0.18,"WATCH · pending, not law",fontsize=7.5,color=WATCH,family="monospace")
for yy in ys:
    ax.add_patch(FancyArrowPatch((4.2,yy+0.55),(5.7,yy+0.55),arrowstyle="-|>",mutation_scale=16,
        color=WATCH,lw=1.8,connectionstyle="arc3,rad=0"))
ax.set_title('"We Need ANOTHER Law!" — each new bill traces back to an existing, lightly-enforced statute',
    fontsize=12.5,fontweight="bold",loc="left",color=INK,pad=10)
fig.text(0.012,0.02,"The post's thesis made visual: a dormant felony statute on the left, a fresh bill on the right, joined by a shared mechanism node. Not legal advice.",
    fontsize=8,color=MUT)
fig.subplots_adjust(left=0.02,right=0.98,top=0.9,bottom=0.1)
fig.savefig(f"{HERE}/fig2_one_law_chain.png",dpi=150); plt.close(fig)

# ---------- FIG 3: mechanism crossroads ----------
counts={}
with open(f"{HERE}/data/tickerforum_legal_index_v1.csv") as fh:
    for r in csv.DictReader(fh):
        for m in r["mechanism_nodes"].split("|"):
            counts[m]=counts.get(m,0)+1
items=sorted(counts.items(),key=lambda x:x[1])
fig,ax=plt.subplots(figsize=(10,5))
ax.barh([k for k,_ in items],[v for _,v in items],color=ACC,alpha=0.85,height=0.6)
for i,(k,v) in enumerate(items):
    ax.text(v+0.05,i,str(v),va="center",color=MUT,fontweight="bold")
ax.set_xlim(0,max(counts.values())+1); ax.set_xticks(range(0,max(counts.values())+2))
for s in ["top","right"]: ax.spines[s].set_visible(False)
ax.set_title("Mechanism Crossroads — where the post's claims cluster",fontsize=14,fontweight="bold",loc="left",pad=12)
fig.text(0.012,0.02,"Records touching each mechanism node across the index. antitrust_monopolization and criminal_enforcement are load-bearing; the CPT/CMS lane is the one where no private party can bring a charge.",
    fontsize=8,color=MUT)
fig.subplots_adjust(left=0.30,right=0.96,top=0.9,bottom=0.14)
fig.savefig(f"{HERE}/fig3_mechanism_crossroads.png",dpi=150); plt.close(fig)
print("figures written:",[f for f in os.listdir(HERE) if f.endswith(".png")])
