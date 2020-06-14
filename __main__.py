from src.engine.base.game import Game
from src.engine.tree.node import Node
from src.engine.tree.sprite_node import SpriteNode
from src.truckdriver.player import Player
from src.engine.base.physics_server import PhysicsServer
import pyglet
import pymunk
import pymunk.pyglet_util
from src.truckdriver.arenas import Arena1, Arena2, Arena3
from src.truckdriver.marker import Marker
from src.truckdriver.win_banner import WinBanner
from src.truckdriver.game_over import GameOver
class TruckDriver:
    def __init__(self):
        self.window : pyglet.window.Window = pyglet.window.Window(640 , 480)
        self.options = pymunk.pyglet_util.DrawOptions()
        pyglet.gl.glScalef(4.0, 4.0, 4.0);
        self.setup_level(1)
        self.end_timer = 0
        self.end_time = 1
        self.current_level = 1


    def setup_level(self, level: int):
        physics_server = PhysicsServer.instance()
        physics_server._space = pymunk.Space()
        self.player = Player()
        if level == 2:
            self.scenario = Arena2()
            self.marker = Marker((101,91), False)
        elif level == 3:
            self.scenario = Arena3()
            self.marker = Marker((9,97), False)
        else:
            self.scenario = Arena1()
            self.marker = Marker((54,47), True)
        self.banner = WinBanner()
        self.game_over = GameOver()
        self.won = False
        self.lost = False
        self.window.push_handlers(self.player.keys)

    def update(self, delta : float):
        if not self.won and not self.lost:
            self.scenario.update(delta)
            self.player.update(delta)
            self.marker.update(delta)
            self.banner.update(delta, self.marker.check_win(self.player.cont_body))
            self.game_over.update(delta, self.player.damage)
            physics_server = PhysicsServer.instance()
            physics_server.step(delta)
            self.won = self.banner.won
            self.lost = self.game_over.lost
            if self.won:
                self.lost = False
        if self.won:
            self.banner.update(delta, self.marker.check_win(self.player.cont_body))
            self.end_timer+=delta
        if self.lost:
            self.game_over.update(delta, self.player.damage)
            self.end_timer+=delta
        if self.end_timer > self.end_time:
            self.end_timer = 0
            if self.won:
                self.current_level+=1
            self.setup_level(self.current_level)


    def draw(self):
        self.window.clear()
        physics_server = PhysicsServer.instance()
        #physics_server._space.debug_draw(self.options)
        self.scenario.draw()
        self.marker.draw()
        self.player.draw()
        if not self.lost:
            self.banner.draw()
        if not self.won:
            self.game_over.draw()
        #physics_server._space.debug_draw(self.options)
        
        

game = TruckDriver()
@game.window.event
def on_draw():
    game.draw()
pyglet.clock.schedule_interval(game.update, 1.0/60)
        
pyglet.app.run()