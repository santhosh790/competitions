'''
Happy Trees
You’re given a balanced bracket expression. In the forest representation of it, find the number of trees which are
happy. A happy tree is a tree in which every vertex other than the leaves has the same number of children. A tree
with just one vertex would also be considered happy.

Input Format
First line of input consists of an integer t denoting the number of test cases. First line of each test case consists
of an integer n denoting the length of the expression. Second line consists of the bracket expression.

Output Format
For each test case, find the number of trees which are happy.

Constraints
1 <= t <= 1000

n = 2 * m where 1 <= m <= 1000

Sample Input
4
12
[[[][]][[]]]
20
[[[][][]][][[][][]]]
14
[[]][[][[]]][]
28
[[[][]][[][]]][[][]][[[[]]]]
Sample Output
0
1
2
3
Explanation
The expression [[[][]][[]]] has the following representation

[]
├── []
│   ├── []
│   └── []
└── []
    └── []
There is only one tree. Root and second child of root has two children each. First child of root has only one child.
It’s not happy.

The expression [[[][][]][][[][][]]] has the following representation

[]
├── []
│   ├── []
│   ├── []
│   └── []
├── []
└── []
    ├── []
    ├── []
    └── []
There is only one tree. All non-leaf vertices have exactly 3 children. Tree is happy.

The expression [[]][[][[]]][] has the following representation

[]
└── []
[]
├── []
└── []
    └── []
[]
There are three trees. Only two of them are happy.

The expression [[[][]][[][]]][[][]][[[[]]]] has the following representation

[]
├── []
│   ├── []
│   └── []
└── []
    ├── []
    └── []
[]
├── []
└── []
[]
└── []
    └── []
        └── []
The number of happy trees is 3.
'''

class Tree:
    def __init__(self, item):
        self.item = item
        self.children = []



def findHappy(vals):
    stack = []
    treestack = []
    trees = []
    for id, each in enumerate(vals):
        #print(id)
        if each == '[':
            child = Tree(1)
            treestack.append(child)
            stack.append('[')
        if each == ']':
            en = stack.pop()
            if en == '[':
                temp = treestack.pop()
                if len(treestack) != 0:
                    parent = treestack.pop()
                    parent.children.append(temp)
                    treestack.append(parent)
                else:
                    trees.append(temp)
    #print(stack)
    #print(treestack)
    print(len(trees))
    return trees

'''
def findHappy_rec(vals, index):
    if vals[index] == '[':
        child = Tree(1)
        stack.append('[')
'''

trees = findHappy('[[[][]][[]]]') ## 1 tree
trees = findHappy('[[[][][]][][[][][]]]') ## 1 tree
#trees = findHappy('[[]][[][[]]][]') ## 3 trees
#trees = findHappy('[[[][]][[][]]][[][]][[[[]]]]') ## 3 trees
stack = []
def getChildrenLength(subtree):
    for each in subtree.children:
        if len(each.children) > 0:
            stack.append(len(each.children))
            getChildrenLength(each)
for each in trees:
    if len(each.children) > 0:
        stack.append(len(each.children))
        getChildrenLength(each)
        children = stack.pop()
        bool = True
        for vals in stack:
            if stack.pop() != children:
                print('Not happy')
                bool = False
        if bool:
            print("happy")
    else:
        print('happy')