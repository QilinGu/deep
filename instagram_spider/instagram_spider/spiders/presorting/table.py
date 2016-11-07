
class Table():
    '''
    Data structure description:
        - Very similar to an adjacency list
        - Has 'buckets' that are distributed in a Log Normal Distribution see
          [1] for more info, the reason for this distribution is outlined in
          experiments/number_statistics.ipynb
        - For example if the number of followers is 200 it'll be seperated into
          the bucket for values betweeen 195-205 (or something similar), while
          at the same time if the value was 200k it'll be in the bucket of
          150k-250k followers
    [1] http://mathworld.wolfram.com/LogNormalDistribution.html


    TODO in the future:
        - Use a hash table which will find the bucket based on the Log Normal
          Distribution (useful if the dataset is big enough – for now this is 
          good enough)


    Possible additions:
        - Increase the number of buckets when it gets too full to improve speed
    '''
    def __init__(mu, sigma, num_buckets):
        '''
        Initialize the table with num_buckets and distributed according to mu
        and sigma.
        '''
        pass

    def save(output_file):
        '''
        Save the data in order to a file given by output_file
        '''
        pass
