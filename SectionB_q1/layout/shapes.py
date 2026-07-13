class Rect:
    def __init__(self, layer, width, length, cordX, cordY):
        #layer valid in rules, width and length in um. Coords are given in um too
        self.layer = layer
        self.width = width
        self.length = length
        self.area = width*length
        self.edgeX_left = cordX #assumes left edge of rectangle
        self.edgeX_right = cordX+width  #assumes right edge: left edge coord + width of wire
        self.edgeY_bottom = cordY
        self.edgeY_top = cordY + length
        