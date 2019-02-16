
def getRanker(method_name, param_map={}):
    if method_name == "lambdaMART":
        from analysislib.ranking.LambdaMART import LambdaMART
        return LambdaMART(**param_map)
    return None

class AbstractRanker:
    def fit(self, vector_list, score, qid_list):
        pass

    def predict(self, vector_list):
        pass