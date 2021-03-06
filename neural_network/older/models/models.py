class Network:
    """Base class to create model"""
    
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_prime = None
    
    # Adds a layer
    def add(self, layer):
        self.layers.append(layer)
    
    # Specifies what loss function to use
    def use(self, loss, loss_prime):
        self.loss = loss
        self.loss_prime = loss_prime
    
    # Predictions
    def predict(self, input_data):
        samples = len(input_data)
        result = []
        
        # predictions for each sample loop (thru forward prop)
        for i in range(samples):
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)
        return result
    
    # Trains model    
    def fit(self, x_train, y_train, epochs, learning_rate):
        samples = len(x_train)
        
        # training for each sample loop (# of epoch times)
        for i in range(epochs):
            err = 0
            for j in range(samples):
                output = x_train[j]
                for layer in self.layers:
                    output = layer.forward_propagation(output)
                    
                err += self.loss(y_train[j], output)
                
                error = self.loss_prime(y_train[j], output)
                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error, learning_rate)
                    
                err /= samples
                print(f'epoch {i+1}/{epochs}; error={err}')