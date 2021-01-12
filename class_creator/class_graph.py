from class_creator.class_ms import *
from collections import OrderedDict, deque
import random
#from random import Random
Random = random.Random
import randomizer

class Graph:
  def __init__(self,nodes,rng,hubNodes):
    self.nodes = nodes
    self.rng = rng
    self.hubNodes = hubNodes

  def Graph(self,nodeList,RandomState,multiDirectionalEdges,linear):
    groupAmount = findPotentialAmount(nodeList)
    Random.setSeed(RandomState)
    nodes = Node[len(nodeList)] #???
    if(groupAmount==0 or linear):
      node = []
      nodes[0] = Node(nodeList[0][0],1)
      for i in range(len(nodeList)-1):
        node.append(nodeList[i][0]) #???
        nodes[i] = Node(nodeList[i][0],1)
      random.shuffle(node)
      fillLinearEdgesWithStack(self,node, multiDirectionalEdges)
    else:
      for i in range(len(nodeList)):
        nodes[i] = Node(nodeList[i][0],nodeList[i][1])
      setHubNodes(self,rng)
      connectHubsToRoot(self,rng,multiDirectionalEdges)
      isolatedNodes = findIsolatedNodes(self)
      random.shuffle(isolatedNodes)
      connectIsolatedNodes(self,isolatedNodes,rng,multiDirectionalEdges)

  def setHubNodes(self):
    rng = self.rng
    hubTotal,hubNodes = getHubAmount()
    if( hubTotal < 5 ):
      random.shuffle(hubNodes)
    else:
      random.shuffle(hubNodes)
      hubNodes.pop()             #???
      hubTotal -= 1

  def getHubAmount(self):
    hubAmount = 0
    for node in self.nodes:
      if node.isHub() :
        hubAmount += 1
        hubNodes.append(node)
    return hubAmount

  def connectHubsToRoot(self,multiDirectionalEdges):
    hubNodeStack = deque()
    for node in hubNodes:
      if hubNodes[node]==nodes[0]:
        continue
      else:
        hubNodeStack.append(node)
    if not multiDirectionalEdges:
      fillLinearEdgesWithStack(hubNodeStack,multiDirectionalEdges)
    else:
      fillLinearEdgesWithStackRandomEdges(hubNodeStack,self.rng)

  def findIsolatedNodes(self):
    isolatedNodes = deque()
    for node in self.nodes:
      if node.isIsolated() :
        isolatedNodes.append(node)
    return isolatedNodes

  def connectIsolatedNodes(self,isolatedNodes,multiDirectionalEdges):
    unvisitNodes()
    for node in hubNodes:
      node.visited = True
    self.nodes[0].visited = True
    #Connects all Isolated Nodes in cycles to random hub nodes.
    while(len(isolatedNodes!=0):
      nextNode = isolatedNodes.pop()
      hubNode = random.choice(hubNodes)
      hubChild = hubNode.findHubLeaf()
      if not hubChild.connectedNodes(nextNode, self.rng, multiDirectional):
        isolatedNodes.pop(isolatedNodes.index(nextNode))
      for node in hubNodes:
        leafNode = nodes[nodes.index(node.findLeafChild())]
        leafNode.connectNodes(node, self.rng, False)

  def findPotentialAmount(self,potLimit=0):
    nodeList = self.nodes
    for index in nodeList:
      potLimit += nodeList[index][1]-1
    return potLimit

  def findLinearEdgesWithStack(self,destinations, multiDirectionalEdges):
    while(len(destinations)!=0):
      nextDestination = destinations.pop()
      nextRootChild = nodes[0].finalLeafChild()
      nodes[nodes.index(lastRootChild)].insertEdge(nodes[0].nodeID, self.rng.nextBoolean())

  def unvisitNodes(self):
    for node in self.nodes:
      node.visited = False

  def verifyGraph(self):
    unvisitNodes
    nodes[0].pingDescendants()
    for node in self.nodes :
      if not node.visited :
        return False
    return True

  def getIndex(self, nodeID):
    for i in len(nodes):
      if nodes[index].nodeID == NodeID:
        return i

  class Node :
    def __int__(self,nodeID,potLimit,visited,edges,graph):
      self.nodeID = nodeID
      self.potLimit = potLimit
      self.visited = visited
      self.edges = edges
      self.graph = graph

    def isHub(self):
      if self.potLimit>2:
        return True
      return False

    def connectNodes(self,destination,rng,multiDirectionalEdges):
      if not multiDirectionalEdges:
        return insertEdge(destination.nodeID,multiDirectionalEdges)
      return insertEdge(destination.nodeID,rng.nextBoolean())

    def insertEdge(self,destination,multiDirectionalEdges=False):
      if(self.nodeID==destination or hasChild(destination)):
        return False
      if multiDirectionalEdges:
        newEdge = Edge(nodeID,destination,multiDirectionalEdges)
        nodes[getIndex(destination)].insertEdge(nodeID)
      else:
        newEdge = Edge(nodeID,destination,multiDirectionalEdges)
      return True

    def findDescendant(self,descendantID):
      self.visited = True
      if self.nodeID = descendantID :
        return True
      for children in self.edges:
        child = children.destination #Hmm
        if(children.source == (self.nodeID and not nodes[child].visited)):
          return nodes[child].findDescendant(descendantID)
      return False

    def pingDescendants(self):
      self.visited = True
      for children in self.edges:
        child = children.destination
        if(children.source == (self.nodeID and not nodes[child].visited)):
          nodes[child].pingDescendants()

    def hasEdgeLeft(self):
      currentEdgeAmount = 0
      for edge in self.edges:
        if(edge.source == self.nodeID):
          currentEdgeAmount+=1
      if(currentEdgeAmount==self.potLimit):
        return False
      return True

    def edgeCapacityLeft(self):
      currentEdgeAmount = 0
      for edge in self.edges:
        if edge.source == self.nodeID:
          currentEdgeAmount+=1
      return potLimit - currentEdgeAmount

    def hasChild(self,childID):
      for edge in self.edges:
        if(edge.source == NodeID and edge.destination == childID):
          return True
      return False

    def findLeafChild(self):
      self.visited = True
      if edgeCapacityLeft(self) == potLimit:
        return self.nodeID
      else:
        for edge in self.edges:
          if(nodes[self.graph.getIndex(edge.destination)].visited):
            continue
          return nodes[self.graph.getIndex(edge.destination)].findLeafChild()
      return self.nodeID

    def findHubLeafHelper(self,sourceID):
      if(self.edges.size()==0):
        return self.nodeID
      for edge in self.edges:
        if(edge.source!=sourceID):
          return nodes[self.graph.getIndex(edge.destination)].findHubLeafHelper()
      return self.nodeID

    def isIsolated(self):
      if(self.edges.size()==0):
        return True
      return False

  class Edge:
    def __int__(self,source,destination,multiDirectional):
      self.source = source
      self.destination = destination
      self.multiDirectional = multiDirectional
