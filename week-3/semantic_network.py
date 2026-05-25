import json
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

with open("knowledge_base.json") as f:
    kb = json.load(f)

G = nx.DiGraph()

diseases = [r["diagnosis"] for r in kb["rules"]]
G.add_nodes_from(["Patient"], type="patient")
G.add_nodes_from(diseases, type="disease")
G.add_nodes_from([s.title() for s in kb["symptoms"]], type="symptom")

for s in kb["symptoms"]:
    G.add_edge("Patient", s.title(), label="has")

for rule in kb["rules"]:
    for c in rule["conditions"]:
        G.add_edge(c.title(), rule["diagnosis"], label="indicates")

color_map = {
    "patient": "#4A90D9",
    "symptom": "#F5A623",
    "disease": "#D0021B",
}

node_colors = []
for node in G.nodes():
    if node == "Patient":
        node_colors.append(color_map["patient"])
    elif node in diseases:
        node_colors.append(color_map["disease"])
    else:
        node_colors.append(color_map["symptom"])

plt.figure(figsize=(14, 9))
pos = nx.spring_layout(G, seed=42, k=2)
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1800, alpha=0.9)
nx.draw_networkx_labels(G, pos, font_size=8, font_weight="bold")
nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=15, edge_color="#555", alpha=0.6)

legend = [
    mpatches.Patch(color=color_map["patient"], label="Patient"),
    mpatches.Patch(color=color_map["symptom"], label="Symptom"),
    mpatches.Patch(color=color_map["disease"], label="Disease"),
]
plt.legend(handles=legend, loc="upper left")
plt.title("Semantic Network — Medical Expert System", fontsize=13)
plt.axis("off")
plt.tight_layout()
plt.savefig("semantic_network.png", dpi=150)
print("Saved semantic_network.png")
