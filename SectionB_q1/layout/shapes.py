class Rect:
    def __init__(self, layer, width, length, cordX, cordY):
        self.layer = layer
        self. width = width
        self.length = length
        self.area = width*length
        self.edgeX_left = cordX
        self.edgeX_right = cordX+width
        self.edgeY_bottom = cordY
        self.edgeY_top = cordY + length
        