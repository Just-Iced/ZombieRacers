import pygame
from pygame.math import Vector2
from enum import Enum

class ColliderState(Enum):
    Blank = 1
    Overlap = 2
    Block = 3
class Event(object):
 
    def __init__(self):
        self.__eventhandlers = []
 
    def __iadd__(self, handler):
        self.__eventhandlers.append(handler)
        return self
 
    def __isub__(self, handler):
        self.__eventhandlers.remove(handler)
        return self
 
    def __call__(self, object, *args, **keywargs):
        for eventhandler in self.__eventhandlers:
            eventhandler(object, *args, **keywargs)

#physics object class
class PhysicsObject:
    def __init__(self, owner, simulate, gravityScale, initVelocity = Vector2(0,0)):
        self.owner = owner
        self.simulate = simulate
        self.scale = gravityScale
        self.velocity = initVelocity
        self.minVel = Vector2(0,0)
        self.collider = pygame.Rect(self.owner.transform.pos.x - (self.owner.transform.scale.x // 2),self.owner.transform.pos.y - (self.owner.transform.scale.y // 2),self.owner.transform.scale.x, self.owner.transform.scale.y)
        self.colliderState = ColliderState(ColliderState.Blank)
        self.overlappingObject = None
        
        self.overlapEvent = Event()
        self.hitEvent = Event()
        
        self.owner.main.colliders.append(self)
        
    def update(self):
        self.collider.x, self.collider.y = self.owner.transform.pos.x - (self.owner.transform.scale.x // 2), self.owner.transform.pos.y - (self.owner.transform.scale.y // 2)
        
    def addVelocity(self, vel = Vector2(0,0)):
        self.velocity -= vel
        
    def setVelocity(self, vel = Vector2(0,0)):
        self.velocity = vel
        
    #assign event to Begin Overlap
    def AddSubscribersForCollisionEvent(self,objMethod):
        self.overlapEvent += objMethod
    
    #remove event from Begin Overlap
    def RemoveSubscribersForCollisionEvent(self,objMethod):
        self.overlapEvent -= objMethod

    #assign event to Begin Overlap
    def AddSubscribersForHitEvent(self,objMethod):
        self.hitEvent += objMethod
    
    #remove event from Begin Overlap
    def RemoveSubscribersForHitEvent(self,objMethod):
        self.hitEvent -= objMethod