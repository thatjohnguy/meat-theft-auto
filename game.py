import pygame

WIDTH,HEIGHT=500,500
WHITE=(255,255,255)
FPS=60
VEL=2
BOY1=pygame.image.load('boy.png')
BOY2=pygame.image.load('boy2.png')
BOY1=pygame.transform.scale(BOY1,(50,50))
BOY2=pygame.transform.scale(BOY2,(70,70))
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Meat Theft Auto")

def draw_window(b1,b2):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,(0,0,0),pygame.Rect(250,0,2,500))
    WIN.blit(BOY1,(b1.x,b1.y))
    WIN.blit(BOY2,(b2.x,b2.y))
    pygame.display.update()
    
def boy_movement(key_pressed,b1):
    if key_pressed[pygame.K_d] and b1.x<200:
        b1.x+=VEL
    elif key_pressed[pygame.K_a] and b1.x>-1:
        b1.x-=VEL
    elif key_pressed[pygame.K_w] and b1.y>-1:
        b1.y-=VEL
    elif key_pressed[pygame.K_s] and b1.y<450:
        b1.y+=VEL

def main():
    b1=pygame.Rect(0,0,50,50)
    b2=pygame.Rect(0,0,50,50)
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        key_pressed=pygame.key.get_pressed()
        boy_movement(key_pressed,b1)

       
       
        
        draw_window(b1,b2)

    pygame.quit()
if __name__=="__main__":
    main()