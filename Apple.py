class person():
    def __init__(self):
        self.apple = 10
    def __str__(self):
        return f'The value is : {self.apple}'
    def __len__(self):
        return self.apple
