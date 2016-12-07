import json
import node

class Table():
    '''
    Data structure description:
        - Very similar to a hash table with chaining as linked lists
        - Has 'buckets' that are distributed in a Log Normal Distribution see
          [1] for more info, the reason for this distribution is outlined in
          experiments/number_statistics.ipynb
        - For example if the number of followers is 200 it'll be seperated into
          the bucket for values betweeen 195-205 (or something similar), while
          at the same time if the value was 200k it'll be in the bucket of
          150k-250k followers
    [1] http://mathworld.wolfram.com/LogNormalDistribution.html

    TODO in the future:
        - Use a better hash function which will find the bucket based on the Log
          Normal Distribution (useful if the dataset is big enough - for now
          this is good enough)

    Possible additions:
        1. Increase the number of buckets when it gets too full to improve
           speed, would split the current buckets into these ranges.
           Eg: prev bucket range was 100-200, new buckets at 100-150 and 151-200
           traverse list and set element 150 to 'None' and set 151 to be the
           first element of the next bucket
    '''
    def __init__(self, mu=0, sigma=1, num_buckets=100):
        '''
        Initialize the table with num_buckets and distributed according to mu
        and sigma.
        '''
        self.mu = mu
        self.sigma = sigma
        # The following will have to be changed based on num_buckets
        self.ranges = self.get_ranges(num_buckets)
        self.buckets = []

        #for i in range(num_buckets):
        for i in range(len(self.ranges)):
            self.buckets.append(None)

    # Helper Functions
    def compute_bucket(self, followers):
        '''
        Helper function
        Add to the given bucket

        Arguments:
            - followers: the number of followers to compute which bucket the
              node should be in
        Returns:
            - A pointer (or index) to the bucket that the node should be in
        '''
        # Will need to change the following to compute buckets

        i = 0
        while followers > self.ranges[i]:
            i += 1
        return i

    def get_ranges(self, num_buckets):
        '''
        Returns the ranges for each bucket

        TODO: Finish this to actually calculate the num buckets -> use the code
        from experiments
        '''
        # TODO IMPORANT! Change this to work with num_buckets

        ranges = [4, 8, 10, 12, 16, 18, 21, 23, 26, 28, 32, 34, 36, 39, 41, 43,
        46, 48, 51, 53, 55, 58, 60, 64, 66, 69, 71, 74, 76, 79, 81, 84, 86, 89,
        91, 94, 96, 99, 101, 104, 106, 109, 111, 114, 116, 119, 121, 124, 128,
        130, 133, 136, 139, 142, 144, 147, 150, 153, 156, 159, 161, 164, 167,
        170, 173, 175, 178, 181, 184, 187, 190, 192, 195, 198, 201, 204, 207,
        209, 212, 215, 218, 221, 223, 226, 229, 232, 235, 238, 240, 243, 246,
        249, 252, 256, 260, 265, 270, 274, 279, 284, 289, 293, 298, 303, 307,
        312, 317, 322, 326, 331, 336, 341, 345, 350, 355, 359, 364, 369, 374,
        378, 383, 388, 392, 397, 402, 407, 411, 416, 421, 426, 430, 435, 440,
        444, 449, 454, 459, 463, 468, 473, 477, 482, 487, 492, 496, 501, 506,
        512, 520, 529, 537, 546, 554, 563, 571, 580, 588, 597, 605, 614, 622,
        631, 639, 648, 656, 665, 673, 682, 690, 699, 707, 716, 724, 733, 741,
        750, 758, 767, 776, 784, 793, 801, 810, 818, 827, 835, 844, 852, 861,
        869, 878, 886, 895, 903, 912, 920, 929, 937, 946, 954, 963, 971, 980,
        988, 997, 1005, 1014, 1024, 1043, 1062, 1081, 1101, 1120, 1139, 1159,
        1178, 1197, 1217, 1236, 1255, 1274, 1294, 1313, 1332, 1352, 1371, 1390,
        1410, 1429, 1448, 1467, 1487, 1506, 1525, 1545, 1564, 1583, 1603, 1622,
        1641, 1660, 1680, 1699, 1718, 1738, 1757, 1776, 1796, 1815, 1834, 1853,
        1873, 1892, 1911, 1931, 1950, 1969, 1989, 2008, 2027, 2048, 2111, 2175,
        2239, 2303, 2367, 2431, 2495, 2559, 2623, 2687, 2751, 2815, 2879, 2943,
        3007, 3071, 3135, 3199, 3263, 3327, 3391, 3455, 3519, 3583, 3647, 3711,
        3775, 3839, 3903, 3967, 4031, 4096, 4282, 4468, 4654, 4840, 5026, 5212,
        5398, 5585, 5771, 5957, 6143, 6329, 6515, 6701, 6888, 7074, 7260, 7446,
        7632, 7818, 8004, 8192, 8738, 9284, 9830, 10376, 10922, 11468, 12014,
        12560, 13106, 13652, 14198, 14744, 15290, 15836, 16384, 19660, 22937,
        26213, 29490, 32768, 49151, 65536, 131072, 157286, 183500, 209714,
        235928, 262144, 299593, 337042, 374491, 411940, 449389, 486838, 524288,
        699050, 873812, 1048576]
        return ranges

    def get_num_buckets(self, ):
        '''
        Helper function
        Returns the total number of bucket

        Arguments:
        - followers: the number of followers to compute which bucket the
        node should be in
        Returns:
        - A number
        '''
        return len(self.buckets)

    def buckets(self, bucket):
        '''
        Helper function
        Abstraction that returns the bucket you want.
        Will make code calling it work regardless of data structure of the table
        of buckets

        Arguments:
            - bucket: the identifier of the buket (index or code, etc.)
        Returns:
            - the first node in that bucket (or 'None' if bucket is empty)
        '''
        return self.buckets[bucket]

    def set_bucket(self, bucket, el):
        '''
        Helper function
        Abstraction that set the bucket to what you want
        Will make code calling it work regardless of data structure of the table
        of buckets

        Arguments:
            - bucket: the identifier of the buket (index or code, etc.)
            - el: what you want to place in it
        '''
        self.buckets[bucket] = el

    def add_to_bucket(self, node, bucket, followers=None):
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
            self.set_bucket(bucket, node)
        elif self.buckets(bucket).get_followers > followers:
            # insert before first element
            self.buckets(bucket).insert_before(node)
        else:
            # insert somewhere in the middle or end
            ptr = self.buckets(bucket)
            while (ptr is not None):
                if (ptr.next() is None) or (ptr.next().get_followers() > followers):
                    ptr.insert_after(node)

    # Public Functions
    def add(self, json_str, followers=None):
        '''
        Adds the json string json_str to a specific bucket and places it in
        order inside the bucket
        Creates a node with that information and adds it to the proper bucket
        in the right order

        Arguments:
            - json_str: a string formated as a json
            - followers (optional)
        '''
        if followers == None:
            print json_str
            json_struc = json.loads(json_str)
            followers = json_struc['entry_data']['ProfilePage'][0]['user']['followed_by']['count']
        # create node and add to correct bucket in correct order
        node = Node(json_str, followers)
        bucket = self.compute_bucket(followers)
        self.add_to_bucket(node, followers, bucket)

    def print_bucket(self, bucket=None):
        '''
        Prints the content of bucket or if none given, print all of them

        Arguments:
            - bucket (optional): if none given print all
        '''
        if bucket is not None:
            ptr = self.buckets(bucket)
            while ptr is not None:
                ptr.get_data()
                ptr = ptr.next()
        else:
            for bucket in range(self.get_num_buckets()):
                ptr = self.buckets(bucket)
                while ptr is not None:
                    ptr.get_data()
                    ptr = ptr.next()

    def save(self, output_file):
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
        #output_file = '../'+output_file # Since presorting is a subfolder
        for bucket in range(self.get_num_buckets()):
            ptr = self.buckets(bucket)
            while ptr is not None:
                with open(output_file, 'a') as f:
                    f.write(ptr.get_data())
                ptr = ptr.next()
