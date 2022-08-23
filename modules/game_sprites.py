import pygame 
import modules.settings as settings

pygame.init()
width_table = 420
end_game = False
#
list_cross = []
list_apple = []
list_win_cor = []
list_win = [0,0,0,
            0,0,0,
            0,0,0]

class Sprite(settings.Settings):
    def __init__(self, obj = None, **kwargs):
        super().__init__(**kwargs)
        self.SHOW = False
        self.OBJECT = obj

    def show(self, window, index):
        if self.SHOW:
            self.blit_sprite(window)
            if self.OBJECT == "CROSS":
                list_win[index] = 1
            elif self.OBJECT == "APPLE":
                list_win[index] = 2


table = Sprite(
    x = settings.list_settings_window[0] // 2 - width_table // 2,
    y = settings.list_settings_window[1] // 2 - width_table // 2,
    width= width_table,
    height= width_table,
    name= 'images/1.png'
)

def create_sprites(name_list, name_img, name_obj):
    x = 20
    y = 20
    for num in range(3):
        for num1 in range(3):
            obj = Sprite(
                obj= name_obj,
                x = x,
                y = y,
                width = 100,
                height = 100,
                name = name_img
            )
            name_list.append(obj)
            x += obj.WIDTH + 40
        x = 20
        y += name_list[0].HEIGHT + 40

create_sprites(list_cross, 'images/cross.png', "CROSS")
create_sprites(list_apple, 'images/apple.png', "APPLE")

def victory(index1, index2, index3, value):
    global end_game
    if list_win[index1] == value and list_win[index2] == value and list_win[index3] == value:
        end_game = True
        list_win_cor.extend([list_cross[index1], list_cross[index3]])
        if value == 1:
            print("Победили крестики")
        elif value == 2:
            print("Победили нолики!")
    elif not end_game and not 0 in list_win:
        print("Ничья")