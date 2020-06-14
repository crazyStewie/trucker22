from src.engine.base.game import Game
from src.engine.tree.node import Node
from src.engine.tree.sprite_node import SpriteNode
from src.truckdriver.player import Player
from src.engine.base.physics_server import PhysicsServer
import pyglet
import pymunk
import pymunk.pyglet_util
from src.truckdriver.scenario import Scenario
from src.truckdriver.marker import Marker
from src.truckdriver.win_banner import WinBanner
from src.truckdriver.game_over import GameOver
class TruckDriver:
    def __init__(self):
        self.window : pyglet.window.Window = pyglet.window.Window(640 , 480)
        self.player = Player()
        self.options = pymunk.pyglet_util.DrawOptions()
        self.window.push_handlers(self.player.keys)
        pyglet.gl.glScalef(4.0, 4.0, 4.0);
        self.scenario = Scenario()
        self.marker = Marker((54, 47))
        self.banner = WinBanner()
        self.game_over = GameOver()
        self.won = False
        self.lost = False

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
        if self.lost:
            self.game_over.update(delta, self.player.damage)


    def draw(self):
        self.window.clear()
        #physics_server = PhysicsServer.instance()
        #physics_server._space.debug_draw(self.options)
        self.scenario.draw()
        self.marker.draw()
        self.player.draw()
        if not self.lost:
            self.banner.draw()
        if not self.won:
            self.game_over.draw()
        
        

game = TruckDriver()
@game.window.event
def on_draw():
    game.draw()
pyglet.clock.schedule_interval(game.update, 1.0/60)
        
pyglet.app.run()