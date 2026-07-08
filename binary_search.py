list=[11,14,18,35,40,50]
search_num=18
starting_index=0
ending_index=len(list)-1
found=False
while starting_index<=ending_index:
    middle_index=(starting_index+ending_index)//2
    if list[middle_index]==search_num:
        found=True
        print(f"{search_num} found at index {middle_index}")
        break
    elif list[middle_index]<search_num:
        starting_index=middle_index+1
    else:
        ending_index=middle_index-1

if not found:
    print(f"{search_num} not found in the list")
    