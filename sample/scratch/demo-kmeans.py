"""
created by  : ridwanbejo
deskripsi   : contoh implementasi algoritma K-Means untuk clustering data
sumber      : http://endroandriyanto.blogspot.com/2012/06/belajar-clustering-k-means-dan-nearest.html
buku        : Data Mining, Jiawei Han
"""

# library yang dibutuhkan untuk clustering k-means
import math
import collections
import copy

# contoh data yang akan dicluster
hasil_test_fc = { 
                    'a1': (2, 10),
                    'a2': (2, 5),
                    'a3': (8, 4),
                    'a4': (5, 8),
                    'a5': (7, 5),
                    'a6': (6, 4),
                    'a7': (1, 2),
                    'a8': (4, 9),
                }

seeds = {
            '1': {'name' : 'a1', 'point' : (2, 10)}, 
            '2': {'name' : 'a4', 'point' : (5, 8)}, 
            '3': {'name' : 'a7', 'point' : (1, 2)}, 
        }


# fungsi - fungsi yang terlibat dalam perhitungan clustering k-means
def get_euclidean_distance(point_a, point_b):
    temp = math.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)
    return temp

def find_min_dict(dicto):
        temp_v = 999999999999999
        temp_k = '1'
        for k in dicto:
            if dicto[k] < temp_v :
                temp_v = dicto[k]
                temp_k = k
        return temp_k

def do_cluster(points, seeds):
    temp_cluster = {'1': [], '2':[], '3':[]}

    for point in points:
        epoch_list = {}
        
        for seed in seeds:
            temp_distance = get_euclidean_distance(points[point], seeds[seed]['point'])
            epoch_list.update({seed : temp_distance})
            
        temp_min = find_min_dict(epoch_list)
        
        if temp_min == '1':
            temp_cluster['1'].append(points[point]) 
        elif temp_min == '2':
            temp_cluster['2'].append(points[point])
        elif temp_min == '3':
            temp_cluster['3'].append(points[point])
    
    return temp_cluster

def generate_center_of_cluster(temp_cluster):
    temp_center_of_cluster = {}
    temp_index = 1
    for cluster in temp_cluster:
        temp_x = 0
        temp_y = 0
        temp_len = len(temp_cluster[cluster])
        for point in temp_cluster[cluster]:
            temp_x += point[0]
            temp_y += point[1]
        temp_center = {'name':'c'+str(temp_index), 'point':(temp_x * 1.0 / temp_len,  temp_y * 1.0 / temp_len)}
        temp_center_of_cluster.update({str(temp_index): temp_center})
        temp_index += 1
    
    return temp_center_of_cluster

def check_center_of_cluster_similarity(old_center_of_cluster, new_center_of_cluster):
    print "bejo :", old_center_of_cluster
    print "ridwan :", new_center_of_cluster
    
    for old_center in old_center_of_cluster:
        print old_center_of_cluster[old_center]['point']
        print new_center_of_cluster[old_center]['point']
        haula = cmp(old_center_of_cluster[old_center]['point'], new_center_of_cluster[old_center]['point'])
        print "haula: ", haula
        print "\n"
    
    counter = 0
   
    
# bagian utama program
old_center_of_cluster = seeds
temp_cluster = do_cluster(hasil_test_fc, seeds)

    
for i in range(1, 5):
    temp_center_of_cluster = generate_center_of_cluster(temp_cluster) 
    print temp_center_of_cluster
    
    temp_check_coc = check_center_of_cluster_similarity(old_center_of_cluster, temp_center_of_cluster)
    del old_center_of_cluster
    
    old_center_of_cluster = temp_center_of_cluster
    print old_center_of_cluster
    
    temp_cluster = do_cluster(hasil_test_fc, temp_center_of_cluster)
    del temp_center_of_cluster
