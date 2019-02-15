from concurrent.futures import ThreadPoolExecutor

class AbstracSearchOptimizer:
    def maximize(self, cost_function, args):
        pass

    def minimize(self, cost_function, args):
        pass

    def traverse_search_space(self, func, args):
        pass

class GridSearch:

    def __init__(self, param_min, param_max, step_size, thread=True):
        if len(param_max) != len(param_min):
            print("Unequal number of parameters")
        self.num_param = len(param_min)
        self.param_min = param_min
        self.param_max = param_max
        self.step_size = step_size
        self.thread = thread

    def maximize(self, cost_function, args):
        if self.num_param == 2:
            return self.__2_paramterter_maximum(cost_function, args)
        return None

    def traverse_search_space(self, cost_function, args):
        if self.num_param == 2:
            return self.__traverse_grid_2_param(cost_function, args)
        return None

    def __traverse_grid_2_param(self, cost_function, args):
        if self.thread:
            executor = ThreadPoolExecutor(max_workers=15)
            future_result = []
        full_map = {}
        param_a = self.param_min[0]
        while param_a <= self.param_max[0]:
            if str(param_a) not in full_map:
                full_map[str(param_a)] = {}
            param_b = self.param_min[1]
            while param_b <= self.param_max[1]:
                if self.thread:
                    th_param = {}
                    th_param['func'] = cost_function
                    th_param['param'] = [param_a, param_b]
                    th_param['args'] = args
                    future = executor.submit(self.__traverse_multithread, th_param)
                    future_result.append(future)
                else:
                    full_map[str(param_a)][str(param_b)] = cost_function([param_a, param_b], args)
                param_b += self.step_size
                print(param_a, param_b)
            param_a += self.step_size

        if self.thread:
            for future in future_result:
                param, map = future.result()
                full_map[str(param[0])][str(param[1])] = map
        return full_map

    def __traverse_multithread(self, param_map):
        func = param_map['func']
        param = param_map['param']
        args = param_map['args']
        map = func(param, args)
        return param, map

    def __2_paramterter_maximum(self, cost_function, args):
        param_a = self.param_min[0]
        param_b = self.param_min[1]
        max_value = cost_function([param_a, param_b], args)
        max_a = param_a
        max_b = param_b
        while param_a <= self.param_max[0]:
            param_b = self.param_min[1]
            while param_b <= self.param_max[1]:
                value = cost_function([param_a, param_b], args)
                if value > max_value:
                    max_value = value
                    max_a = param_a
                    max_b = param_b
                    print(max_a, max_b, max_value)
                param_b += self.step_size
            param_a += self.step_size
        return (max_a, max_b, max_value)

    def __2_paramterter_minimum(self, cost_function, args):
        param_a = self.param_min[0]
        param_b = self.param_min[1]
        min_value = cost_function([param_a, param_b], args)
        min_a = param_a
        min_b = param_b
        while param_a <= self.param_max[0]:
            param_b = self.param_min[1]
            while param_b <= self.param_max[1]:
                value = cost_function([param_a, param_b], args)
                if value < min_value:
                    min_value = value
                    min_a = param_a
                    min_b = param_b
                param_b += self.step_size
            param_a += self.step_size
        return (min_a, min_b, min_value)


    def minimize(self, cost_function, args):
        if self.num_param == 2:
            return self.__2_paramterter_minimum(cost_function, args)
        return
