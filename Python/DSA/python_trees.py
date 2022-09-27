class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def print_info(self):
        return f"Name: {self.name}, Username: {self.username}, Email: {self.email}"

    def __repr__(self) -> str:
        return f"Name: {self.name}, Username: {self.username}, Email: {self.email}"
    
    def __str__(self) -> str:
        return self.__repr__()

# IN INEFFECIENT WAY----->>>>>

# class Database:
#     def __init__(self):
#         self.users = []
#     def insert(self,user):
#         if len(self.users)==0:
#             self.users.insert(0,user)
#         for i in range(len(self.users)):
#             if self.users[i].username > user.username:
#                 self.users.insert(i,user)
#                 break
#     def find(self,username):
#         for i in self.users:
#             if i.username == username:
#                 return i
#     def update(self, user_info):
#         user_finder = self.find(user_info.username)
#         user_finder.name = user_info.name
#         user_finder.email = user_info.email
#     def users_list(self):
#         return self.users

# john = User("John", "johncena","john@cena.com")
# Joe = User("Joe","joelux","joe@lux.com")
# Rick = User("Rick","ricktherock","rick@rock.com")
# Alex = User(name="Alex",username="Alexrox",email="alex@rox.com")

# # print(john)
# user_db = Database()
# user_db.insert(john)
# user_db.insert(Joe)
# user_db.insert(Rick)
# user_db.insert(Alex)
# # print(user_db.use4rs_list())
# # print(user_db.find("joelux"))
# print(Joe)
# user_db.update(User(name="Joe Nick",username="joelux",email="joe@nick.com"))
# print(Joe)


# BINARY TREE----->>>>>



# class TreeNode:
#     def __init__(self,key) -> None:
#         self.key = key
#         self.left = None
#         self.right = None

#     def tree_to_tuple(self):
#         if self is None:
#             return None
#         elif self.left is None and self.right is None:
#             return self.key
#         else:
#             return (TreeNode.tree_to_tuple(self.left),self.key,TreeNode.tree_to_tuple(self.right))
#     @staticmethod
#     def display_tree(self,space="\t",level=0):
#         if self is None:
#             print(space*level+"∅")
#             return 
#         elif self.left is None and self.right is None:
#             print(space*level+str(self.key))
#             return
#         TreeNode.display_tree(self.right, space, level+1)
#         print(space*level+str(self.key))
#         TreeNode.display_tree(self.left,space,level+1)

#     @staticmethod
#     def parse_tuple(data):
#         if isinstance(data, tuple) and len(data)==3:
#             node = TreeNode(data[1])
#             node.left = TreeNode.parse_tuple(data[0])
#             node.right = TreeNode.parse_tuple(data[2])
#         elif data is None:
#             node = None
#         else:
#             node = TreeNode(data)
#         return node

#     def traverse_in_order(self):
#         if self is None:
#             return []
#         else:
#             return (TreeNode.traverse_in_order(self.left)+[self.key]+TreeNode.traverse_in_order(self.right))

#     def tree_height(self):
#         if self is None:
#             return 0
#         else:
#             return 1 + max(TreeNode.tree_height(self.left),TreeNode.tree_height(self.right))

#     def tree_size(self):
#         if self is None:
#             return 0
#         else:
#             return 1 + TreeNode.tree_size(self.left)+ TreeNode.tree_size(self.right)

#     def __repr__(self) -> str:
#         return f"BinarTree:{self.tree_to_tuple()}"

#     def __str__(self) -> str:
#         return self.__repr__()


# bs_tree1 = TreeNode.parse_tuple(((1,3,2),5,(6,7,8)))
# # tree1 = parse_tuple((2,5,7))
# # print(tree1.key)
# # print(tree1.left.key)
# # print(tree1.left.left.key)
# # print(tree1.left.right.key)
# # print(tree1.right.key)
# # print(tree1.right.left.key)
# # print(tree1.right.right.key)
# # tree1.display_tree()
# print(tree1.tree_size())



# BINARY SEARCH TREE ----->>>>>
# Checking binary search tree --->>>

# def is_bst(node):
#     if node is None:
#         return True, None, None
    
#     is_left_bst,min_left,max_left = is_bst(node.left)
#     is_right_bst,min_right,max_right = is_bst(node.right)

#     is_bst_node = is_left_bst and is_right_bst and (max_left is None or node.key>max_left) and (min_right is None or node.key<min_right)
#     min_key = min([x for x in [min_left,node.key,min_right] if x is not None])
#     max_key = max([x for x in [max_left,node.key,max_right] if x is not None])

#     return is_bst_node, min_key, max_key



# tree1 = TreeNode.parse_tuple(((1,3,2),5,(6,7,8)))
# print(is_bst(tree1))


# STORING KEY-VALUE PAIRS USING BSTs ----->>>>>

