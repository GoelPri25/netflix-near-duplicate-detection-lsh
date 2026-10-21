import numpy as np
from collections import defaultdict
from scipy.sparse import dok_matrix

data = np.load("../user_movie_rating.npy")

# this method takes 4:30
mid_map = {mid: idx for idx, mid in enumerate(np.unique(data[:, 1]))}
max_mid = np.max(data[:, 1])
hashmap = defaultdict(lambda: dok_matrix((1, max_mid)))
for uid, mid, score in data:
    movie_idx = mid_map[mid]
    hashmap[uid][0, movie_idx] = score


# for sparse
def calculate_Jaccard_Similarity(hashmap, user_1, user_2):
    set_user1 = set(hashmap[user_1].nonzero()[1])
    set_user2 = set(hashmap[user_2].nonzero()[1])
    return len(set_user1 & set_user2) / len(set_user1 | set_user2)


print(
    "Jaccard Simularity of user 1 and user 2 = {}".format(
        calculate_Jaccard_Similarity(hashmap, 1, 2)
    )
)
