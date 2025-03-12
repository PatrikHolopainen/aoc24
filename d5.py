
rules = []

page_nrs_list = []

with open('test_input.txt') as f:
    lines = f.readlines()

    for l in lines:
        if '|' in l:
            rules.append([int(num) for num in l.split('|')])
        elif ',' in l:
            page_nrs_list.append([int(num) for num in l.split(',')])


total = 0

failed_page_nrs =[]

for page_nrs in page_nrs_list:
    idx_pairs = []
    for a,b in rules:
        try:
            i_a = page_nrs.index(a)+1 # Add ones to make it 1-indexed
            i_b = page_nrs.index(b)+1
        except ValueError:
            i_a = None
            i_b = None
        if i_a and i_b:
            idx_pairs.append((i_a,i_b))
    ordered_pairs = all([a < b for a,b in idx_pairs])
    if ordered_pairs:
        total += page_nrs[len(page_nrs)//2]
    else:
        failed_page_nrs.append(page_nrs)

# B part

b_total = 0

for page_nrs in failed_page_nrs:

    i = 0
    n = len(rules)
    while i < n:
        a,b = rules[i]
        try:
            i_a = page_nrs.index(a)+1 # Add ones to make it 1-indexed
            i_b = page_nrs.index(b)+1
        except ValueError:
            i_a = None
            i_b = None
        if i_a and i_b:
            i_a, i_b = i_a -1, i_b -1
            if i_a > i_b:
                page_nrs[i_a], page_nrs[i_b] = page_nrs[i_b], page_nrs[i_a]
                i = 0
            else:
                i +=1
        else:
            i+=1
        
    b_total += page_nrs[len(page_nrs)//2]
print(b_total)