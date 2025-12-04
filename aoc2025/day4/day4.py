from aoc2025.utils.utils import read_input
import copy
cardinals = {
    "up": (0, 1),
    'down': (0, -1),
    'left': (-1, 0),
    'right': (1, 0),
    'right_upper_diagonal': (1, 1),
    'right_lower_diagonal': (1, -1),
    'left_upper_diagonal': (-1, 1),
    'left_lower_diagonal': (-1, -1),
}
directions = ['up', 'down', 'left', 'right',
              'right_upper_diagonal', 'right_lower_diagonal','left_upper_diagonal', 'left_lower_diagonal']
paper_symbol = '@'
empty_symbol = '.'

def clear_and_check_surroundings(list_of_lists):
    paper_list = copy.deepcopy(list_of_lists)
    paper_list = [list(row) for row in paper_list]
    rows = len(paper_list)
    columns = len(paper_list[0])
    paper_count=0
    to_continue = True
    while to_continue:
        points_to_change = []
        count_of_paper = 0
        for row in range(rows):
            for column in range(columns):

                if paper_list[row][column] == paper_symbol:
                    paper = (row,column)
                    surround_value = check_surrounding(paper,rows,columns,paper_list)
                    if surround_value <4:
                        points_to_change.append(paper)
                        count_of_paper+=1
        for values in points_to_change:
            x,y = values
            paper_list[x][y]=empty_symbol
        if count_of_paper==0:
            to_continue = False
        paper_count+=count_of_paper
    return paper_count

def check_surrounding(element,rows,columns,lists_of_lists):
    paper_data = lists_of_lists
    x,y = element
    surrounding_value = 0
    for value in directions:
        a,b = cardinals[value]
        if 0<=x+a<rows and 0<=y+b<columns:
            if paper_data[x+a][y+b]==paper_symbol:
                surrounding_value+=1

    return surrounding_value  # Element not found in any sublist
def star1() -> int:
    data = read_input()
    # TODO: Implement star 1 solution
    rows = len(data)
    cols = len(data[0])
    forklift_paper = 0
    for i in range (rows):
        for j in range (cols):
            if data[i][j] == paper_symbol:
                paper = (i,j)
                sur_value = check_surrounding(paper,rows,cols,data)
                if sur_value<4:
                    forklift_paper+=1
    print(forklift_paper)
    return 0


def star2() -> int:
    data = read_input()
    # TODO: Implement star 2 solution
    forklift_paper = clear_and_check_surroundings(data)
    print(forklift_paper)

    return 0


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
