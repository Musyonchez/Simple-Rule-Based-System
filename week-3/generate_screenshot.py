import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import subprocess
import sys

inputs = [
    "fever, headache, fatigue",
    "cough, chest pain, fatigue",
    "sneezing, runny nose, sore throat",
    "vomiting, diarrhea, fatigue",
    "headache",
]

outputs = []
for inp in inputs:
    result = subprocess.run(
        [sys.executable, "main.py"],
        input=inp,
        capture_output=True,
        text=True,
    )
    lines = result.stdout.strip().split("\n")
    symptom_line = next((l for l in lines if l.startswith("Symptoms recorded:")), "")
    diag_line = next((l for l in lines if "condition:" in l or "No matching" in l), "")
    outputs.append((inp, symptom_line.strip(), diag_line.strip()))

lines = []
lines.append("=" * 52)
lines.append("          Medical Expert System")
lines.append("=" * 52)
for inp, symptoms, diagnosis in outputs:
    lines.append(f"\n> Input: {inp}")
    lines.append(f"  {symptoms}")
    lines.append(f"  {diagnosis}")
lines.append("\n" + "=" * 52)

text = "\n".join(lines)

fig, ax = plt.subplots(figsize=(9, 6))
ax.set_facecolor("#1e1e1e")
fig.patch.set_facecolor("#1e1e1e")
ax.text(
    0.02, 0.97, text,
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    fontfamily="monospace",
    color="#d4d4d4",
)
ax.axis("off")
plt.title("Sample Output — Medical Expert System", color="white", pad=10)
plt.tight_layout()
plt.savefig("screenshots/output.png", dpi=150, facecolor="#1e1e1e")
print("Saved screenshots/output.png")
