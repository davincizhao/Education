assignments = []
import logging



rows = 'ABCDEFGHI'
cols = '123456789'

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def eliminate_naked_twins_in_rows(may_be_twins,row_num,values):
    # if other boxes(not including naked twins boxes) in this rows have same value of naked_twins,delete it
    other_boxes = [row_num+c_num for c_num in cols
            if len(values[row_num+c_num]) >= 2
            and may_be_twins != values[row_num+c_num]]

    if len(other_boxes) == 0:
        logging.info(' Nothing to delete in this row*** ')
        return False

    for catch_box in other_boxes:
        if len(may_be_twins) != 2:
            continue
        if may_be_twins in values[catch_box]:
            logging.info(' bef both rows 0 bingo*** %s',may_be_twins)
            #display(values)
            replace_v = values[catch_box].replace(may_be_twins,'')
            assign_value(values, catch_box, replace_v)
            logging.info(' after both rows 0 bingo*** %s',may_be_twins)
            #display(values)
            continue

        if may_be_twins[0] in values[catch_box]:
            replace_v = values[catch_box].replace(may_be_twins[0],'')
            assign_value(values, catch_box, replace_v)
            continue
        if may_be_twins[1] in values[catch_box]:
            replace_v = values[catch_box].replace(may_be_twins[1],'')
            assign_value(values, catch_box, replace_v)

    return values

def eliminate_naked_twins_in_cols(may_be_twins,col_num,values):

    other_boxes = [r_num+col_num for r_num in rows
                    if len(values[r_num+col_num]) >= 2
                    and may_be_twins != values[r_num+col_num]]

    if len(other_boxes) == 0:
        logging.info(' Nothing to delete in this col*** ')
        return False

    for catch_box in other_boxes:
        if len(may_be_twins) != 2:
            continue
        if may_be_twins in values[catch_box]:
            logging.info('in both col 0 bingo*** %s',may_be_twins)

            replace_v = values[catch_box].replace(may_be_twins,'')
            assign_value(values, catch_box, replace_v)
            continue
        if may_be_twins[0] in values[catch_box]:
            logging.info('in col 0 bingo*** %s',may_be_twins)

            replace_v = values[catch_box].replace(may_be_twins[0],'')
            assign_value(values, catch_box, replace_v)
            continue

        if may_be_twins[1] in values[catch_box] :
            logging.info('in col 1 bingo*** %s',may_be_twins)
            replace_v = values[catch_box].replace(may_be_twins[1],'')
            assign_value(values, catch_box, replace_v)

    return values

def eliminate_naked_twins_in_square(may_be_twins,sq,values):

    other_boxes = [u for u in sq
            if len(values[u]) >= 2
            and may_be_twins != values[u]]

    if len(other_boxes) == 0:
        logging.info(' Nothing to delete in this square unit*** ')
        return False

    for catch_box in other_boxes:
        if len(may_be_twins) != 2:
            continue
        if may_be_twins in values[catch_box]:
            logging.info('in both square bingo*** %s',may_be_twins)

            replace_v = values[catch_box].replace(may_be_twins,'')
            assign_value(values, catch_box, replace_v)
            continue
        if may_be_twins[0] in values[catch_box]:
            logging.info('in square bingo*** %s',may_be_twins)

            replace_v = values[catch_box].replace(may_be_twins[0],'')
            assign_value(values, catch_box, replace_v)
            continue

        if may_be_twins[1] in values[catch_box] :
            logging.info('in square bingo*** %s',may_be_twins)
            replace_v = values[catch_box].replace(may_be_twins[1],'')
            assign_value(values, catch_box, replace_v)
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    row_units = [cross(r, cols) for r in rows]
    column_units = [cross(rows, c) for c in cols]
    square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

    _, unitlist, peers = create_boxes_unitlist_peers( )
    no_more_twins = False
    while not no_more_twins:
        board_before = values

        for box_in_ulist in unitlist:
            nake_twin_boxes = [box for box in box_in_ulist if len(values[box]) == 2]
            for box in nake_twin_boxes:
                may_be_twins = values[box]
                for peer in peers[box]:
                    if may_be_twins == values[peer]:
                        if box[0] == peer[0]: # naked twins in rows eliminate
                            logging.info('may_be_twins row====%s',may_be_twins)
                            new_values = eliminate_naked_twins_in_rows(may_be_twins, box[0],values)
                            #if not new_values:
                                #continue

                        if box[1] == peer[1]: # naked twins in cols eliminate
                            logging.info('may_be_twins cols====%s',may_be_twins)
                            new_values = eliminate_naked_twins_in_cols(may_be_twins, box[1],values)
                            #if not new_values:
                                #continue

                        for sq in square_units: #
                            if box in sq and peer in sq: #naked twins in square unit eliminate
                                logging.info('may_be_twins square====%s',may_be_twins)
                                new_values = eliminate_naked_twins_in_square(may_be_twins,sq,values)
                                #if not new_values:
                                    #continue


        board_after = values

        if board_before == board_after:
            no_more_twins = True

    return values


def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

def create_boxes_unitlist_peers():

    boxes = cross(rows, cols)

    #create Diagonal_units
    diagonal_units = [[r+c for r,c in zip(rows,cols)], [r+c for r,c in zip(rows,cols[::-1])]]
    row_units = [cross(r, cols) for r in rows]
    column_units = [cross(rows, c) for c in cols]
    #create 3*3 square units index
    square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
    unitlist = row_units + column_units + square_units + diagonal_units
    units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
    peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

    return boxes, unitlist, peers


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    print(grid)
    boxes, _, _ = create_boxes_unitlist_peers()
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """

    boxes, _, _ = create_boxes_unitlist_peers()

    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):

    #Create 9*9 boxes and peers
    boxes, _, peers = create_boxes_unitlist_peers()

    #search the box having a fit value (len == 1)
    solved_values = [box for box in boxes if len(values[box]) == 1]
    #search all fit value boxes index and save value to digit, search this value's peer
    for box in solved_values:

        digit = values[box]
        for peer in peers[box]:
            logging.info('eliminate=%s',digit)
            replace_v = values[peer].replace(digit,'')
            assign_value(values, peer, replace_v)
    return values

def only_choice(values):
    _, unitlist, _ = create_boxes_unitlist_peers()
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                #values[dplaces[0]] = digit
                logging.info('only choicedigit=%s',digit)
                assign_value(values, dplaces[0], digit)
    return values

def reduce_puzzle(values):

    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        logging.info('before eliminate ***')

        values = eliminate(values)
        logging.info('after eliminate,before only choice***')

        values = only_choice(values)

        logging.warning('before twins***')
        #display(values)
        values = naked_twins(values)

        logging.warning('after twins***+++')
        #display(values)

        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):

    boxes, _, _ = create_boxes_unitlist_peers()
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        #new_sudoku[s] = value
        assign_value(new_sudoku, s, value)
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """


    solve_values = grid_values(grid)
    solve_values = search(solve_values)
    return solve_values

if __name__ == '__main__':
    #diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    diag_sudoku_grid = '9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9................'
    #diag_sudoku_grid = '1......2.....9.5...............8...4.........9..7123...........3....4.....936.4..'
    display(solve(diag_sudoku_grid))


    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
