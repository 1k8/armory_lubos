from arm.logicnode.arm_nodes import *

class PauseSpeakerNode(ArmLogicTreeNode):
    """Use to pause a speaker."""
    bl_idname = 'LNPauseSoundNode'
    bl_label = 'Pause Speaker'
    arm_version = 1

    def init(self, context):
        super(PauseSpeakerNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Speaker')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(PauseSpeakerNode, category=PKG_AS_CATEGORY)