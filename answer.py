# #1. check if a variable is of type int
# a = 10
# print(isinstance(a,int))

# #2. convert a string to an integer
# s = "12345"
# num = int(s)
# print(num)

# #3. get the length of a list 
# s = "shreya choure"
# print(len(s))

# #4. create a tuple and access the 2nd element
# tuple = (1 , 2 , 3 , 4,'shreya')
# print(tuple[1])

# #5. convert list to set
# list = [1,2,3,4]
# a = set(list)
# print(a)

#6. check if a key exists in a dict
# dict = {"Name":"shreya","Age":"21","location":"pune","desig":"SDE" }
# print("Name" in dict)

#7. convert an integer to a string 
# int = 709
# s = str(int)
# print(s)

# #8. merg two dict
# dict_1 = {"Name" : "shreya" , "Age" : "21"}
# dict_2 = {"emp_id" : "102" , "location" : "pune"}
# merge = {**dict_1, **dict_2}
# print(merge)

# #9. find the max num in a list
# list = [568 , 102, 99]
# print(max(list))

#10. convert list of tuple to a dictonary
# list = [("a",1),("b",2),("c",3)]
# dict_1 = dict(list)
# print(dict_1)

#11. reverse a string
# s = "shreya choure"
# reverse = s[::-1]
# print(reverse)

#12. remove duplicates from list while keeping order
# list = [1,2,2,3,3,3,2,2,4]
# range = []
# for i in list:
#     if i not in range:
#         range.append(i)
# print(range)

#13. convert nested list to a single flat list
# nested = [[1, 2], [3, 4], [5]]
# flat = [x for sub in nested for x in sub]
# print(flat)

#14. count frequency of each element in list
# list = [1, 2, 2, 3, 3, 3]
# freq = {}
# for a in list:
#     freq[a] = freq.get(a, 0) + 1
# print(freq)

#15. sort dictonary by value

#16. check if two lists have the same element 
list1 = [1, 2, 3]
list2 = [3, 2, 1]
print(set(list1) == set(list2))

#17. find common keys in two dictionaries



