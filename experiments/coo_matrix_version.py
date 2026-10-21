import numpy as np
from collections import defaultdict
from scipy.sparse import coo_matrix

data = np.load("../user_movie_rating.npy")

user_ids = data[:, 0]
movie_ids = data[:, 1]
ratings = data[:, 2]

user_map = {uid: idx for idx, uid in enumerate(np.unique(user_ids))}
movie_map = {mid: idx for idx, mid in enumerate(np.unique(movie_ids))}

row_indices = np.array([user_map[uid] for uid in user_ids])
col_indices = np.array([movie_map[mid] for mid in movie_ids])

ratings_matrix = coo_matrix((ratings, (row_indices, col_indices)))

print("Sparse Matrix Shape:", ratings_matrix.shape)
print("Non-zero Entries:", ratings_matrix.nnz)
print("Matrix in Dense Format:\n", ratings_matrix.toarray())

num_users = len(np.unique(user_ids))
num_movies = len(np.unique(movie_ids))
num_hashmap = 100

hashes = [np.random.permutation(num_movies) for _ in range(num_hashmap)]
signature_matrix = np.zeros((num_hashmap, num_users))
