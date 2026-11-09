import csv
import collections # count how many times each class is predicted - Counter
from pathlib import Path # messy path naming handling
import matplotlib # to draw the figures
matplotlib.use('Agg') # to avoid the picture window - save picture to files

import matplotlib.pyplot as plt # short command

# anchor paths to this file, so output always lands in THIS folder no matter where you run it
repo = Path(__file__).resolve().parents[2] # AI-VIS/
root = repo / "phase1-Ai/split_preprocess-train" # our teams saved results (read-only)
out  = Path(__file__).resolve().parent # YOUR folder: phase1_ai_pair/trust_confidence
(out/"figures").mkdir(parents=True, exist_ok=True) # create the folder if not exist

def rows(p): # reading the csv file and return the rows
    with open(p, newline='') as f:
        return list(csv.DictReader(f))

T = "visualizations and transforms"
base = rows(root/"base results and setup/test_set_merged.csv") # to load base(unchanged image) result first

cond = { # keep all conditions in a dictionary for easy access
    "normal":base, # normal results on table
    "black&white":rows(root/T/"test_results_black_and_white.csv"), # black&white results on table
    "brightness":rows(root/T/"test_results_brightness_raised.csv"), # brightness results on table
    "invert" : rows(root/T/"test_results_color_inverted.csv"), # invert results on table
    "flip90" : rows(root/T/"test_results_flipped_90.csv"), # flip results on table
    "fliphorizontal" : rows(root/T/"test_results_flipped_horizontal.csv"), # flip results on table
    "flipupdown" : rows(root/T/"test_results_flipped_upside_down.csv"), # flip results on table
}

def acc(rs):
    return sum(r["correct"]=="True" for r in rs)/len(rs) # count the correct ans and divide by total

names = list(cond) # get all the conditions names
vals = [acc(cond[n]) * 100 for n in names] # get the accuracy for each condition

plt.figure(figsize=(8, 4)) # set the figure size
plt.bar(names, vals, color='skyblue') # draw the bar chart
plt.ylabel("correct %")
plt.ylim(0, 100) # set the y limit
plt.title("correct % : normal vs changed_images") # set the title
plt.xticks(rotation=30, ha='right') # rotate the x labels for better visibility
plt.tight_layout() # auto-adjust the layout to fit everything nicely
plt.savefig(out/"figures"/"fig1_accuracy.png", dpi=150) # save the figure to file
plt.close() # close the figure to free memory

ths = [0.5, 0.7, 0.8, 0.9, 0.95, 0.99] # we test thresholds for confidence cut-offs (keep ontly ans >= each val)

def curve(rs): # comput correct % for each threshold
    xs, ys = [], [] # collect the cut-off threshold and the corresponding correct % y here
    for t in ths: # for each threshold
        k = [r for r in rs if float(r["confidence"]) >= t] # keep only the ans with confidence >= threshold
        if k: # if no ans pass cut-off, we skip this threshold
            xs.append(t) # record this cut-off so x-axis has it
            ys.append(sum(r["correct"]=="True" for r in k)/len(k)*100) # compute the correct % among kept ans
    return xs, ys # return the collected values


plt.figure(figsize=(7, 4)) # start the trust curve picture
for lab in ["normal", "fliphorizontal", "flipupdown"]: # to draw those 3 lines
    x, y = curve(cond[lab]) # get the cut=offs and correcet % for this condition
    plt.plot(x, y, marker='o', label=lab) # draw the conditions line with dots and name for the legend
plt.xlabel("keep only answers with confidence >= threshold") # explain what horizontal axis means and x label
plt.ylabel("correct % of kept") # explain what vertical axis means and y label
plt.ylim(0, 100) # set the vertical axis limit to 0-100%
plt.title("can confidence warn us") # what the chart answers
plt.legend() # show the legend to explain which line is which condition
plt.grid(alpha=0.3) # add a light grid to help read the chart
plt.tight_layout() # auto-adjust the layout to fit everything nicely
plt.savefig(out/"figures"/"fig2_trust_curve.png", dpi=150)
plt.close() # close the figure to free memory

fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharey=True) # put the 2 charts side by side normal vs side flip with a shared y-axis

for ax, lab in zip(axes, ["normal", "fliphorizontal"]): # loops over 2 axis and their names to fill both charts per condition
    rs = cond[lab] # picks this condition's results
    # build the list right of those confidences
    right = [float(r["confidence"]) for r in rs if r["correct"]=="True"] # collect the confidence of correct ans
    wrong = [float(r["confidence"]) for r in rs if r["correct"]!="True"] # collect the confidence of wrong ans
    ax.hist([right, wrong], bins=20, color=['green', 'red'], label=["correct", "wrong"]) # draw the histogram of both groups so we can see how much their confidence overlap
    ax.set_title(lab) # set the title for this chart
    ax.set_xlabel("confidence") # set the x label for this chart
axes[0].set_ylabel("count") # set the y label for this chart
axes[0].legend() # show the legend to explain which color is which group
plt.tight_layout() # auto-adjust the layout to fit everything nicely
plt.savefig(out/"figures"/"fig3_confidence_histogram.png", dpi=150)
plt.close() # close the figure to free memory

classes = ["call", "dislike", "fist", "four", "like"] # the 5 classes we have
def dist(rs): # count how often ecah class is predicteed
    c = collections.Counter(r["pred_label"] for r in rs) # count how many times each class is predicted
    return [c.get(k, 0) for k in classes] # return the counts in the order of classes list - 0 if class was never predicted

fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharey=True) # put the 2 charts side by side normal vs side flip with a shared y-axis
for ax, lab in zip(axes, ["normal", "fliphorizontal"]): # loops over 2 axis and their names to fill both charts per condition
    ax.bar(classes, dist(cond[lab]), color='skyblue') # draw the bar chart of class distribution for this conditiona
    ax.set_title(lab) # set the title for this chart
    ax.set_ylabel("predicted_count") # set the y label for this chart
plt.tight_layout() # auto-adjust the layout to fit everything nicely
plt.savefig(out/"figures"/"fig4_predictions.png", dpi=150)
plt.close() # close the figure to free memory

def kept(rs, t): # a small tool that reports how many we keep and how many of those are correct at a confidence cut off t.
    k = [r for r in rs if float(r["confidence"]) >= t] # keep only the ans with confidence >= threshold
    if not k: # if no ans pass cut-off, we skip this threshold
        return 0, 0 # return 0 kept and 0 correct
    return len(k)/len(rs), sum(r["correct"]=="True" for r in k)/len(k) # return 1, the number of kept ans and 2, how many of those are correct

covN, accN = kept(base, 0.9) # for normal condition, how many we keep and how many of those are correct at confidence cut-off 0.9
covF, accF = kept(cond["fliphorizontal"], 0.9) # for side flip condition, how many we keep and how many of those are correct at confidence cut-off 0.9

summary = {n: round(acc(cond[n])*100, 1) for n in cond} # build a small table of summary of correct % for each condition. map each comdition name to its accuracy rounded to 1 decimal place
print("accuracy %", summary) # print the summary table

print("normal sure>=0.9: coverage %.2f acc %.1f%%" % (covN, accN * 100)) # print the coverage and accuracy with 2/1 decimals - show how much the model keeps and how right it is
print("flip   sure>=0.9: coverage %.2f acc %.1f%%" % (covF, accF * 100)) # print the coverage and accuracy with 2/1 decimals - show how much the model keeps and how right it is - for side flip images
text = [
    "# AI pair - Phase I : Trust in confidence", # Title line of findings.md
    "",
    "- Normal correct: %s%% | side flip: %s%%" % (summary["normal"], summary["fliphorizontal"]), # put 2 main accuracy numbers into file
    "- Sure(>=90%%) normal right: %.1f%% | after flip right: %.1f%%" % (accN * 100, accF * 100),
    "- Means: confidence is not a safe warning signal when images change.",
    "- Not proven: which pixels cause it (Phase II).",
]

(out / "findings.md").write_text("\n".join(text)+ "\n")

print("WROTE", out)
