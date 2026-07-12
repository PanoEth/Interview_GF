def rect_spacing(a, b):
    overlap_x= not(a.edgeX_right <= b.edgeX_left or b.edgeX_right <= a.edgeX_left)
    overlap_y= not(a.edgeY_top <= b.edgeY_bottom or b.edgeY_top <= a.edgeY_bottom)

    if overlap_x and overlap_y: 
        return 0.0
    #if they overlap the rule doesn't apply since its same same wiring/metal

    if overlap_x and not overlap_y:
        gap1= a.edgeY_bottom - b.edgeY_top
        gap2= b.edgeY_bottom - a.edgeY_top
        return max(gap1, gap2, 0.0)
    #if they overlap on x and not on y, gap is on Y (length-wise)

    if overlap_y and not overlap_x:
        gap1= a.edgeX_left - b.edgeX_right
        gap2= b.edgeX_left - a.edgeX_right
        return max(gap1, gap2, 0.0)

    dx= max(b.edgeX_left - a.edgeX_right, a.edgeX_left - b.edgeX_right, 0.0)
    dy= max(b.edgeY_bottom - a.edgeY_top, a.edgeY_bottom - b.edgeY_top, 0.0)
    return (dx*dx + dy*dy) ** 0.5 ##eucladian formula for distance: sqrt( (x*x)+(y*y) )
