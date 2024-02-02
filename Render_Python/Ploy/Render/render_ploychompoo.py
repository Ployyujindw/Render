import maya.cmds as cmds


def close_window(*args):
    cmds.deleteUI("my_window", window=True)


def create_camera():
    cmds.createNode("camera")

def render_ploychompoo(*args):
    #Get user inputs
    result_int_width_res = get_int_input_width_res()
    result_int_high_res = get_int_input_high_res()

    # image_path = cmds.textField("output_render_image", query=True, tx=True) 
    
    #Render image
    cmds.render()
    camera_name = cmds.textField("camera_name", query=True, text=True)
    node_shapes = cmds.listRelatives(camera_name, shapes=True)
    camShape = node_shapes[0] # cameras[0] is the first camera
    print(camShape)
    img = cmds.render(camShape, x=result_int_width_res, y=result_int_high_res )
    print("image is " + img)
    
    
    #Display render image
    window = cmds.window(title="Your Image", iconName='Short Name', widthHeight=(result_int_width_res, result_int_high_res))
    cmds.paneLayout()
    cmds.image( image=img ) 
    cmds.showWindow( window )
    
    
def get_int_input_width_res(*args):
    result_width_res = cmds.intField("input_width_res", query=True, value=True )
    print(result_width_res)
    return result_width_res
    
def get_int_input_high_res(*args):
    result_high_res = cmds.intField("input_high_res", query=True, value=True )
    print(result_high_res)
    return result_high_res
   
def get_selected_camera(*args):
    cameras = cmds.ls(sl=True)
    cmds.textField("camera_name", edit=True, text=cameras[0])


def main():
    if cmds.window("my_window", query=True, exists=True ):
        close_window()
    #Start when run code - display window to render
    my_window = cmds.window( "my_window",title="Render by Ploychompoo C.", iconName='Short Name', widthHeight=(250, 200) )
    cmds.columnLayout( adjustableColumn=True )

    # input camera name
    cmds.text( label='Camera name' )
    cmds.textField("camera_name", text="")

    # get cameera selected button
    cmds.button("get_camera", label='Get Camera', command=(get_selected_camera) )

    cmds.text( label='input width resolution' )
    cmds.intField("input_width_res", value=500)
    cmds.text( label='input high resolution' )
    cmds.intField("input_high_res", value=500)
    cmds.button("run",label='Run', command=(render_ploychompoo) )
    cmds.button("cloes",label='Close', command=(close_window) )
    
    # cmds.text( label='Your image' )
    # cmds.textField("output_render_image", editable=False, preventOverride=False ) #Complete render image URL

    # path output
    # cmds.text( label='Path output' )
    # cmds.textField("output_render_path") #Complete render image URL

    cmds.setParent( '..' )
    cmds.showWindow( my_window )