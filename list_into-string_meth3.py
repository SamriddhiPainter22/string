# Converting list into string using list comprehension  
list1 = ["preet", 18, "Johnny", 20, "Dhruv",26]  
  
convertList = ' '.join([str(e) for e in list1]) #List comprehension  
  
print(convertList)  