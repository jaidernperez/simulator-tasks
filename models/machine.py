class machine:
  def _init_(self,id,name,state):
    self.id =id
    self.name =name
    self.state= state
    
  def getId(self):
    return self.id
  def getName(self):
    return self.name
  def getState(self):
    return self.state
