# <pep8-80 compliant>
from . import data

# shader


def shader_image(nodes, image):
    # inputs
    # "Vector"
    # outputs
    # "Color"
    # "Alpha"
    node = nodes.new("ShaderNodeTexImage")
    node.image = image
    node.interpolation = "Cubic"
    node.projection = "FLAT"
    node.extension = "CLIP"
    return node


def shader_diffuse(nodes):
    # inputs
    # "Color"
    # "Roughness"
    # "Normal"
    # outputs
    # "BSDF"
    node = nodes.new("ShaderNodeBsdfDiffuse")
    return node


def shader_output(nodes):
    # inputs
    # "Surface"
    # "Volume"
    # "Displacement"
    # outputs
    node = nodes.new("ShaderNodeOutputMaterial")
    node.target = "ALL"
    return node


# material


def material(name, image):
    material = data.material.new(name)
    material.use_nodes = True

    tree = material.node_tree
    nodes = tree.nodes
    nodes.clear()

    aaa = shader_image(nodes, image)
    aaa.location = (000, 000)

    bbb = shader_diffuse(nodes)
    bbb.location = (300, 000)

    ccc = shader_output(nodes)
    ccc.location = (500, 000)

    tree.links.new(aaa.outputs["Color"], bbb.inputs["Color"])
    tree.links.new(bbb.outputs["BSDF"], ccc.inputs["Surface"])

    return material
