from os.path import join

from Minecraft.gui.frame import Frame
from Minecraft.gui.widget.image import Image
from Minecraft.source import path
from Minecraft.utils.utils import *

import pyglet
from pyglet import image
# 0 90 176 166
# 264 249(1.5x)

class Bag():

    def __init__(self, game):
        width, height = get_size()
        self.game = game
        self.frame = Frame(self.game, True)
        self._bag = Image((width - 264) / 2, (height - 249) / 2,
                image.load(join(path['texture.gui'], 'containers', 'inventory.png')).get_region(0, 90, 176, 166))
        self._bag.sprite.scale = 1.5

        def on_resize(width, height):
            self._bag.sprite.position = (width - 264) / 2, (height - 249) / 2

        self.frame.register_event('resize', on_resize)
        self.frame.add_widget(self._bag)
