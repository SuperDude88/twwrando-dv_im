from class_creator.class_ms import *
from collections import OrderedDict, deque
#import random
from random import Random
import randomizer

#   Created by CrainWWR    in   Java
#Translated by DualVission into Python
# Corrected by tanjo3      for  Python

class Graph:
  class Node :
    class Edge:
      def __int__(self,source,destination,multiDirectional):
        self.source = source
        self.destination = destination
        self.multiDirectional = multiDirectional

      def __repr__(self):
        return "{}, {}, {}".format(self.source,self.destination,self.multiDirectional)

      def __str__(self):
        return f"|| Source: {self.source}, Destination: {self.destination}, MultiDirectional: {self.multiDirectional}"

    def __int__(self,nodeID: int,potLimit: int,edges: list,graph, visited=False):
      self.nodeID = nodeID
      self.potLimit = potLimit
      self.visited = visited
      self.edges = edges
      self.graph = graph

    def __eq__(self,other):
      return self.nodeID == other.nodeID

    def __repr__(self):
      edgeData = ""
      for edge in self.edges:
        edgeData+="\n-\t{}".format(repr(edge))
      return "{}: {}/{}{}".format(self.nodeID,len(self.edges),self.potLimit,edgeData)

    def __str__(self):
      header = f"NodeID: {self.nodeID}, Total Edge Capacity: {self.potLimit}, Edge Total: {len(self.edges)}"
      info = f"\n-- Visited: {self.visited}, Current Edge Capacity: {self.edgeCapacityLeft()}"
      edgeInfo = ""
      for edge in self.edges:
        edgeInfo += f"\t{str(edge)}

      return f"{header}\n{info}\n{edgeInfo}"

    def isHub(self) -> bool:
      return self.potLimit > 2

    def connectNodes(self,destination,rng: Random,multiDirectionalEdges: bool) -> bool:
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

    def findDescendant(self,descendantID: int) -> bool:
      self.visited = True
      if self.nodeID == descendantID :
        return True
      for children in self.edges:
        child = children.destination
        if(children.source == (self.nodeID and not self.graph.nodes[child].visited)):
          return self.graph.nodes[child].findDescendant(descendantID)
      return False

    def pingDescendants(self):
      self.visited = True
      for children in self.edges:
        child = children.destination
        if(children.source == (self.nodeID and not self.graph.nodes[child].visited)):
          self.graph.nodes[child].pingDescendants()

    def hasEdgeLeft(self) -> bool:
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
      if self.edgeCapacityLeft(self) == potLimit:
        return self.nodeID
      else:
        for edge in self.edges:
          if(nodes[self.graph.getIndex(edge.destination)].visited):
            continue
          return nodes[self.graph.getIndex(edge.destination)].findLeafChild()
      return self.nodeID

    def findHubLeafHelper(self,sourceID: int):
      if(self.isIsolated(self)):
        return self.nodeID
      for edge in self.edges:
        if(edge.source!=sourceID):
          return nodes[self.graph.getIndex(edge.destination)].findHubLeafHelper(self,self.nodeID)
      return self.nodeID

    def isIsolated(self) -> bool:
      return len(self.edges) == 0

  def __init__(self,nodeList,randomState: int, multiDirectionalEdges: bool,linear: bool):
    groupAmount = self._findPotentialAmount(nodeList)

    self.nodes = [None]*len(nodeList)
    self.rng = Random()
    self.rng.seed(RandomState)
    self.hubNodes = []

    if(groupAmount==0 or linear):
      node = []
      self.nodes[0] = self.Node(self,nodeList[0][0],1)
      for i in range(len(nodeList)-1):
        node.append(nodeList[i][0])
        self.nodes[i] = self.Node(self,nodeList[i][0],1)
      self.rng.shuffle(node)
      self.fillLinearEdgesWithStack(self,node,multiDirectionalEdges)
    else:
      for i in range(len(nodeList)):
        self.nodes[i] = self.Node(self,nodeList[i][0],nodeList[i][1])
      setHubNodes(self,self.rng)
      connectHubsToRoot(self,self.rng,multiDirectionalEdges)
      isolatedNodes = self.findIsolatedNodes(self)
      self.rng.shuffle(isolatedNodes)
      #bug is here v?
      self.connectIsolatedNodes(self,isolatedNodes,rng,multiDirectionalEdges)

  def __repr__(self):
    graphData = "{}"
    for node in self.nodes:
      graphData+="\n-{}".format(repr(node))

  def __str__(self):
    graphInfo = f"For the graph of size{len(self.nodes)},  the node information is as follows"

    nodeInfo = "\n-----"
    for node in self.nodes:
      nodeInfo += f"\n{str(node)}\n-----"

    return f"{graphInfo}{nodeInfo}"

  def setHubNodes(self):
    rng = self.rng
    hubTotal = getHubAmount()
    if( hubTotal < 5 ):
      rng.shuffle(hubNodes)
    else:
      rng.shuffle(hubNodes)
      self.hubNodes = self.hubNodes[floor(hubTotal**0.5):hubTotal]

  def getHubAmount(self):
    hubAmount = 0
    for node in self.nodes:
      if node.isHub() :
        hubAmount += 1
        self.hubNodes.append(node)
    return hubAmount

  def connectHubsToRoot(self,multiDirectionalEdges):
    hubNodeStack = deque()
    for node in self.hubNodes:
      if node!=self.nodes[0]:
        hubNodeStack.append(node.nodeID)
    if not multiDirectionalEdges:
      self.fillLinearEdgesWithStack(self,hubNodeStack,multiDirectionalEdges)
    else:
      fillLinearEdgesWithStackRandomEdges(hubNodeStack,self.rng)

  def findIsolatedNodes(self):
    isolatedNodes = deque()
    for node in self.nodes:
      if node.isIsolated() :
        isolatedNodes.append(node)
    return isolatedNodes

  def connectIsolatedNodes(self,isolatedNodes,multiDirectionalEdges: bool):
    self.unvisitNodes(self)
    for node in self.hubNodes:
      node.visited = True
    self.nodes[0].visited = True
    #Connects all Isolated Nodes in cycles to random hub nodes.
    while(len(isolatedNodes!=0):
      nextNode = isolatedNodes.pop()
      hubNode = self.rng.choice(self.hubNodes)
      hubChild = self.nodes[self.getIndex(hubNode.findHubLeaf())]
      if not hubChild.connectedNodes(nextNode, self.rng, multiDirectional):
        isolatedNodes.append(nextNode)
    for node in self.hubNodes:
      leafNode = self.nodes[self.getIndex(node.findLeafChild())]
      leafNode.connectNodes(node, self.rng, False)

  def findPotentialAmount(self) -> int:
    nodeList = self.nodes
    potLimit = 0
    for i in range(len(nodeList)):
      potLimit += nodeList[i][1]-1
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
    self.unvisitNodes()
    self.nodes[0].pingDescendants()
    for node in self.nodes :
      if not node.visited :
        return False
    return True

  def getIndex(self, nodeID: int) -> int:
    for i in range(len(self.nodes)):
      if nodes[i].nodeID == NodeID:
        return i
    return -1
