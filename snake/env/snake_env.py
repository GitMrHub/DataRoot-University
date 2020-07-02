import gym
from gym import spaces
import numpy as np

from .core.world import World
from .utils.renderer import Renderer
from settings.constants import SIZE

'''
    Configurable single snake environment.
    Parameters:
        - SIZE: size of the world
        - OBSERVATION_MODE: return a raw observation (block ids) or RGB observation
        - OBS_ZOOM: zoom the observation (only for RGB mode, FIXME)
'''


class SnakeEnv(gym.Env):
    metadata = {
        'render': ['human', 'rgb_array'],
        'observation.types': ['raw', 'rgb']
    }

    def __init__(self, size=SIZE, render_zoom=20, custom=False, start_position=None, start_direction_index=None,
                 food_position=None):
        # for custom init
        self.custom = custom
        self.start_position = start_position
        self.start_direction_index = start_direction_index
        self.food_position = food_position
        #  Set size of the game world
        self.SIZE = size
        # Create world
        self.world = World(self.SIZE, self.custom, self.start_position, self.start_direction_index, self.food_position)
        # Init current step for future usage
        self.current_step = 0
        # Init alive flag
        self.alive = True
        # Observation space
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(self.SIZE[0], self.SIZE[1]),
                                            dtype=np.uint8)
        # Action space
        self.action_space = spaces.Discrete(len(self.world.DIRECTIONS))
        #  Set renderer
        self.RENDER_ZOOM = render_zoom
        self.renderer = None

    def step(self, action):
        """
        Execute action
        @param action: int
        @return: np.array (observation after the action), int (reward), bool ('done' flag), np.array (snake)
        """
        # Check if game is ended
    #   if not self.alive: self.render(mode='rgb_array')
        # Perform the action
        reward, done, snake = self.world.move_snake(action)
        # Disable interactions if snake dead
    #  if done:self.render(mode='rgb_array')
        return self.world.get_observation(), reward, done, snake

    def reset(self, ):
        """
        Reset environment to the initial state
        @return: initial observation
        """
        # Reset step counters
        self.current_step = 0
        # Set 'alive' flag
        self.alive = True
        # Create world
        self.world = World(self.SIZE, self.custom, self.start_position, self.start_direction_index, self.food_position)
        return self.world.get_observation()

    def render(self, mode='human', close=False):
        """
        Render environment depending on the mode
        @param mode: str
        @param close: bool
        @return: np.array
        """
        if not close:
            # Renderer lazy loading
            if self.renderer is None:
                self.renderer = Renderer(size=self.SIZE, zoom_factor=self.RENDER_ZOOM)
            return self.renderer.render(self.world.get_observation(), mode=mode, close=False)

    def close(self):
        """
        Close rendering
        """
        if self.renderer:
            self.renderer.close()
            self.renderer = None