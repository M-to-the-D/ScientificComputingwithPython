def arithmetic_arranger(list1, bool=False):
    if len(list1)>5:
        return 'Error: Too many problems.'
    l1=[]
    for i in list1:
        #print(i)
        temp=i.split()
        l1.append(temp)
    formatted_problems = [[], [], [],[]]
    for i in l1:
        if i[0].isnumeric() and i[2].isnumeric():
            if len(i[0])<=4 and len(i[2])<=4:
                if i[1]=='+':
                    i.append(str(int(i[0])+int(i[2])))
                elif i[1]=='-':
                    i.append(str(int(i[0])-int(i[2])))
                else:
                    return 'Error: Operator must be '+' or '-'.'
                print(i)
                max_width = max(len(i[0]), len(i[2]), len(i[3]))+2
                formatted_problems[0].append(i[0].rjust(max_width-len(i[0])+1))
                formatted_problems[1].append((i[1] +' '+ i[2]).rjust(max_width-1))
                formatted_problems[2].append('-' * (max_width-1))
                if bool:
                    formatted_problems[3].append(i[3].rjust(max_width-len(i[3])))
            else:
                return 'Error: Numbers cannot be more than four digits.'
        else:
            return 'Error: Numbers must only contain digits.'
    arranged_problems = '\n'.join('    '.join(row) for row in formatted_problems)
    return arranged_problems

#print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print(arithmetic_arranger(['1 + 2', '1 - 9380']))
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))