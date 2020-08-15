α = 1
print('α = {}'.format(α))

β = 2

print('β = {}'.format(β))


with open('out.txt','w',encoding='utf8') as f:
    f.write('α = {}'.format(α))
    f.write('\n')
    f.write('β = {}'.format(β))
