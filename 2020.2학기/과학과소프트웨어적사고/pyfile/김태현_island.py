class Node:
    def __init__(self, name, left=None, right = None):
        self.name = name
        self.left = left
        self.right = right

class Map:
    def __init__(self):
        self.n1 = Node('H')
        self.n2 = Node('F')
        self.n3 = Node('S')
        self.n4 = Node('U')
        self.n5 = Node('E')
        self.n6 = Node('Z')
        self.n7 = Node('K')
        self.n8 = Node('N')
        self.n9 = Node('A')
        self.n10 = Node('Y')
        self.n11 = Node('T')

        self.n1.left = self.n2
        self.n1.right = self.n3
        self.n2.left = self.n4
        self.n2.right = self.n5
        self.n3.left = self.n6
        self.n3.right = self.n7
        self.n4.left = self.n8
        self.n5.left = self.n9
        self.n7.right = self.n10
        self.n9.right = self.n11

    def mapping(self):
        return self.n1

class Course:

    def __init__(self):
        pass
    
    def A_course(self,n):
        if n!= None:
            print(n.name, '-> ', end='')
            self.A_course(n.left)
            self.A_course(n.right)
            
    def B_course(self,n):
        if n!= None:
            self.B_course(n.left)
            print(n.name, '-> ', end='')
            self.B_course(n.right)

    def C_course(self,n):
        if n!= None:
            self.C_course(n.left)
            self.C_course(n.right)
            print(n.name, '-> ', end='')

class Main:
    def __init__(self):
        self.start = Map().mapping()
        self.course = Course()

    def run(self):
        print("A-코스:\t", end='')
        self.course.A_course(self.start)
        print('')
        
        print("B-코스:\t", end='')
        self.course.B_course(self.start)
        print('')
        
        print("C-코스:\t", end='')
        self.course.C_course(self.start)
        print('')
        
main = Main()
main.run()
    
    
