import numpy as np
from collections import defaultdict
from scipy.sparse import dok_matrix

data = np.load("../user_movie_rating.npy")


# this only takes 0:30, but may takes more
def create_hashmap(data):
    max_mid = np.max(data[:, 1])
    hashmap = defaultdict(list)

    for uid, mid, score in data:
        if uid not in hashmap:
            hashmap[uid] = np.zeros(max_mid)
            hashmap[uid][mid - 1] = score
        else:
            hashmap[uid][mid - 1] = score
    return hashmap


hashmap = create_hashmap(data)


# need check banding technique
def calculate_Jaccard_Similarity(hashmap, user_1, user_2):
    set_user1 = set(np.nonzero(hashmap[user_1])[0])
    set_user2 = set(np.nonzero(hashmap[user_2])[0])
    return len(set_user1 & set_user2) / len(set_user1 | set_user2)


print(
    "Jaccard Simularity of user 1 and user 2 = {}".format(
        calculate_Jaccard_Similarity(hashmap, 1, 2)
    )
)
