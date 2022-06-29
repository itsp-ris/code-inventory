import argparse as ap
import platform
import numpy as np

def read_datafile(fname, attribute_data_type = 'integer'):
    inf = open(fname,'r')
    lines = inf.readlines()
    inf.close()
    #--
    X = []
    Y = []
    for l in lines:
        ss=l.strip().split(',')
        temp = []
        for s in ss:
            if attribute_data_type == 'integer':
                temp.append(int(s))
            elif attribute_data_type == 'string':
                temp.append(s)
            else:
                print("Unknown data type")
                exit()
        X.append(temp[:-1])
        Y.append(int(temp[-1]))
    return X, Y

#===
class DecisionTree :
    def __init__(self, split_random, depth_limit, curr_depth=0, default_label=1, minSampleSz=3):
        '''
        function creates an object of type DecisionTree
        precondition:
        :param: split_random: boolean input to indicate splitting rules
                depth_limit: the maximum depth of the tree allowed
                minSampleSz: the minimum number of examples to stop splitting
        postcondition:
        '''
        self.split_random = split_random # if True splits randomly, otherwise splits based on information gain
        self.maxDepth = depth_limit
        self.minSampleSz = minSampleSz

    def _classify(self, labels):
        '''
        function classify based on the label with the most number of examples
        precondition:
        :param: labels: array of labels of examples
        postcondition:
        return: the label the examples is classified into
        '''
        uniqueLabels, count = np.unique(labels, return_counts=True)
        return uniqueLabels[count.argmax()]

    def calculateEntropy(self, splitData, labels):
        '''
        function calculates entropy of positive/negative examples
        precondition:
        :param: splitData: examples
                labels: array of labels of examples
        postcondition:
        return: the positive/negative examples entropy
        '''
        _, count = np.unique(labels[splitData], return_counts=True)
        total = sum(count)
        probabilities = count / total
        return -sum(probabilities * np.log2(probabilities))

    def calculateOverallEntropy(self, left, right, labels):
        '''
        function calculates total entropy
        precondition:
        :param: left: index of negative examples in the whole data
                right: index of positive examples in the whole data
                labels: array of labels of examples
        postcondition:
        return: the total entropy
        '''
        nLeft = len(left)
        nRight = len(right)
        n = nLeft + nRight

        pLeft = nLeft / n
        pRight = nRight / n

        return (pLeft * self.calculateEntropy(left, labels)
                + pRight * self.calculateEntropy(right, labels))

    def _split(self, data, splitFeature, splitValue):
        '''
        function splits examples to positive or negative examples
        precondition:
        :param: data: examples
                splitFeature: the feature to split on
                splitValue: the value of the feature to split on
        postcondition:
        return: index of the positive and negative examples in the whole data
        '''
        featureValues = data[:, splitFeature]
        left = np.where(featureValues <= splitValue)
        right = np.where(featureValues > splitValue)
        return left, right

    def _chooseBestSplit(self, data, potentialSplits, labels):
        '''
        function choose the best feature and value of the feature to split on from all potential splits
        precondition:
        :param: data: all examples
                potentialSplits: dictionary of possible splits
                labels: array of labels of all examples
        postcondition:
        return: the feature and value of the feature to split on
        '''
        bestSplitFeature, bestSplitValue = None, None
        min = 999
        for i in range(len(potentialSplits)):
            for value in potentialSplits[i]:
                left, right = self._split(data, i, value)
                current = self.calculateOverallEntropy(left, right, labels)
                # get the feature and value of the feature with the highest information gain
                if (current <= min):
                    min = current
                    bestSplitFeature = i
                    bestSplitValue = value

        return bestSplitFeature, bestSplitValue

    def _getPotentialSplits(self, data):
        '''
        function collects all potential splits
        precondition:
        :param: data: examples
        postcondition:
        return: the potential splits from a list of examples
        '''
        _, features = data.shape
        potentialSplits = {_: [] for _ in range(features)}

        for i in range(features):
            uniqueValues = np.unique(data[:, i])

            for j in range(len(uniqueValues) - 1):
                potentialValue = (uniqueValues[j] + uniqueValues[j + 1]) / 2
                potentialSplits[i] += [potentialValue]

        return potentialSplits

    def train(self, data, labels):
        '''
        function trains the tree
        precondition:
        :param: data: examples
                labels: array of labels of examples
        postcondition:
        return: the trained tree
        '''
        # base case
        isPure = True
        uniqueLabels = np.unique(labels)
        if len(uniqueLabels) > 1:
            isPure = False

        if len(data) <= self.minSampleSz or isPure or self.maxDepth <= 0:
            return self._classify(labels)

        # recursive case
        else:
            self.maxDepth -= 1
            potentialSplits = self._getPotentialSplits(data)
            bestSplitFeature, bestSplitValue = self._chooseBestSplit(data, potentialSplits, labels)
            left, right = self._split(data, bestSplitFeature, bestSplitValue)

            leftChild = self.train(data[left], labels[left])
            rightChild = self.train(data[right], labels[right])

            if leftChild != rightChild:
                condition = str(bestSplitFeature) + " <= " + str(bestSplitValue)
                subTree = {condition: [leftChild, rightChild]}
                return subTree
            else:
                return leftChild

    def predict(self, example, tree):
        '''
        function predicts the label of an example by running through the tree
        precondition:
        :param: example: example to be predicted on
                tree: decision tree to run on for prediction
        postcondition:
        return: the label of the example
        '''
        # base case
        if type(tree) != dict:
            return tree

        # recursive case
        else:
            key = list(tree.keys())[0]
            feature, _, value = key.split()
            if example[int(feature)] <= float(value):
                tree = tree[key][0]
            else:
                tree = tree[key][1]
            return self.predict(example, tree)


