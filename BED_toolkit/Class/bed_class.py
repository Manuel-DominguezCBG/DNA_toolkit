
'''
Read BED files and do basic checking

'''
import pandas as pd
import pyranges as pr

class Bed():
    '''
    '''

    def __init__(self,bed_data):
        '''
        '''
        self.bed_data = bed_data

    def read_bed(self):
        '''
        Read and convert data into pandas df
        '''
        return pd.read_csv(self,sep='\t', header=None)
        