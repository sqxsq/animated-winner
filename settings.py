class Settings:
    """为 Alien Invasion存储所有参数设置的类."""

    def __init__(self):
        """初始化游戏参数"""

        #屏幕参数设置,宽度和高度
        self.screen_width = 1200
        self.screen_height = 800
        #设置背景颜色，RGB模式
        self.background_color = (240, 230, 230)