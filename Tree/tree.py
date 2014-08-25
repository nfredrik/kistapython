import collections.abc
import weakref
class TreeNode:
    """..   TODO:: weakref to the tree; tree has the key() function."""
    def __init__( self, item, less=None, more=None, parent=None ):
        self.item= item
        self.less= less
        self.more= more
        if parent != None:
            self.parent = parent
    @property
    def parent( self ):
        return self.parent_ref()
    @parent.setter
    def parent( self, value ):
        self.parent_ref= weakref.ref(value)
    def __repr__( self ):
        return( "TreeNode({item!r},{less!r},{more!r})".format( **self.__dict__ ) )
    def find( self, item ):
        if self.item is None: # Root
            if self.more: return self.more.find(item)
        elif self.item == item: return self
        elif self.item > item and self.less: return self.less.find(item)
        elif self.item < item and self.more: return self.more.find(item)
        raise KeyError
    def __iter__( self ):
        if self.less:
            for item in iter(self.less):
                yield item
        yield self.item
        if self.more:
            for item in iter(self.more):
                yield item
    def add( self, item ):
        if self.item is None: # Root Special Case
            if self.more:
                self.more.add( item )
            else:
                self.more= TreeNode( item, parent=self )
        elif self.item >= item:
            if self.less:
                self.less.add( item )
            else:
                self.less= TreeNode( item, parent=self )
        elif self.item < item:
            if self.more:
                self.more.add( item )
            else:
                self.more= TreeNode( item, parent=self )
    def remove( self, item ):
        # Recursive search for node
        if self.item is None or item > self.item:
            if self.more:
                self.more.remove(item)
            else:
                raise KeyError
        elif item < self.item:
            if self.less:
                self.less.remove(item)
            else:
                raise KeyError
        else: # self.item == item
            if self.less and self.more: # Two children are present
                successor = self.more._least()
                self.item = successor.item
                successor.remove(successor.item)
            elif self.less:   # One child on less
                self._replace(self.less)
            elif self.more:  # On child on more
                self._replace(self.more)
            else: # Zero children
                self._replace(None)
    def _least(self):
        if self.less is None: return self
        return self.less._least()
    def _replace(self,new=None):
        if self.parent:
            if self == self.parent.less:
                self.parent.less = new
            else:
                self.parent.more = new
        if new is not None:
            new.parent = self.parent

class Tree(collections.abc.MutableSet):
    def __init__( self, iterable=None ):
        self.root= TreeNode(None)
        self.size= 0
        if iterable:
            for item in iterable:
                self.root.add( item )
                self.size += 1
    def add( self, item ):
        self.root.add( item )
        self.size += 1
    def discard( self, item ):
        try:
            self.root.more.remove( item )
            self.size -= 1
        except KeyError:
            pass
    def __contains__( self, item ):
        try:
            self.root.more.find( item )
            return True
        except KeyError:
            return False
    def __iter__( self ):
        for item in iter(self.root.more):
            yield item
    def __len__( self ):
        return self.size

bt= Tree()
bt.add( "Number 1" )
print( list( iter(bt) ) )
bt.add( "Number 3" )
print( list( iter(bt) ) )
bt.add( "Number 2" )
print( list( iter(bt) ) )
print( repr(bt.root) )
print( "Number 2" in bt )
print( len(bt) )
bt.remove( "Number 3" )
print( list( iter(bt) ) )
bt.discard( "Number 3" ) # Should be silent
try:
    bt.remove( "Number 3" )
    raise Exception( "Fail" )
except KeyError as e:
    pass # Expected
bt.add( "Number 1" )
print( list( iter(bt) ) )

import random
for i in range(25):
    values= ['1','2','3','4','5']
    random.shuffle( values )
    bt= Tree()
    for i in values:
        bt.add(i)
    assert list( iter(bt) ) == ['1','2','3','4','5'], "IN: {0}, OUT: {1}".format(values,list( iter(bt) ))
    random.shuffle(values)
    for i in values:
        bt.remove(i)
        values.remove(i)
        assert list( iter(bt) ) == list(sorted(values)), "IN: {0}, OUT: {1}".format(values,list( iter(bt) ))

s1 = Tree( ["Item 1", "Another", "Middle"] )
s2 = Tree( ["Another", "More", "Yet More"] )
print( list( iter(bt) ) )
print( list( iter(bt) ) )
print( list( iter(s1|s2) ) )
