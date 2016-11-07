import json

def count():
    '''
    Counts the number
    '''
    file_input = '../external_files/input.json' # TODO Change this part
    num_stats = {}

    f_read = open(file_input, 'r')
    for line in f_read:
        loaded_json = json.loads(line[:line.index('},')+1])
        followed_by = loaded_json['followed_by']
        num_stats[followed_by] = num_stats.get(followed_by, 0) + 1
    return num_stats

def magnitude_of_scale(num_stats, base=10):
    '''
    Will seperate the statistics into magnitudes of scale (powers of the base).
    The dictionary will be organized as exponents not the actual number.
    Ex: num_stats_powers[2] will output the number of examples between 100-999
    '''
    num_stats_powers = {}
    for key in num_stats.keys():
        n = -1 # assumes above that all accounts have above 0 followers
        temp = key
        while temp > 0:
            temp /= base
            n += 1
        num_stats_powers[n] = num_stats_powers.get(n, 0) + num_stats[key]
    return num_stats_powers