class BSTnode:
    def __init__(self,key,value=None) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def display_node(self,space="\t",level=0):
        if self is None:
            print(space*level+"∅")
            return
        elif self.left is None and self.right is None:
            print(space*level+str(self.key))
            return

        BSTnode.display_node(self.right,space,level+1)
        print(space*level+str(self.key))
        BSTnode.display_node(self.left,space,level+1)
        
    def insert(self,key,value):
        if self is None:
            self = BSTnode(key,value)
        elif key<self.key:
            self.left = BSTnode.insert(self.left,key,value)
            self.left.parent = self
        elif key>self.key:
            self.right = BSTnode.insert(self.right,key,value)
            self.right.parent = self
        return self

    def find(self,key):
        if self is None:
            return None
        elif key == self.key:
            return self
        elif key<self.key:
            return BSTnode.find(self.left,key)
        elif key>self.key:
            return BSTnode.find(self.right,key) 

    def update(self,key,value):
        finder = BSTnode.find(self,key)
        if finder:
            finder.value = value
    
    def list_all(self):
        if self is None:
            return []
        return BSTnode.list_all(self.left)+[(self.key,self.value)]+BSTnode.list_all(self.right)
    
    def tree_size(self):
        if self is None:
            return 0
        return 1 + (BSTnode.tree_size(self.left)+BSTnode.tree_size(self.right))

    def is_balanced(self):
        if self is None:
            return True,0
        balanced_l,height_l = BSTnode.is_balanced(self.left)
        balanced_r,height_r = BSTnode.is_balanced(self.right)
        balanced = balanced_l and balanced_r and abs(height_l-height_r) <=1
        height = 1+ max(height_l,height_r)
        return balanced,height

    @staticmethod
    def make_balanced_bst(data,lo=0,high=None,parent=None):
        if high is None:
            high = len(data)-1
            
        if lo>high:
            return None
        
        mid_index = (lo+high)//2
        key,value = data[mid_index] 
        
        node = BSTnode(key,value)
        node.parent = parent
        node.left = BSTnode.make_balanced_bst(data,lo,mid_index-1,node)
        node.right = BSTnode.make_balanced_bst(data,mid_index+1,high,node)
        return node

    def balance_unbalance_bst(node):
        list = BSTnode.list_all(node)
        return BSTnode.make_balanced_bst(list)

john = User("John", "johncena","john@cena.com")
Joe = User("Joe","joelux","joe@lux.com")
Rick = User("Rick","ricktherock","rick@rock.com")
Alex = User(name="Alex",username="Alexrox",email="alex@rox.com")
Alex2 = User(name="Alex2",username="Roxalex",email="rox@alex.com")

# bs_tree1 = BSTnode(john.username,john)
# bs_tree1.left = BSTnode(Joe.username,Joe)
# bs_tree1.left.parent = bs_tree1
# bs_tree1.right = BSTnode(Rick.username,Rick)
# bs_tree1.right.parent = bs_tree1
# # print(bs_tree1.left.key)
# BSTnode.insert(bs_tree1,Alex.username,Alex) 
# BSTnode.insert(bs_tree1,Alex2.username,Alex2) 
# # # bs_tree1.display_node()
# # # finder = bs_tree1.find("Alexrox")
# # # print(finder.value)
# # # bs_tree1.update("Alexrox",Alex2)
# # # print(finder.value)
# # # print(bs_tree1.list_all())
# print(bs_tree1.is_balanced())
# # # BSTnode.insert(bs_tree1,Alex2.username,Alex2)
# # # print(bs_tree1.is_balanced())
# # user_list = [(Alex.username,Alex),(Joe.username,Joe),(john.username,john),(Rick.username,Rick)]
# # bs_tree2 = BSTnode.make_balanced_bst(user_list)
# # print(bs_tree2)
# # bs_tree2.display_node()
# bs_tree3 = BSTnode.balance_unbalance_bst(bs_tree1)
# print(bs_tree3.is_balanced())
# bs_tree1.display_node()
# bs_tree3.display_node()


# PYTHON FRIENDLY TREEMAP ----->>>>>

class TreeMap():
    def __init__(self):
        self.root = None
    
    def __setitem__(self,key,value):
        finder = BSTnode.find(self.root,key)
        if not finder:
            self.root = BSTnode.insert(self.root,key,value)
            self.root = BSTnode.balance_unbalance_bst(self.root)
        else:
            self.root = BSTnode.update(self,key,value)

    def __getitem__(self,key):
        finder = BSTnode.find(self.root,key)
        if not finder:
            return None
        else:
            return finder.value

    def __iter__(self):
        return (x for x in BSTnode.list_all(self.root))
    
    def __len__(self):
        return BSTnode.tree_size(self.root)
    def display(self):
        return BSTnode.display_node(self.root)
    
    def balance_checker(self):
        return BSTnode.is_balanced(self.root)

tree_cls = TreeMap()
tree_cls["johncena"] = john
tree_cls["joelux"] = Joe
tree_cls["ricktherock"] = Rick
tree_cls["Alexrox"] = Alex
# tree_cls.display()
# print(tree_cls.balance_checker())
tree_cls["Roxalex"] = Alex2
# tree_cls.display()
# print(tree_cls.balance_checker())
# print(tree_cls["Roxalex"])
# for key,value in tree_cls:
#     print(key,"--->>>",value)
print(len(tree_cls))