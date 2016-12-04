
class Node():
    '''
    Each node will represent an image
    Each node should have the following data:
        - The json data for an image
        - The number of followers the author has
        - Link to next node
        - If this is the last node in the bucket, link to next bucket (for
          convenience)
    '''

    def __init__(data, followers, next_node=None):
        self.data = data
        self.followers = followers
        self.next = next_node

    def get_data():
        '''
        Returns a string formatted as a json
        '''
        return self.data

    def get_followers():
        '''
        Returns the followers
        '''
        return self.followers

    def next():
        '''
        Returns the pointer to the next node
        '''
        return self.next

    def set_next(node):
        '''
        Sets the 'next' for the node
        '''
        self.next = next_node

    '''
    Not very object orientedy, maybe change
    '''
    def insert_before(node):
        '''
        ONLY FOR THE PUTTING NODE AS FIRST ELEMENT IN BUCKET
        '''
        node.set_next(self)

    def insert_after(node):
        next_node = self.next()
        self.next = node
        node.set_next(next_node)
