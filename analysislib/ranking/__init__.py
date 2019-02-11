def getRanker(method_name, param_map={}):
    return None

class AbstractRanker:
    def fit(self, vector_list, score):
        pass

    def transform(self, vector_list):
        pass