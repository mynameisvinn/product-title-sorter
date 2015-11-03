
import argparse
import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file")
ap.add_argument("-t", "--type")
ap.add_argument("-i", "--index")
args = vars(ap.parse_args())

reference_filename = 'data/' + args['file']
reference = pd.read_table(reference_filename, header = None)
reference.columns = ['id', 'site', 'category', 'title']

neighbor_filename = 'features/' + args['type'] + '/' + args['type'] + '_neighbors.csv'

neighbor_data_1 = pd.read_csv(neighbor_filename)
neighbor_data_2 = neighbor_data_1.drop(['Unnamed: 0'], axis = 1)
neighbor_data_2.columns = ['nearest_neighbors']

idx = int(args['index'])

neighbors = neighbor_data_2['nearest_neighbors'][idx]
neighbors = map(lambda x: int(x), neighbors.split())

print '=' * 60
print 'QUERY >>> ', reference['title'][idx]
print '=' * 60

for i in range(1, 8):
	print '#',i, ':', reference['title'][neighbors[i]]
	print '-' * 30
    