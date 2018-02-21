N = 4
arr = [[N*i + j for i in range(N)] for j in range(N)]
def print_map():
    seperate_line = "+------+------+------+------+"
    print(seperate_line)
    for i in range(N):
        row = arr[i]
        print(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

        print(seperate_line)


if __name__ == "__main__":

    print_map()
#map(list,zip(*[[1,2,3],[4,5,6],[7,8,9]]))
#matrix[:] = map(list,zip(*matrix[::-1]))