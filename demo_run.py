import os, sys, pygame,levelEditor

pygame.init()
screen_width, screen_height = 500,500
screen = pygame.display.set_mode((screen_width,screen_height))
lEditor = levelEditor.LevelEditor(screen)
print("created level editor")
quit = False

while(not quit):
    pygame.time.Clock().tick(30)

    for e in pygame.event.get():
        if(e.type == pygame.KEYDOWN):
            if(e.key == pygame.K_ESCAPE):
                quit = True
        if(e.type == pygame.QUIT):
            quit = True
    
    screen.fill(0)
    lEditor.draw()
    pygame.display.flip()