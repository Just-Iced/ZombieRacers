import pygame
from pygame.math import Vector2
from Engine.gameObject import GameObject
from Engine.physicsObject import ColliderState


#physics calculations
class Physics:
    def __init__(self, entities):
        self.entities: list = entities
        self.simulated = []
        
        for entity in self.entities:
            if entity.physics:
                if entity.physics.simulate == True:
                    self.simulated.append(entity)
            else:
                pass
                
    def update(self):
        self.simulated = []
        
        for entity in self.entities:
            callOverlap = False
            callHit = False
            if entity.physics.simulate == True:
                self.simulated.append(entity)
                
        for e in self.simulated:
            entity: GameObject = e
        
            lastPos = entity.transform.pos
            entity.physics.velocity.y = min(10, entity.physics.velocity.y + (0.1*entity.physics.scale))
            pY = entity.transform.pos.y + entity.physics.velocity.y * entity.main.dt
            pX = entity.transform.pos.x + entity.physics.velocity.x * entity.main.dt
            direction = Vector2(pX, pY) - lastPos
            
            colliding = {"up": False, "down": False, "right": False, "left": False}   
            
            #apply x             transform
            entity.transform.pos.x += (entity.physics.velocity.x * entity.main.dt)
            entity.physics.update()
            for collider in entity.main.colliders: 
                if entity.physics.collider.colliderect(collider.collider) and collider.collider != entity.physics.collider:

                    if entity.physics.colliderState == ColliderState.Block and collider.colliderState == ColliderState.Block:
                        if direction.x < 0:
                            entity.physics.collider.left = collider.collider.right
                            colliding["left"] = True
                        if direction.x > 0:
                            entity.physics.collider.right = collider.collider.left
                            colliding["right"] = True
                        
                        if colliding["left"] or colliding["right"]:
                            entity.transform.pos.x = entity.physics.collider.x + (entity.transform.scale.x // 2)
                            entity.physics.velocity.x = entity.physics.minVel.x
                            callHit = True
                    
                    if entity.physics.colliderState == ColliderState.Overlap and collider.colliderState != ColliderState.Blank:
                        callOverlap = True
                        
                        
            entity.transform.pos.y += (entity.physics.velocity.y * entity.main.dt)
            entity.physics.update()
            for collider in entity.main.colliders:  
                if entity.physics.collider.colliderect(collider.collider) and collider.collider != entity.physics.collider:

                    if entity.physics.colliderState == ColliderState.Block and collider.colliderState == ColliderState.Block:
                        if direction.y < 0:
                            entity.physics.collider.top = collider.collider.bottom
                            colliding["up"] = True
                        if direction.y > 0:
                            entity.physics.collider.bottom = collider.collider.top
                            colliding["down"] = True                   
                        
                        if colliding["up"] or colliding["down"]:
                            entity.transform.pos.y = entity.physics.collider.y + (entity.transform.scale.y // 2)
                            entity.physics.velocity.y = entity.physics.minVel.y
                            callHit = True
                            
                    if entity.physics.colliderState == ColliderState.Overlap and collider.colliderState != ColliderState.Blank:
                        callOverlap = True
                        
            if callOverlap == True:
                entity.physics.overlapEvent()
            elif callHit == True:
                entity.physics.hitEvent()