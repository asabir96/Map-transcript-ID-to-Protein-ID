class Matrix:
    '''
    Create Matrix class
    '''
    def __init__(self, exprs):
        self.expressions = exprs

    def __repr__(self):
        return '{}'.format(self.expressions)

    def __iter__(self):
        '''
        Method to iterate through the 'expressions' attribute
        '''
        for item in self.expressions:
            yield item