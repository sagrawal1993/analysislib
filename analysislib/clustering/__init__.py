from analysislib.clustering.ClusterEmbedding import  WeightedCentroid, Centroid

def getClusterEmbeddingFromPoints(method_name="centroid", param_map={}):
    if method_name == "weightedCentroid":
        return WeightedCentroid(param_map)
    return Centroid(param_map)

def getClustering(method_name="k-mean", param_map={}):
    if method_name is "k-mean":
        from sklearn.cluster.k_means_ import KMeans
        return KMeans(param_map)
    elif method_name is "dbscan":
        from sklearn.cluster import DBSCAN
        return DBSCAN(param_map)
    return None

def getClusterRepresentative(method_name="", param_map={}):
    return