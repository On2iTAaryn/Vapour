import os,sys,pygame,math,random

class Missile:
    def __init__(self,startX,startY,passed_surface,trackingPos=(0,0)):
        self.x = startX
        self.y = startY
        self.surface = passed_surface
        self.rotation = 0
        self.trackX, self.trackY = trackingPos
        self.trail = []
        self.speed = 10
        self.width,self.height = (40,30)
        self.loadSprites()

    def loadSprites(self):
        self.sprite_missile = pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/missile.png").convert_alpha(),(self.width,self.height)),True,False)

    def draw(self):
        x,y,c = (0,1,2)
        for point in self.trail:
            pygame.draw.circle(self.surface,(255,255,0),(int(point[x]+random.randint(-2,2)),int(point[y]+random.randint(-2,2))),int(15-point[c]))
            point[c]+=0.5
            if(point[c] >= 15):
                self.trail.remove(point)
        self.surface.blit(pygame.transform.rotate(self.sprite_missile,self.rotation),(self.x,self.y))

    def update(self):
        self.track()
        self.trail.append([self.x+int(self.width/2),self.y+int(self.height/2),0])

    def track(m):
        diffX = m.trackX - m.x
        diffY = m.trackY - m.y
        m.rotation = -math.degrees(math.atan2(diffY,diffX))
        velX = m.speed*((90-math.fabs(m.rotation))/90)
        velY = 0
        if(-m.rotation < 0):
            velY = -m.speed+math.fabs(velX)
        else:
            velY = m.speed-math.fabs(velX)
        m.x+=velX
        m.y+=velY

    def setTarget(self,targetPos):
        self.trackX,self.trackY = targetPos