#===	   
def compute_accuracy(dt_classifier, X_test, Y_test, tree):
    numRight = 0
    for i in range(len(Y_test)):
        x = X_test[i]
        y = Y_test[i]
        if y == dt_classifier.predict(x, tree):
            numRight += 1
    return (numRight*1.0)/len(Y_test)

#===
def main():
    # create a parser object
    parser = ap.ArgumentParser()

    # specify what arguments will be coming from the terminal/commandline
    parser.add_argument("train_file_name", help="specifies the name of the train file", type=str)
    parser.add_argument("depth", help="specifies the maximum depth allowed for the decision tree", type=int)
    parser.add_argument("test_file_name", help="specifies the name of the test file", type=str)
    parser.add_argument("output_file_name", help="specifies the name of the output file", type=str)


    # get all the arguments
    arguments = parser.parse_args()

    # Extract the required arguments

    operating_system = platform.system()

    if operating_system == "Windows":
        train_file_name = arguments.train_file_name
        test_file_name = arguments.test_file_name
        output_file_name = arguments.output_file_name

    else:
        train_file_name = arguments.train_file_name
        test_file_name = arguments.test_file_name
        output_file_name = arguments.output_file_name

    depth = arguments.depth

    try:
        X_train, Y_train = read_datafile(train_file_name)
        X_test, Y_test = read_datafile(test_file_name)
        X_train, Y_train = np.array(X_train), np.array(Y_train)
        X_test, Y_test = np.array(X_test), np.array(Y_test)
        treeClassifer = DecisionTree(False, depth)
        tree = treeClassifer.train(X_train, Y_train)
        accuracy = compute_accuracy(treeClassifer, X_test, Y_test, tree)
        file_handle = open(output_file_name, 'w+')
        file_handle.write(str(accuracy))
    except FileNotFoundError:
        print("files are not present")
        return -1

#==============================================
#==============================================
if __name__ == "__main__":
    # print(DecisionTree.calculateEntropy())
    # print(DecisionTree.calculateOverallEntropy())
    import math
    s = (-6/12 * math.log(6/12, 2)) - (6/12 * math.log(6/12, 2))
    print(s)
    # print( -7.180 * 0.001 + (-3.445) * 0.1 + 359.766 * 1 + (-550.377) * 0.5 + 335.473 * 6 + (-0.302) * 400 + (-78.677) * 10 + (1496.067) + 3187.691)