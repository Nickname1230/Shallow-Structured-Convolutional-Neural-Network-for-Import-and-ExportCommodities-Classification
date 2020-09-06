# 制作class_map
from tqdm import tqdm
with open('./84-85-90/data/train.txt', 'r', encoding='UTF-8') as f:
    dict_map = {}
    for line in tqdm(f):
        lin = line.strip().split('\t')
        gather_label = lin[3]
        label = lin[2]
        if label not in dict_map.keys():
            dict_map[label] = gather_label

with open('./84-85-90/data/class_map.txt', 'w', encoding='UTF-8') as f:
    for key, value in dict_map.items():
        f.write(key)
        f.write('\t')
        f.write(value)
        f.write('\n')
    print('finish')

