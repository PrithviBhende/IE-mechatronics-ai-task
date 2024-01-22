names = []
nums = []
for i in range(5):
    name = input("Enter a name: ")
    names.append(name)
    number = int(input("Enter a number: "))
    nums.append(number)
dict = {}
for i in range(5):
    dict[names[i]] = nums[i]
srtd_names = srtd(names)
srtd_dict = {}
for name in srtd_names:
    srtd_dict[name] = dict[name]
print(srtd_dict)