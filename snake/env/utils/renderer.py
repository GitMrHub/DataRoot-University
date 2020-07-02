import numpy as np


class SnakeColor:
    def __init__(self, body_color, head_color):
        self.body_color = body_color
        self.head_color = head_color

class Colored:
    """
    Translate the world state with block ids into an RGB image
    Return an RGB observation or render the world
    """
    def __init__(self, size, zoom_factor):
        # Setting default colors
        self.snake_colors = SnakeColor((0, 204, 0), (0, 77, 0))
        self.zoom_factor = zoom_factor
        self.size = size
        self.height = size[0]
        self.width = size[1]

    def get_color(self, state):
        # Void => BLACK
        if state == 0:
            return 0, 0, 0
        # Wall => WHITE
        elif state == 255:
            return 255, 255, 255
        # Food => RED
        elif state == 64:
            return 255, 0, 0
        else:
            is_head = (state - 100) % 2
            if is_head == 0:
                return self.snake_colors.body_color
            else:
                return self.snake_colors.head_color

    def get_image(self, state):
        # Transform to RGB image with 3 channels
        color_lu = np.vectorize(lambda x: self.get_color(x), otypes=[np.uint8, np.uint8, np.uint8])
        _img = np.array(color_lu(state))
        # Zoom every channel
        _img_zoomed = np.zeros((3, self.height * self.zoom_factor, self.width * self.zoom_factor), dtype=np.uint8)
        for c in range(3):
            for i in range(_img.shape[1]):
                for j in range(_img.shape[2]):
                    _img_zoomed[c, i * self.zoom_factor:i * self.zoom_factor + self.zoom_factor,
                    j * self.zoom_factor:j * self.zoom_factor + self.zoom_factor] = np.full(
                        (self.zoom_factor, self.zoom_factor), _img[c, i, j])
        #  Transpose to get channels as last
        _img_zoomed = np.transpose(_img_zoomed, [1, 2, 0])
        return _img_zoomed

class Renderer:
    """
    Handles the renderer for the environment
    Receive a map from gridworld and transform it into a visible image (applies colors and zoom)
    """
    def __init__(self, size, zoom_factor):
        self.rgb = Colored(size, zoom_factor)
        self.viewer = None

    def render(self, state, close, mode='human'):
        if close:
            if self.viewer is not None:
                self.viewer.close()
                self.viewer = None
            return
        img = self.rgb.get_image(state)
        if mode == 'human':
            from gym.envs.classic_control import rendering
            if self.viewer is None:
                self.viewer = rendering.SimpleImageViewer()
            self.viewer.imshow(img)
            return self.viewer.isopen
        elif mode == 'rgb_array':
            return img

    def close(self):
        if self.viewer is not None:
            self.viewer.close()
            self.viewer = None
