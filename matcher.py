def matchstr(expression, param):
    typebkt = {'(': ')', '[': ']', '{': '}', '<': '>'}
    start, end = -1, -1
    answer = ['True', 'None', 'None']
    for i in range(len(expression)):
        if expression[i] == param[0]:
            start = i
            continue
        if expression[i] == typebkt[param[0]]:
            end = i
            break
    if len(param) > 1:
        for i in range(start + 1, end):
            if expression[i] == param[1]:
                for k in range(i + 1, end):
                    if expression[k] == typebkt[param[1]]:
                        break
                    if k == end - 1 and expression[k] != typebkt[param[1]]:
                        answer[0] = 'False'
                        answer[1] = (expression[end], end)
                        answer[2] = (expression[i], i)
                break
    return answer
