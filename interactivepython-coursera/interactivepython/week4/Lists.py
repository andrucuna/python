__author__ = 'andrucuna'

# Fun with lists
# Create

mt_lists = []
print mt_lists

l1 = [1, 3, 4, -7, 62, 43]
print l1

l2 = ['milk', 'eggs', "bread", "butter"]
print l2

l3 = [ [3, 4], ['a', 'b', 'c'], [] ]
print l3


# Access

print len(mt_lists), len(l1), len(l2), len(l3)
print "first element: ", l1[0]
print "last element:", l1[-1]

l4 = l2[1:3]
print l4


# Update

l2[0] = "cheese"
print l2