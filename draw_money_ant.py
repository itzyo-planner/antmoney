import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Ellipse, FancyArrowPatch, Arc
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(7, 9), facecolor='#1a2a1a')
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('#1a2a1a')

# === BODY ===
# Abdomen
abdomen = Ellipse((5, 3.2), 3.4, 4.5, color='#2d5a1b', zorder=3)
ax.add_patch(abdomen)
abdomen_shine = Ellipse((4.2, 4.2), 1.0, 1.5, color='#4a8a2a', zorder=4, alpha=0.4)
ax.add_patch(abdomen_shine)

# $ sign on abdomen
ax.text(5, 3.2, '$', fontsize=28, ha='center', va='center',
        color='#ffd700', fontweight='bold', zorder=6, alpha=0.9)

# Thorax
thorax = Ellipse((5, 7), 2.0, 1.8, color='#2d5a1b', zorder=3)
ax.add_patch(thorax)

# Head
head = Ellipse((5, 9.0), 2.2, 2.0, color='#2d5a1b', zorder=3)
ax.add_patch(head)

# === EYES ===
eye_l = Ellipse((4.1, 9.4), 0.5, 0.5, color='#ffd700', zorder=5)
eye_r = Ellipse((5.9, 9.4), 0.5, 0.5, color='#ffd700', zorder=5)
ax.add_patch(eye_l)
ax.add_patch(eye_r)
pupil_l = Ellipse((4.12, 9.38), 0.22, 0.22, color='#1a1a1a', zorder=6)
pupil_r = Ellipse((5.92, 9.38), 0.22, 0.22, color='#1a1a1a', zorder=6)
ax.add_patch(pupil_l)
ax.add_patch(pupil_r)
# Gold glint
glint_l = Ellipse((4.05, 9.5), 0.08, 0.08, color='white', zorder=7)
glint_r = Ellipse((5.85, 9.5), 0.08, 0.08, color='white', zorder=7)
ax.add_patch(glint_l)
ax.add_patch(glint_r)

# === ANTENNAE ===
ax.plot([4.3, 2.8, 2.0], [9.9, 11.4, 12.6], color='#4a8a2a', linewidth=2.8,
        solid_capstyle='round', zorder=3)
ax.plot([5.7, 7.2, 8.0], [9.9, 11.4, 12.6], color='#4a8a2a', linewidth=2.8,
        solid_capstyle='round', zorder=3)
# Antenna tips (coin-shaped)
tip_l = plt.Circle((2.0, 12.6), 0.28, color='#ffd700', zorder=5)
tip_r = plt.Circle((8.0, 12.6), 0.28, color='#ffd700', zorder=5)
ax.add_patch(tip_l)
ax.add_patch(tip_r)
ax.text(2.0, 12.6, '$', fontsize=7, ha='center', va='center', color='#1a1a1a', fontweight='bold', zorder=6)
ax.text(8.0, 12.6, '$', fontsize=7, ha='center', va='center', color='#1a1a1a', fontweight='bold', zorder=6)

# === LEGS (6) ===
leg_color = '#4a8a2a'
lw = 2.4
# Front
ax.plot([4.1, 2.3, 1.2], [7.3, 6.5, 5.0], color=leg_color, linewidth=lw, solid_capstyle='round', zorder=2)
ax.plot([5.9, 7.7, 8.8], [7.3, 6.5, 5.0], color=leg_color, linewidth=lw, solid_capstyle='round', zorder=2)
# Middle
ax.plot([4.0, 2.0, 1.0], [6.8, 5.6, 4.4], color=leg_color, linewidth=lw, solid_capstyle='round', zorder=2)
ax.plot([6.0, 8.0, 9.0], [6.8, 5.6, 4.4], color=leg_color, linewidth=lw, solid_capstyle='round', zorder=2)
# Back
ax.plot([4.2, 2.4, 1.5], [6.2, 4.8, 3.5], color=leg_color, linewidth=lw, solid_capstyle='round', zorder=2)
ax.plot([5.8, 7.6, 8.5], [6.2, 4.8, 3.5], color=leg_color, linewidth=lw, solid_capstyle='round', zorder=2)

# === MANDIBLES holding coins ===
ax.plot([4.1, 3.2, 2.7], [8.2, 7.7, 7.0], color='#4a8a2a', linewidth=2.8, solid_capstyle='round', zorder=4)
ax.plot([5.9, 6.8, 7.3], [8.2, 7.7, 7.0], color='#4a8a2a', linewidth=2.8, solid_capstyle='round', zorder=4)
# Coins in mandibles
coin_l = plt.Circle((2.5, 6.7), 0.38, color='#ffd700', zorder=5)
coin_r = plt.Circle((7.5, 6.7), 0.38, color='#ffd700', zorder=5)
ax.add_patch(coin_l)
ax.add_patch(coin_r)
ax.text(2.5, 6.7, '$', fontsize=9, ha='center', va='center', color='#1a1a1a', fontweight='bold', zorder=6)
ax.text(7.5, 6.7, '$', fontsize=9, ha='center', va='center', color='#1a1a1a', fontweight='bold', zorder=6)

# === FLOATING COINS ===
for cx, cy, s in [(1.5, 9.5, 11), (8.5, 8.5, 9), (1.0, 5.5, 8), (9.0, 4.5, 10)]:
    coin = plt.Circle((cx, cy), 0.32, color='#ffd700', zorder=2, alpha=0.7)
    ax.add_patch(coin)
    ax.text(cx, cy, '$', fontsize=s, ha='center', va='center',
            color='#1a2a1a', fontweight='bold', zorder=3, alpha=0.7)

# === TITLE ===
ax.text(5, 13.3, 'ant money_bot', fontsize=14, ha='center', va='center',
        color='#ffd700', fontweight='bold', fontfamily='DejaVu Sans')
ax.text(5, 0.4, '@antmoney_bot', fontsize=10, ha='center', va='center',
        color='#4a8a2a', fontfamily='DejaVu Sans')

plt.tight_layout()
plt.savefig('C:/Users/kajjoo/.blnk/workspace/c3pt0i0c/money_ant.png',
            dpi=150, bbox_inches='tight', facecolor='#1a2a1a')
print("saved!")
