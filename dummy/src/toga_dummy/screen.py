from pathlib import Path

import toga_dummy
from toga.screen import Screen as ScreenInterface

from .utils import LoggedObject  # noqa


class Screen(LoggedObject):
    _instances = {}

    def __new__(cls, native):
        if native in cls._instances:
            return cls._instances[native]
        else:
            instance = super().__new__(cls)
            instance.interface = ScreenInterface(_impl=instance)
            instance.native = native
            cls._instances[native] = instance
            return instance

    def get_name(self):
        return self.native

    def get_origin(self):
        if self.native == "primary_screen":
            return (0, 0)
        else:
            return (-1920, 0)

    def get_size(self):
        return (1920, 1080)

    # Same as for the window as_image().
    def get_image_data(self):
        self._action("get image data")
        path = Path(toga_dummy.__file__).parent / "resources/screenshot.png"
        return path.read_bytes()
