#THAYS CONCEICAO DA SILVA  2019.2

class Node:
  def __init__(self, key, parent = None, left = None, right = None, item = None):
    self.key = key
    self.item = item
    self.parent = parent
    self.left = left
    self.right = right
    self.color = 1

  def __str__(self):
    return str(self.key)

    
class RB_Tree:
  def __init__(self):
    self.none = Node(float('inf'))
    #self.none.color = 1
    self.root = self.none
    self.none.parent = self.none
    self.none.left = self.none
    self.none.right = self.none

  def LeftRotate(self, x):
    y = x.right
    x.right = y.left

    if y.left != self.none:
      y.left.parent = x
    
    y.parent = x.parent

    if x.parent == self.none:
      self.root = y
    elif x == x.parent.left:
      x.parent.left = y
    else: 
      x.parent.right = y
    
    y.left = x
    x.parent = y


  def RightRotate(self, x):
    y = x.left
    x.left = y.right

    if y.right != self.none:
      y.right.parent = x
    
    y.parent = x.parent

    if x.parent == self.none:
      self.root = y
    elif x == x.parent.right:
      x.parent.right = y
    else: 
      x.parent.left = y
    
    y.righ = x
    x.parent = y


  def InsertFixup(self, z):
    while z.parent.color == 0:
      if z.parent == z.parent.parent.left:
        y = z.parent.parent.right
        
        if y.color == 0:
          z.parent.color = 1
          y.color =1
          z.parent.parent.color = 0
          z = z.parent.parent
        
        elif y.color == 1:
          if z == z.parent.right:
            z = z.parent
            self.LeftRotate(z)
          if z == z.parent.left:
            z.parent.color = 1
            z.parent.parent.color = 0
            self.RightRotate(z.parent.parent)
      
      elif z.parent == z.parent.parent.right:
        y = z.parent.parent.left
        
        if y.color == 0:
          z.parent.color = 1
          y.color =1
          z.parent.parent.color = 0
          z = z.parent.parent
        
        elif y.color == 1:
          if z == z.parent.left:
            z = z.parent
            self.RightRotate(z)
          if z == z.parent.right:
            z.parent.color = 1
            z.parent.parent.color = 0
            self.LeftRotate(z.parent.parent)

    self.root.color = 1


  def Insert(self, key):
    z = Node(key, parent = self.none, left = self.none, right = self.none)
    y = self.none
    x = self.root

    while x != self.none:
      y = x
      if z.key < x.key:
        x = x.left
      else:
        x = x.right
      
    z.parent = y
    
    if y == self.none:
      self.root = z
    elif z.key < x.key:
      y.left = z
    else:
      y.right = z
    
    z.left = self.none
    z.right = self.none
    z.color = 0

    self.InsertFixup(z)

  def Transplant(self, u, v):
    if u.parent == self.none:
      self.root = v
    elif u == u.parent.left:
      u.parent.left = v
    else:
      u.parent.right = v
    
    v.parent = u.parent
  

  def DeleteFixup(self, x):
    while x != self.root and x.color == 1:
      if x == x.parent.left:
        w = x.parent.right
        if w.color == 0:
          w.color = 1
          x.parent.color = 0
          self.LeftRotate(x.parent)
          w = w.parent.right
        if w.left.color == 1 and w.right.color == 1:
          w.color = 0
          x = x.parent
        elif w.right.color == 1:
          w.left.color = 1
          w.color = 0
          self.RightRotate(w)
          w = x.parent.right
        elif w.right.color == 0:
          w.color = x.parent.color
          x.parent.color = 1
          w.right.color = 1
          self.LeftRotate(x.parent)
          x = self.root
      else:
        w = x.parent.left
        if w.color == 0:
          w.color = 1
          x.parent.color = 0
          self.Right(x.parent)
          w = w.parent.left
        if w.right.color == 1 and w.left.color == 1:
          w.color = 0
          x = x.parent
        elif w.left.color == 1:
          w.right.color = 1
          w.color = 0
          self.LeftRotate(w)
          w = x.parent.left
        elif w.left.color == 0:
          w.color = x.parent.color
          x.parent.color = 1
          w.left.color = 1
          self.RightRotate(x.parent)
          x = self.root
        
    x.color = 1


  def Minimum(self, x):
    while x.left != self.none:
      x = x.left
    return x


  def Delete(self, key):
    z = Node(key, parent = self.none, left = self.none, right = self.none)
    z.left = self.none
    z.right = self.none
    y = z
    y_oc = y.color

    if z.left == self.none:
      x = z.right
      self.Transplant(z, z.right)
    elif z.right == self.none:
      x = z.left
      self.Transplant(z, z.left)
    else:
      y = self.Minimum(z.right)
      y_oc = y.color
      x = y.right

      if y.parent == z:
        x.parent = y
      else:
        self.Transplant(y, y.right)
        y.right = z.right
        y.right.parent = y
      
      self.Transplant(z, y)
      y.left = z.left
      y.left.parent = y
      y.color = z.color
    
    if y_oc == 1:
      self.DeleteFixup(x)

  def Search(self, key):
    if self.root == self.none:
      return False
    x = self.root
    while key != x.key:
      if key < x.key:
        x = x.left
      else:
        x = x.right
      return True

  def InOrder(self, node):
    if node != self.none:
      self.InOrder(node.left)
      print(node,  end=" ")
      self.InOrder(node.right)

  def Show(self):
    print("Arvore: ", end=" ")
    self.InOrder(self.root)
    
#--------------------------------------

rbTree = RB_Tree()
opcao = 0

while opcao != 5:

    print("""
    Bem-vindo(a) a Arvore Vermelho-Preto
    __________________________________________
    | Digite o número que controle a árvore: |
    | 1: Inserir                             |
    | 2: Excluir                             |
    | 3: Pesquisar                           |
    | 4: Exibir                              |
    | 5: Sair do programa                    |
    __________________________________________
    """)

    opcao = int(input("Opcao escolhida:  "))

    if opcao == 1:
      valor = int(input("Insira o valor que deseja: "))
      rbTree.Insert(valor)
      print("{} inserido com sucesso!".format(valor))

    elif opcao == 2:
      valor = int(input("Insira o valor que deseja: "))
      if rbTree.Search(valor) == True:
        print("Valor nao encontrado!")
        print("")
      else:
        rbTree.Delete(valor)
        print("{} removido!".format(valor))
        print("")

    elif opcao == 3:
      valor = int(input("Insira o valor que deseja: "))
      if rbTree.Search(valor) == True:
        print("Valor nao encontrado")
        print("")
      else:
        print("Valor encontrado!")
        print("")
    
    elif opcao == 4:
      rbTree.Show()
      print("")

    elif opcao == 5:
      break
