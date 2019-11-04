sandwich_order = ['sda', 'ssdw', 'eers']
finished_sandwiches = []
while sandwich_order:
    currurt_sand = sandwich_order.pop()
    print("doing:"+currurt_sand)
    finished_sandwiches.append(currurt_sand)
print("the follow snd is done:\n")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())
