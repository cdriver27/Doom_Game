from sprite_object import *
from npc import *
from random import choices, randrange


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.animated_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        # sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(9.5, 7.5)))

        # npc map
        add_npc(NPC(game))
        add_npc(NPC(game, pos=(11.5, 4.5)))
        # npc map
        add_npc(SoldierNPC(game, pos=(11.0, 19.0)))
        add_npc(SoldierNPC(game, pos=(11.5, 4.5)))
        add_npc(SoldierNPC(game, pos=(13.5, 6.5)))
        add_npc(SoldierNPC(game, pos=(2.0, 20.0)))
        add_npc(SoldierNPC(game, pos=(4.0, 29.0)))
        add_npc(CacoDemonNPC(game, pos=(5.5, 14.5)))
        add_npc(CacoDemonNPC(game, pos=(5.5, 16.5)))
        add_npc(CyberDemonNPC(game, pos=(14.5, 25.5)))

    def spawn_npc(self):
        for i in range(self.enemies):
                npc = choices(self.npc_types, self.weights)[0]
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                    pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()
            self.check_win()
    
    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list }
        [sprite.update() for sprite in self.sprite_list]
        # call update for all enemies on this list
        [npc.update() for npc in self.npc_list]
    
    # for conveinece we will make method to add npc
    def add_npc(self, npc):
        self.npc_list.append(npc)
        

    # method to add sprites to the sprite list
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)