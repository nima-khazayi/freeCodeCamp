def arithmetic_arranger(problems, show_answers=False):

    # first statement
    if len(problems) > 5:
        return 'Error: Too many problems.'

    p_set = []
    operand = []
    for p in problems:
        if '+' in p:
            problem = p.replace(' ', '').split('+')
            operand.append('+')
        elif '-' in p:
            problem = p.replace(' ', '').split('-')
            operand.append('-')
        
        else:
            # second statement
            return "Error: Operator must be '+' or '-'."

        p_set.append(problem)

    for i in range(len(p_set)):
        for j in range(len(p_set[i])):
            if not p_set[i][j].isdigit():
                # third statement
                return 'Error: Numbers must only contain digits.'
                
            if len(p_set[i][j]) > 4:
                # fourth statement
                return 'Error: Numbers cannot be more than four digits.'
            
    return visualization(p_set, operand, show_answers)

def visualization(problems, operand, show_answers):
    top_row = []
    bottom_row = []
    dashes = []
    answers = []

    for i in range(len(problems)):
        first = problems[i][0]
        second = problems[i][1]
        op = operand[i]

        # width: longest number + 2 (for operator + space)
        width = max(len(first), len(second)) + 2

        # build each part
        top_row.append(first.rjust(width))
        bottom_row.append(op + second.rjust(width - 1))
        dashes.append('-' * width)

        if show_answers:
            if op == '+':
                ans = str(int(first) + int(second))
            else:
                ans = str(int(first) - int(second))
            answers.append(ans.rjust(width))

    # join with 4 spaces between problems
    arranged = '    '.join(top_row) + '\n' + '    '.join(bottom_row) + '\n' + '    '.join(dashes)
    if show_answers:
        arranged += '\n' + '    '.join(answers)

    return arranged

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
