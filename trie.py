class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfString=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insertString(self,word):
        current=self.root
        for i in word:
            ch=i
            node=current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.children.update({ch:node})
            current=node
        current.endOfString=True
    def search(self,word):
        current=self.root
        for i in word:
            node=current.children.get(i)
            if node==None:
                return False
            current=node
        if current.endOfString==True:
            return True
        else:
            return False
        


def delete(root,word,index):
    ch=word[index]
    current=root.children.get(ch)
    nodedelete=False
    if len(current.children)>1:
        delete(current,word,index+1)
        return False
    if index==len(word)-1:
        if len(current.children)>=1:
            current.endOfString=False
            return False
        else:
            root.children.pop(ch)
            return True
    if current.endOfString==True:
        delete(current,word,index+1)
        return False
    nodedelete=delete(current,word,index+1)
    if nodedelete==True:
        root.children.pop(ch)
        return True
    else:
        return False
    
          


        
newTrie=Trie()
newTrie.insertString("app")
newTrie.insertString("api")
print(delete(newTrie.root,"app",0))
print(newTrie.search("ap"))