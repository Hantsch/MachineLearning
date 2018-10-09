import numpy
import scipy.special

class neuralNetwork:
    
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.input_nodes = inputnodes
        self.hidden_nodes = hiddennodes
        self.output_nodes = outputnodes

        self.learning_rate = learningrate

        self.weight_input_hidden = numpy.random.normal(0.0, pow(self.hidden_nodes, -0.5), (self.hidden_nodes, self.input_nodes))
        self.weight_hidden_output = numpy.random.normal(0.0, pow(self.output_nodes, -0.5), (self.output_nodes, self.hidden_nodes))

        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    def train():
        pass

    def query():
        pass