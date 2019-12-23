class Blast:
    '''
    Create Blast Class
    '''
    def __init__(self, hits):
        self.hits = hits

    def __repr__(self):
        return '{}'.format(self.hits)

    def __iter__(self):
        '''
        Method to iterate through the 'hits' attribute
        '''
        for item in self.hits:
            yield item