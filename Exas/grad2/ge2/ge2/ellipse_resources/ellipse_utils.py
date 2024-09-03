import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import ellipse_perimeter

root = os.path.dirname(os.path.abspath(__file__))

PRECOMPUTED_DISTANCES = np.load(os.path.join(root, "precomputed_dist.npy"))
PRECOMPUTED_X0 = np.load(os.path.join(root, "precomputed_x0.npy"))
PRECOMPUTED_A = np.load(os.path.join(root, "precomputed_a.npy"))
PRECOMPUTED_B = np.load(os.path.join(root, "precomputed_b.npy"))
PRECOMPUTED_B_VOTES = np.load(os.path.join(root, "precomputed_b_votes.npy"))
PRECOMPUTED_ALPHA = np.load(os.path.join(root, "precomputed_alpha.npy"))
PRECOMPUTED_B_ACCUM = np.load(os.path.join(root, "precomputed_b_accum.npy"))

def get_dist_TEST(i,j):
    return PRECOMPUTED_DISTANCES[i, j]

def get_center_TEST(i,j):
    return PRECOMPUTED_X0[i, j]

def get_a_TEST(i,j):
    return PRECOMPUTED_A[i, j]

def get_orient_TEST(i,j):
    return PRECOMPUTED_ALPHA[i, j]

def get_b_accum_TEST(i,j):
    return PRECOMPUTED_B_ACCUM[i, j]

def get_best_b_with_vote_TEST(i,j):
    return PRECOMPUTED_B[i,j], PRECOMPUTED_B_VOTES[i, j]


def visualize_ellipses(image, ellipses):
    fig, ax = plt.subplots(1,1, figsize=(5,5))
    ax.imshow(image, cmap='gray')
    image_rgb = np.stack([image]*3, axis=-1)
    for ellipse in ellipses:
        [xc, yc], a, b, orientation = ellipse
        cy, cx = ellipse_perimeter(int(yc), int(xc), int(a), int(b), orientation)
        image_rgb[cy, cx] = (0, 0, 1)
        ax.imshow(image_rgb)
    return fig