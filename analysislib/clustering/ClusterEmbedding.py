import numpy as np

"""
This will contains code to create the representation of the cluster based on the points present in the cluster.
Consider all the vectors to be an numpy array.
"""

def getClusterEmbeddingFromPoints(method_name="centroid", param_map = {}):
    if method_name == "weightedCentroid":
        return WeightedCentroid()
    return Centroid()

class AbstractClusterEmbedding:
    def __init__(self):
        pass

    def getClusterRepresentation(self, vector_list, param_map={}):
        """

        :param vector_list: list of point's representation, which belongs to a cluster.
        :type vector_list: numpy array list
        :return:
        :rtype:
        """
        pass


class Centroid(AbstractClusterEmbedding):
    def __init__(self, vector_dimension):
        super.__init__()
        self.dim = vector_dimension

    def getClusterRepresentation(self, vector_list):
        emb = np.zeros(self.dim)
        for vec in vector_list:
            emb += vec
        if len(vector_list) != 0:
            emb /= len(vector_list)
        return emb

class WeightedCentroid(AbstractClusterEmbedding):
    def __init__(self, vector_dimension):
        super.__init__()
        self.dim = vector_dimension

    def getClusterRepresentation(self, vector_list, weighted_list):
        emb = np.zeros(self.dim)
        for i, vec in enumerate(vector_list):
            emb += vec * weighted_list[i]
        if len(vector_list) != 0:
            emb /= len(vector_list)
        return emb

