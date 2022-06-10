import pandas as pd
from sklearn.neighbors import NearestNeighbors


class KNN:
    def get_neighbors(self, encoded_dataframe_by_destination_job, encoded_user_input, original_df_by_destination_job, k_for_knn):
        nbrs = NearestNeighbors(n_neighbors=k_for_knn, algorithm='auto', metric='euclidean').fit(encoded_dataframe_by_destination_job)
        _, indices = nbrs.kneighbors(encoded_user_input)

        neighbors_df = pd.DataFrame()

        for i in indices:
            neighbors_df = neighbors_df.append(original_df_by_destination_job.loc[i, :])
        return neighbors_df