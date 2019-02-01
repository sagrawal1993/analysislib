"""

This function will provide sorted score, index list of vectors.
For different distance metrics we could use
https://docs.scipy.org/doc/scipy-0.14.0/reference/spatial.distance.html#module-scipy.spatial.distance
"""

def closer_to_centroid(vector_list, distance, normalize=True):
    """
    This will get the score as the
    :param vector_list:
    :type vector_list:
    :return:
    :rtype:
    """

    if len(vector_list) == 0:
        return []
    centroid = sum(vector_list)/len(vector_list)
    score_index = []
    sum_score = 0.0
    for i, vector in enumerate(vector_list):
        score = distance(vector, centroid)
        sum_score += score
        score_index.append(score, i)
    score_index.sort(reverse=True)
    if normalize and sum_score > 0:
        for score_tuple in score_index:
            score_tuple[0] /= sum_score
    return score_index


def closer_to_given_vector(vector_list, representative, distance, normalize=True):
    """
    This will choose the vector closed to the given vector
    :param vector_list:
    :type vector_list:
    :param representative:
    :type representative:
    :param distance:
    :type distance:
    :param normalize:
    :type normalize:
    :return:
    :rtype:
    """
    if len(vector_list) == 0:
        return []
    score_index = []
    sum_score = 0.0
    for i, vector in enumerate(vector_list):
        score = distance(vector, representative)
        sum_score += score
        score_index.append(score, i)
    score_index.sort(reverse=True)
    if normalize and sum_score > 0:
        for score_tuple in score_index:
            score_tuple[0] /= sum_score
    return score_index
