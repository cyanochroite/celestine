# <pep8-80 compliant>
from . import new

# shader


def shader_image(nodes, image):
    # inputs
    # "Vector"
    # outputs
    # "Color"
    # "Alpha"
    node = nodes.new('ShaderNodeTexImage')
    node.image = image
    node.interpolation = 'Cubic'
    node.projection = 'FLAT'
    node.extension = 'CLIP'
    return node


def shader_diffuse(nodes):
    # inputs
    # "Color"
    # "Roughness"
    # "Normal"
    # outputs
    # "BSDF"
    node = nodes.new('ShaderNodeBsdfDiffuse')
    return node


def shader_output(nodes):
    # inputs
    # "Surface"
    # "Volume"
    # "Displacement"
    # outputs
    node = nodes.new('ShaderNodeOutputMaterial')
    node.target = 'ALL'
    return node

# material


def material(name, image):
    material = new.material(name)
    material.use_nodes = True

    tree = material.node_tree
    nodes = tree.nodes
    nodes.clear()

    aa = shader_image(nodes, image)
    aa.location = (000, 000)

    bb = shader_diffuse(nodes)
    bb.location = (300, 000)

    cc = shader_output(nodes)
    cc.location = (500, 000)

    tree.links.new(aa.outputs["Color"], bb.inputs["Color"])
    tree.links.new(bb.outputs["BSDF"], cc.inputs["Surface"])

    return material
