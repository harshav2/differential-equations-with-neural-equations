import numpy as np

def sigmoid(x):
    return 1/(1+(np.exp(-x)))

class ForwardProp:
    def forward_prop(self, x):
        z1 = np.dot(self.input_weights, x)
        a1 = sigmoid(z1)

        current_a = a1
        self.intermediary_z = []
        self.intermediary_z.append(z1)

        for i in range(len(self.hidden_weights)):
            weights = self.hidden_weights[i]
            bias=self.hidden_bias[i]

            current_z = np.dot(weights, current_a)+bias
            self.intermediary_z.append(current_z)

            current_a = sigmoid(current_z)
        
        for i, z in enumerate(self.intermediary_z):
            print(f"Layer {i+1} intermediary z:\n", z)
        
        output = sigmoid(np.dot(self.output_weights, current_a) + self.output_bias)
        print("Output:",output)
        
        return output