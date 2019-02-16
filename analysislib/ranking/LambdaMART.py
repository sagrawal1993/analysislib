import pyltr

class LambdaMART:
    def __init__(self, metric="ndcg"):
        metric = pyltr.metrics.NDCG(k=10)
        self.model = pyltr.models.LambdaMART(
            metric=metric,
            n_estimators=1000,
            learning_rate=0.02,
            max_features=0.5,
            query_subsample=0.5,
            max_leaf_nodes=10,
            min_samples_leaf=64,
            verbose=1,
        )

    def fit(self, X, y, qid):
        self.model.fit(X,y,qid)
        return

    def predict(self, X):
        return self.model.predict(X)


# import random
# lm = LambdaMART()
# count = 10
# qid = [1] * count
# predict = [random.randrange(1,5) for i in range(count)]
# vector = [ random.sample(range(20, 50),10) for i in range(count)]
# print(predict)
# print(vector)
# print(qid)
# lm.fit(vector, predict, qid)
# x = lm.predict([random.sample(range(20, 50), 10) for i in range(count)])
# print(x)