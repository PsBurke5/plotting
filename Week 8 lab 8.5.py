import matplotlib.pyplot as plt
data = [4,5,8,3,6,5,6,7,6,9,1,4,5,6,7,6,5,6,6,7]
plt.hist(data,bins=7)
plt.ylabel('Counts')
plt.title('Frequency of letters')
plt.show()

import matplotlib.pyplot as plt
word = 'brontosaurus and tyrannosaurus and aptosaurus'
d=dict()
for char in word:
    d[char]=d.get(char,0)+1 # the zero is what is returned if char is not in d print(d)

    plt.bar(list(d.keys()),d.values())
    plt.ylabel('Counts')
    plt.title('Frequency of letters')
    plt.show()
    
