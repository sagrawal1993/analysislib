class GridSearch:

    def __init__(self, param_min, param_max, num_param, step_size):
        self.num_param = num_param
        self.param_min = param_min
        self.param_max = param_max
        self.step_size = step_size

    def maximize(self, cost_function, args):
        if self.num_param == 2:
            return self.__2_paramterter_maximum(cost_function, args)
        return None

    def __2_paramterter_maximum(self, cost_function, args):
        param_a = self.param_min[0]
        param_b = self.param_min[1]
        max_value = cost_function([param_a, param_b], args)
        max_a = param_a
        max_b = param_b
        while param_a <= self.param_max[0]:
            while param_b <= self.param_max[1]:
                value = cost_function([param_a, param_b], args)
                if value > max_value:
                    max_value = value
                    max_a = param_a
                    max_b = param_b
                param_b += self.step_size
            param_a += self.step_size
        return (max_a, max_b, value)

    def __2_paramterter_minimum(self, cost_function, args):
        param_a = self.param_min[0]
        param_b = self.param_min[1]
        min_value = cost_function([param_a, param_b], args)
        min_a = param_a
        min_b = param_b
        while param_a <= self.param_max[0]:
            while param_b <= self.param_max[1]:
                value = cost_function([param_a, param_b], args)
                if value < min_value:
                    min_value = value
                    min_a = param_a
                    min_b = param_b
                param_b += self.step_size
            param_a += self.step_size
        return (min_a, min_b, value)


    def minimize(self, cost_function, args):
        if self.num_param == 2:
            return self.__2_paramterter_minimum(cost_function, args)
        return

