import json
import node

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
        1. Increase the number of buckets when it gets too full to improve
           speed, would split the current buckets into these ranges.
           Eg: prev bucket range was 100-200, new buckets at 100-150 and 151-200
           traverse list and set element 150 to 'None' and set 151 to be the
           first element of the next bucket
    '''
    def __init__(mu, sigma, num_buckets):
        '''
        Initialize the table with num_buckets and distributed according to mu
        and sigma.
        '''
        self.mu = mu
        self.sigma = sigma
        self.buckets = []
        for i in range(num_buckets):
            self.buckets[i] = None
        pass

    # Helper Functions
    def compute_bucket(followers):
        '''
        Helper function
        Add to the given bucket
        - to make this a hash table, should how this function works

        Arguments:
            - followers: the number of followers to compute which bucket the
              node should be in
        Returns:
            - A pointer (or index) to the bucket that the node should be in
        '''
        pass

    def buckets(bucket):
        '''
        Abstraction that returns the bucket you want.
        Will make code calling it work regardless of data structure of the table
        of buckets

        Arguments:
            - bucket: the identifier of the buket (index or code, etc.)
        Returns:
            - the first node in that bucket (or 'None' if bucket is empty)
        '''
        return self.buckets[bucket]

    def add_to_bucket(node, bucket, followers=None):
        '''
        Helper function
        Adds the node to the given bucken in the correct order

        Arguments:
            - node: node to add
            - bucket: pointer (or index) to bucket
            - followers (optional)

        '''
        if followers == None: # if followers are not given beforehand
            followers = node.get_followers()

        if self.buckets(bucket) is None: # if bucket is empty
            self.buckets(bucket) = node
        else if self.buckets(bucket).get_followers > followers:
            # insert before first element
            self.buckets(bucket).insert_before(node)
        else:
            # insert somewhere in the middle or end
            ptr = self.buckets(bucket)
            while (ptr is not None):
                if (ptr.next() is None) or (ptr.next().get_followers() > followers):
                    ptr.insert_after(node)

    # Public Functions
    def add(json_str, followers=None):
        '''
        Adds the json string json_str to a specific bucket and places it in
        order inside the bucket
        Creates a node with that information and adds it to the proper bucket
        in the right order

        Arguments:
            - json_str :a string formated as a json
            - followers (optional)
        '''
        if followers == None:
            followers = json['followers']
        json = json.loads(json_str)
        # create node and add to correct bucket in correct order
        node = Node(json_str, followers)
        bucket = self.compute_bucket(followers)
        self.add_to_bucket(node, followers, bucket)

    def save(output_file):
        '''
        Save the data *in order* to a file given by output_file

        Arguments:
            - output_file: the location of the file you want to write into

        TODO:
            - Make this work in any general case for both lists, arrays, etc.
            - The problem here is how to iterate over the buckets:
            - eg (made up ranges): go through the elements in bucket 1
              (1-10 followers), then bucket 2 (11-20 followers), all the way to
              the last bucket (1m-10m followers)

        Possible additions:
            - Test out speed of writing one line at a time vs saving all nodes
              from a bucket into a string and then writing once per bucket
        '''
        # PARTIALLY WORKING (ONLY LISTS FOR NOW)
        for bucket in range(len(self.buckets)):
            ptr = self.buckets(bucket)
            while ptr is not None:
                with open(output_file, 'a') as f:
                    f.write(ptr.get_data())
                ptr = ptr.next()
