import pygame
import modules.settings as settings
import modules.game_sprites as sprites

pygame.init()

window = pygame.display.set_mode(settings.list_settings_window)

def run_game():
    clock = pygame.time.Clock()
    game = True
    step = 0
    while game:

        sprites.table.blit_sprite(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

            if not sprites.end_game:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 0 in sprites.list_win:
                    x, y = event.pos

                    if step % 2 == 0:
                        list_name = sprites.list_cross
                    elif step % 2 != 0:
                        list_name = sprites.list_apple

                    for obj in list_name:
                        if obj.RECT.collidepoint(x,y):
                            index = list_name.index(obj)
                            print(sprites.list_win)
                            if sprites.list_win[index] == 0:
                                obj.SHOW = True
                                step += 1
                #                
                sprites.victory(0,1,2,1)
                sprites.victory(3,4,5,1)
                sprites.victory(6,7,8,1)
                sprites.victory(0,3,6,1)
                sprites.victory(1,4,7,1)
                sprites.victory(2,5,8,1)
                sprites.victory(0,4,8,1)
                sprites.victory(2,4,6,1)
                #
                sprites.victory(0,1,2,2)
                sprites.victory(3,4,5,2)
                sprites.victory(6,7,8,2)
                sprites.victory(0,3,6,2)
                sprites.victory(1,4,7,2)
                sprites.victory(2,5,8,2)
                sprites.victory(0,4,8,2)
                sprites.victory(2,4,6,2)
        
        for cross in sprites.list_cross:
            index = sprites.list_cross.index(cross)
            cross.show(window, index)
        for apple in sprites.list_apple:
            index = sprites.list_apple.index(apple)
            apple.show(window, index)
        
        if sprites.end_game:
            list = sprites.list_win_cor
            pygame.draw.line(window, (255,0,0), (list[0].X, list[0].Y + 50), (list[1].X + 100, list[1].Y + 50), 5)

        clock.tick(60)
        pygame.display.flip()

run_game()