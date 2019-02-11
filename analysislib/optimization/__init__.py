def getSearchOptimizer(method_name, parms_map={}):
    if method_name == "grid_search":
        from analysislib.optimization.SearchOptimizer import GridSearch
        return GridSearch(**parms_map)
    return None

