class BlastHit:
    '''
    Create BlastHit Class
    '''
    def __init__(self, Tr_ID, SP_ID, ident, mis):
        self.TranscriptID = Tr_ID
        self.SwissProtID = SP_ID
        self.identity = ident
        self.mismatch = mis

    def __lt__(self, other):
        '''
        compares the mismatch attribute between this instance (self) and another instance (other)
        '''
        return self.mismatch < other.mismatch

    def __repr__(self):
        return '{} {} {} {}'.format(self.TranscriptID, self.SwissProtID, self.identity, self.mismatch)

    def good_match(self):
        '''
        method that returns whether the hit is a really good match (e.g. >95 identity)
        '''
        return self.identity > 95

