import bpy
import bmesh
from mathutils import Euler
from math import radians


def write_some_data(context, filepath, use_some_setting):
    #print("running write_some_data...")
    f = open(filepath, "w", encoding='utf-8')
    f.write("#pragma once \n \n".format(use_some_setting))
    #f.write("#include "'"vertexUtils.hpp"'" \n\n".format(use_some_setting))
    
    #f.write("//vertexUtils contains the Vertex struct\n\n".format(use_some_setting))
    
    f.write("//struct Vertex\n".format(use_some_setting))
    f.write("//{{\n".format(use_some_setting))
    f.write("//    float u, v;\n".format(use_some_setting))
    f.write("//    unsigned int color;\n".format(use_some_setting))
    f.write("//    float x, y, z;\n".format(use_some_setting))
    f.write("//}};\n\n".format(use_some_setting))
    


    obj = bpy.context.object
    
    R = Euler((radians(-90), 0, 0)).to_matrix().to_4x4()
    obj.matrix_world = R @ obj.matrix_world
    mat = obj.matrix_world
    
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bmesh.ops.triangulate(bm, faces=bm.faces[:])
    bm.to_mesh(obj.data)
    bm.free()
    
    uv = []
    pos = []
    ind_ccw = []
    ind_cw = []
    
    it = 0
    for face in obj.data.polygons:
        for vert_idx, loop_idx in zip(face.vertices, face.loop_indices):
            uvs_coords = obj.data.uv_layers.active.data[loop_idx].uv
            v = obj.data.vertices[vert_idx].co
            loc = mat @ v
            pos.append(rounded_tuple(loc.to_tuple()))
            uv.append(rounded_tuple(uvs_coords.to_tuple()))
            ind_ccw.append(it)
            it += 1
    
    
    ind_cw = ind_ccw[::-1]
    
    f.write("// Model Info\n".format(use_some_setting))
    f.write("// Model Name: "'"'+str(obj.name)+"_Model"'"'"\n".format(use_some_setting))
    f.write("// Indices Clock-Wise: "'"'+str(obj.name)+"_Indices_CW"'"'"\n".format(use_some_setting))
    f.write("// Indices Counter Clock-Wise: "'"'+str(obj.name)+"_Indices_CCW"'"'"\n".format(use_some_setting))
    f.write("// Indices Count: "'"'+str(obj.name)+"_Indices_Count"'"' " = "+str(len(ind_cw))+"\n".format(use_some_setting))
    f.write("\n".format(use_some_setting))
    
    f.write("const unsigned short "+str(obj.name)+"_Indices_CW["+str(len(ind_cw))+"] =\n".format(use_some_setting))
    f.write("{{\n    ".format(use_some_setting))
    for z in range(len(ind_cw)):
        f.write(str(ind_cw[z])+", ")
        
    f.write("\n")
    f.write("}}; \n".format(use_some_setting))
    
    f.write("\n")
    f.write("const unsigned short "+str(obj.name)+"_Indices_CCW["+str(len(ind_ccw))+"] =\n".format(use_some_setting))
    f.write("{{\n    ".format(use_some_setting))
    for z in range(len(ind_ccw)):
        f.write(str(ind_ccw[z])+", ")
        
    f.write("\n")
    f.write("}}; \n".format(use_some_setting))
    
    f.write("\n")
    f.write("const unsigned short "+str(obj.name)+"_Indices_Count = "+str(len(ind_cw))+";\n\n".format(use_some_setting))
    
    f.write("const struct Vertex __attribute__((aligned(16))) "+str(obj.name)+"_Model["+str(len(pos))+"] = \n".format(use_some_setting))
    f.write("{{ \n".format(use_some_setting))
      
    for y in range(len(pos)):
        f.write("    { "+str(uv[y][0])+"f, "+str(uv[y][1])+"f, 0xFFFFFFFF, "+str(pos[y][0])+"f, "+str(pos[y][1])+"f, "+str(pos[y][2])+"f}},\n".format(use_some_setting))
    
    f.write("}};".format(use_some_setting))
    
    f.write("\n\n")
    
    
    RR = Euler((radians(90), 0, 0)).to_matrix().to_4x4()
    obj.matrix_world = RR @ obj.matrix_world
    mat = obj.matrix_world
    
    f.close()

    return {'FINISHED'}



# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ExportSomeData(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "export_test.some_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export Some Data"

    # ExportHelper mix-in class uses this.
    filename_ext = ".hpp"

    filter_glob: StringProperty(
        default="*.hpp",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    use_setting: BoolProperty(
        name="Example Boolean",
        description="Example Tooltip",
        default=True,
    )
    
    def execute(self, context):
        return write_some_data(context, self.filepath, self.use_setting)


def rounded_tuple(tup):
    return tuple(round(value, 3) for value in tup)


# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
    self.layout.operator(ExportSomeData.bl_idname, text="Text Export Operator")


# Register and add to the "file selector" menu (required to use F3 search "Text Export Operator" for quick access).
def register():
    bpy.utils.register_class(ExportSomeData)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportSomeData)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.export_test.some_data('INVOKE_DEFAULT')
