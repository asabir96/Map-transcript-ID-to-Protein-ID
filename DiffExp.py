class DiffExp:
    '''
    Create DiffExp Class
    '''
    def __init__(self, trans, dia_shift, hs, lg, pp):
        self.transcript = trans
        self.diauxicshift = dia_shift
        self.heatshock = hs
        self.plateauphase = pp
        self.logarithmicgrowth = lg

    def __repr__(self):
        return '{} {} {} {} {}'.format(self.transcript, self.diauxicshift, self.heatshock, self.logarithmicgrowth, self.plateauphase)

    def return_attribs(self):
        '''
        Method that returns the data sample attributes as a tuple
        '''
        return (self.diauxicshift, self.heatshock, self.logarithmicgrowth, self.plateauphase)
    
