### Import ROS SMACH Dependencies
import rospy
import smach
import smach_ros
from smach_ros import IntrospectionServer

### Robot Building (Import Robot Skills)
import base_skill_template as bskt
import numpy as np
import rospkg

### Importing poses
rospack = rospkg.RosPack()
pkgDir = rospack.get_path('homebreaker_tutorial')
poses = np.load(f'{pkgDir}/poses/poses.npy')

### Defining Home and Checkpoints
home = poses[0]
checkpoints = np.delete(poses,0)

def random_checkpoint(checkpoint):
    check = np.random.choice(checkpoint, 1, replace = False)
    return check


### States
## State Walking:
class Walking(smach.State):
    ### Class Initializer
    def __init__(self):
        smach.State.__init__(self,
            # Outcomes: define the state transition
            outcomes = ['succeded', 'user_says_keep_walking'],
            # Userdata is used to share data between states
            # Input Keys: Userdata attributes to take as input
            input_keys = ["data_1"],
            # Output Keys: Userdata attributes to give as output
            output_keys = ["data_1"],
        )

    ### State Action
    def execute(self, userdata):
        rospy.loginfo('Walking...')
        in_data = userdata.data_1

        # Your state logic here
        
        userdata.data_1 = None
        if True:
            # Transition to state related to outcome 1
            return 'outcome1'  
        else:
            # Transition to state related to outcome 2
            return 'outcome2'


### SMACH Building
def getInstance():

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['succeded', 'user_says_keep_walking','user_says_goto_home'])

    # Open the container
    with sm:
        # Add states to the container
        pass
        
if __name__ == '__main__':
    rospy.init_node('smach_example')
    sm = getInstance()
    sis = IntrospectionServer('smach_example', sm, '/SMACH_EXAMPLE') #Smach Viewer
    sis.start()
    result = sm.execute()
    sis.stop()