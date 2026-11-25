ns = [4, 5, -1, 3, 2, 1, 0, -2, -3, -4]

# n0 n2 n-1
print(f'{ns[0]} {ns[2]} {ns[-1]}')

# change
ns[3] = 10

# append, pop
ns.append(67)
ns.pop(0)

print(f'{ns} - {len(ns)} elements')