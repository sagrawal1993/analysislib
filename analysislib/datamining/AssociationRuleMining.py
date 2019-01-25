import numpy as np
from apyori import apriori

def getAssociationRuleMiner(method):
    return ApriyorAlgorithm()


class ApriyorAlgorithm:

    def getRule(self, records, min_support=0.0045, min_confidence=0.2, min_lift=3, max_length=3):
        self.association_rules = apriori(records, min_support=min_support, min_confidence=min_confidence, min_lift=min_lift, max_length=max_length)

        print(self.association_rules)
        for item in self.association_rules:

            print(item)
            # first index of the inner list
            # Contains base item and add item
            """
            pair = item[0]
            items = [x for x in pair]
            print("Rule: " + items[0] + " -> " + items[1])

            #second index of the inner list
            print("Support: " + str(item[1]))

            #third index of the list located at 0th
            #of the third index of the inner list

            print("Confidence: " + str(item[2][0][2]))
            print("Lift: " + str(item[2][0][3]))
            print("=====================================")
            """

        return self.association_rules
