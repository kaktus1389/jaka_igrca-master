import pygame
from models import SIRINA_EKRANA, VISINA_EKRANA
from main import main
pygame.font.init()
def mainMenu():
    pygame.font.init()
    ekran = pygame.display.set_mode([SIRINA_EKRANA,VISINA_EKRANA])
    pygame.display.set_caption("jaka igrca menu")
    list =["Play","Maps","Options","Quit"]        
    itemFont = pygame.font.Font(None,35)
    settingsFont= pygame.font.Font(None,72)
    ItemY = VISINA_EKRANA/12
    konec_zanke = False
    selectorY= 0
    pozen_main = False
    clock = pygame.time.Clock()
    while not konec_zanke:
        clock.tick(60)
        for dogodek in pygame.event.get():
            if dogodek.type == pygame.QUIT:
                konec_zanke = True
            elif dogodek.type == pygame.KEYDOWN:
                if dogodek.key == pygame.K_UP:
                    if selectorY==0:
                        pass
                    else:
                        selectorY = selectorY-1
                elif dogodek.key == pygame.K_DOWN:
                    if selectorY ==3:
                        pass
                    else:
                        selectorY = selectorY+1
                elif dogodek.key ==pygame.K_RETURN:
                    if selectorY == 3:
                        konec_zanke = True
                    if selectorY == 0:
                       pozen_main = True 
                    if pozen_main == True:
                        main()                       
        settings = settingsFont.render("S E T T I N G S",1,(255,255,255))
        settingsPos = settings.get_rect()
        settingsPos.centerx = SIRINA_EKRANA/2
        ekran.fill((61,118,211))
        ekran.blit(settings,settingsPos)
        for i in range(len(list)):
            listItem = itemFont.render(list[i],True,(255,255,255))
            listItemPos = listItem.get_rect()
            listItemPos.centerx = SIRINA_EKRANA/2
            if i == 0:
                listItemPos.centery = 100
            else:
                listItemPos.centery = 100+(i*ItemY)
            ekran.blit(listItem,listItemPos)
        selector = itemFont.render("->",1,(225,225,225))
        selectorPos = selector.get_rect()
        selectorPos.centerx = SIRINA_EKRANA/3 
        selectorPos.centery = 100 + selectorY*ItemY
        ekran.blit(selector,selectorPos)
        pygame.display.flip()
    pygame.quit()
mainMenu()
