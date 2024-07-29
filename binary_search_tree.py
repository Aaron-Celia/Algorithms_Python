class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None



class BinarySearchTree:
  def __init__(self):
    self.root = None

  
  def insert(self, val):
    node = self.root
    new_node = Node(val)

    if node is None:
      self.root = new_node
      return
    
    while True:
      if val < node.val:
        if node.left is None:
          node.left = new_node
          return
        node = node.left
      elif val > node.val:
        if node.right is None:
          node.right = new_node
          return
        node = node.right
      else:
        return
  

  def find(self, val):
    node = self.root

    if node.val == val:
      return node
    
    while node is not None:
      if val < node.val:
        if node.left is None:
          return None
        else:
          node = node.left
      elif val > node.val:
        if node.right is None:
          return None
        else:
          node = node.right
      else:
        return node
    
    return None
  

  def breadth_first_search(self):
    node = self.root
    data = []
    queue = []

    if node is None:
      return data
    
    queue.append(node)

    while len(queue) > 0:
      node = queue[0]
      queue.pop(0)
      data.append(node.val)

      if node.left is not None:
        queue.append(node.left)
      if node.right is not None:
        queue.append(node.right)
    
    return data
  

  def in_order_traversal(self):
    data = []
    node = self.root

    def traverse(node):
      if node is not None:
        traverse(node.left)
        data.append(node.val)
        traverse(node.right)
    
    traverse(node)
    return data
  
  
  def pre_order_traversal(self):
    data = []
    node = self.root

    def traverse(node):
      if node is not None:
        data.append(node.val)
        traverse(node.left)
        traverse(node.right)
    
    traverse(node)
    return data
  
  
  def post_order_traversal(self):
    data = []
    node = self.root

    def traverse(node):
      if node is not None:
        traverse(node.left)
        traverse(node.right)
        data.append(node.val)
    
    traverse(node)
    return data
