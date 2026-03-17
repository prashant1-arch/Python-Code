list=[12,4,5,7,18,22]
search_num=18
found=False
for i in range(len(list)):
    if list[i]==search_num:
        found=True
        print(f"{search_num} found at index {i}")
        break

if not found:
    print(f"{search_num} not found in the list")
    