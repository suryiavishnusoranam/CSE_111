from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500
    canvas = start_drawing("Scene", scene_width, scene_height)
    
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    finish_drawing(canvas)

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="deepSkyBlue")
    draw_sun(canvas)
    draw_cloud(canvas)
    draw_mountain(canvas)

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="springGreen4")
    draw_road(canvas)

    tree_center_x = 550
    tree_bottom = 50
    tree_height = 250
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    tree_center_x = 650
    tree_bottom = 20
    tree_height = 250
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    draw_birds(canvas)

def draw_pine_tree(canvas, center_x, bottom, height):

    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, outline="darkOrange4", width=1, fill="darkOrange4")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height
    draw_polygon(canvas, center_x, skirt_top, skirt_right, trunk_top, skirt_left, trunk_top, outline="forestGreen", width=1, fill="darkGreen")
        
def draw_cloud(canvas):
    draw_oval(canvas, 300, 450, 100, 400, width=1, outline="white", fill="white")
    draw_oval(canvas, 380, 450, 180, 400, width=1, outline="white", fill="white")
    draw_oval(canvas, 580, 450, 430, 400, width=1, outline="white", fill="white")
    draw_oval(canvas, 660, 450, 490, 400, width=1, outline="white", fill="white")

def draw_sun(canvas):
    draw_oval(canvas, 790, 300, 600, 490, width=1, outline="yellow1", fill="yellow1")

def draw_mountain(canvas):
    draw_polygon(canvas, 550, 100, 400, 300, 50, 100, outline="green", fill="chartreuse4")
    draw_polygon(canvas, 750, 100, 600, 300, 50, 100, outline="green", fill="chartreuse4")

def draw_birds(canvas):
    draw_arc(canvas, 350, 350, 270, 230, start=25, extent=130)
    draw_arc(canvas, 750, 320, 670, 200, start=25, extent=130)
    draw_arc(canvas, 650, 400, 570, 270, start=25, extent=130)
    draw_arc(canvas, 220, 390, 140, 260, start=25, extent=130)
    draw_arc(canvas, 120, 370, 40, 240, start=25, extent=130)

def draw_road(canvas):
    draw_line(canvas, 0, 140, 800, 140, width=70, fill="lavenderBlush4")
    for i in range(14):
        draw_line(canvas, 10+60*i , 140, 50, 140, width=5, fill="white")
        

    draw_line(canvas, 10, 140, 50, 140, width=5, fill="white")
    draw_line(canvas, 70, 140, 110, 140, width=5, fill="white")
    draw_line(canvas, 130, 140, 170, 140, width=5, fill="white")
    draw_line(canvas, 190, 140, 230, 140, width=5, fill="white")
    draw_line(canvas, 250, 140, 290, 140, width=5, fill="white")
    draw_line(canvas, 310, 140, 350, 140, width=5, fill="white")
    draw_line(canvas, 370, 140, 410, 140, width=5, fill="white")
    draw_line(canvas, 430, 140, 470, 140, width=5, fill="white")
    draw_line(canvas, 490, 140, 530, 140, width=5, fill="white")
    draw_line(canvas, 550, 140, 590, 140, width=5, fill="white")
    draw_line(canvas, 610, 140, 650, 140, width=5, fill="white")
    draw_line(canvas, 670, 140, 710, 140, width=5, fill="white")
    draw_line(canvas, 730, 140, 770, 140, width=5, fill="white")
    draw_line(canvas, 790, 140, 830, 140, width=5, fill="white")
    
main()