import numpy as np

def match_edges(tiles, tile_num):
    match = 0
    match_num = []
    directions = []
    control = False
    for k in range(tiles.shape[0]):
        if k != tile_num:
            test_tile = np.copy(tiles[k,:,:])
            for rot in range(4):
                # test_tile = np.copy(tiles[k,:,:])
                # tiles[k,:,:] = np.rot90(tiles[k,:,:])
                test_tile = np.rot90(test_tile)                
                for flip in range(2):
                    # tiles[k,:,:] = np.flip(tiles[k,:,:], flip)
                    test_tile = np.flip(test_tile, flip)
                    # res = np.abs(tiles[tile_num, :,:] - tiles[k,:,:])
                    res = np.abs(tiles[tile_num, :,:] - test_tile)
                    # print(res)
                    for i in [-1,0]:
                        if np.sum(res[i,:]) == 0:
                            match+=1
                            match_num.append(k)
                            directions.append('c{}'.format(i))
                            control = True
                            tiles[k,:,:] = np.flip(np.copy(test_tile),0)
                            break
                    for j in [-1,0]:
                        if np.sum(res[:,j]) == 0:
                            match+=1
                            match_num.append(k)
                            directions.append('r{}'.format(j))
                            control = True
                            tiles[k,:,:] = np.flip(np.copy(test_tile),-1)
                            break
                    # if control:
                    #     break

    return match, match_num, directions, tiles

filename = 'task_20.txt'
# filename = 'test.txt'
file = open(filename, 'r')

lines = file.readlines()

tilenames = []
for line in lines:
    if line[0] == 'T':
        line = line.rstrip()
        tilenames.append(int(line.split(' ')[1][:-1]))

# tilenames.sort()

num_tiles = len(tilenames)
tiles = np.zeros((num_tiles, 10,10))

i = 0
j = 0
for line in lines[1:]:
    if line[0] == 'T':
        i+=1
        j=0
    elif line[0] != '\n':
        line = line.rstrip()
        for k, char in enumerate(line):
            if char == '.':
                tiles[i,j,k] = 0
            else:
                tiles[i,j,k] = 1
        j+=1

## part 1
# prod = 1
# for i in range(num_tiles):
#     m,_,_,_ = match_edges(tiles, i)
#     if m == 2:
#         print(tilenames[i])
#         prod *=tilenames[i]
# print(prod)

print(match_edges(tiles, 0)[1:3])
_, matches, directions,_ = match_edges(tiles,0)

