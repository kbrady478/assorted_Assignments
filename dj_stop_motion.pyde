poses = []

def setup():
    size(1920, 1080, P3D)
    frameRate(30)
    colorMode(HSB)
    
    global fps, cycle, pose
    fps = 0
    cycle = 0
    assign_anim()
   
               
def draw():
    global fps, cycle, pose
    
    colorMode(HSB)
    background(0)
    lights()
    translate(width / 2, height / 2)
    
    
    
    if fps == 30:
        fps = 0
        cycle = cycle + 1
    else:
        fps = fps + 1
        

   
class Model:
    def __init__(self, file_name, x, y, z, s, h):
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.sh = loadShape(file_name)
        self.sh.disableStyle()
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateY(PI)
        rotateZ(PI)
        scale(200)        
        shape(self.sh)
    
        popMatrix()

def assign_anim():

    # Rest position
    dj_anim = Model("dj_anims/dj_anim_rest.obj", 0, 400, 0, 5, random(256))
    poses.append(dj_anim)
    
    # Pose 1, Frame 1
    dj_anim = Model("dj_anims/p1/dj_anim_p1_f1.obj", 0, 400, 0, 5, random(256))
    poses.append(dj_anim)
    
    # Pose 1, Frame 2
    dj_anim = Model("dj_anims/p1/dj_anim_p1_f2.obj", 0, 400, 0, 5, random(256))
    poses.append(dj_anim)
    
    # Pose 1, Frame 3
    dj_anim = Model("dj_anims/p1/dj_anim_p1_f3.obj", 0, 400, 0, 5, random(256))
    poses.append(dj_anim)
    
    # Pose 1, Frame 4
    dj_anim = Model("dj_anims/p1/dj_anim_p1_f4.obj", 0, 400, 0, 5, random(256))
    poses.append(dj_anim)
    
    # Pose 2, Frame 1
    dj_anim = Model("dj_anims/p2/dj_anim_p2_f1.obj", 0, 400, 0, 5, random(256))
    poses.append(dj_anim)

    # Pose 2, Frame 2
    dj_anim = Model("dj_anims/p2/dj_anim_p2_f2.obj", 0, 400, 0, 5, random(256))
    poses.append(dj_anim)
    
    # Pose 2, Frame 3
    dj_anim = Model("dj_anims/p2/dj_anim_p2_f3.obj", 0, 400, 0, 5, random(256))
    poses.append(dj_anim)
    
    # Pose 2, Frame 4
    dj_anim = Model("dj_anims/p2/dj_anim_p2_f4.obj", 0, 400, 0, 5, random(256))
    poses.append(dj_anim)
