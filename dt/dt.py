
import json

class Tree(object):
    def __init__(self, name, nodeList):
        self.name = name
        self.nodelist = nodeList

    def old_get_nodeList(self):
        return self.nodelist


    def get_nodeList(self):
        print self.name
        print '{\n'
        for node in self.nodelist:
            node(1)
        print '};\n'



class Node(object):
    def __init__(self, name, nodeList=[]):
        self.ndict = {}
        self.name = name
        self.nodelist = nodeList
    def __call__(self,i):
        self.get_properties_r(i)

    def get_name(self):
        return self.name

    def set_property(self, key, value):
        self.ndict[key] = value

    def get_propeterty(self,key):
        if key in self.ndict:
            self.ndict[key] = value
        return None

    def get_properties(self, indent):
        print ' '*4*indent,self.get_name()
        print ' '*4*indent,'{'
        for i in self.ndict:
            print ' '*8*indent,i,  self.ndict[i]

        for node in self.nodelist:
            node.get_properties(2)

        print ' '*4*indent, '};','\n'


    def get_properties_r(self, indent):
        print ' '*4*indent,self.get_name()
        print ' '*4*indent,'{'
        for i in self.ndict:
            print ' '*8*indent,i,  self.ndict[i]

        for node in self.nodelist:
            node(indent+1)

        print ' '*4*indent, '};','\n'

n1 = Node('nisse1')

n1.set_property('nyckel1',01234)
n1.set_property('nyckel2',01235)

n2 = Node('nisse2')

n3 = Node('nisse3')
n3.set_property('nyckel2',01235)
nn = Node('nissen')
nn.set_property('nyckel33',01235)
n4 = Node('nisse4',[nn])
n4.set_property('nyckel24',[01235, 1234])

n5 = Node('nisse5', [n3,n4])

n2.set_property('nyckel24',[01235, 1234])

nlist = [n1, n2,n5]

tree = Tree('Fredde',nlist)

tree.get_nodeList()


