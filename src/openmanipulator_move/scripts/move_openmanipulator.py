#! /usr/bin/env python

import time
import rospy
from sensor_msgs.msg import JointState
from dynamixel_workbench_msgs.srv import JointCommand, JointCommandRequest
from std_msgs.msg import Header


class OpenManipulatorMove(object):
    def __init__(self):
        rospy.loginfo("OpenManipulatorMove INIT...Please wait.")

        # We subscribe to the joint states to have info of the system

        self.joint_states_topic_name = '/joint_states'
        self._check_join_states_ready()
        sub = rospy.Subscriber(self.joint_states_topic_name, JointState, self.joint_states_callback)


        # We start the Publisher for the positions of the joints
        self.goal_dynamixel_position_publisher = rospy.Publisher('/goal_dynamixel_position',
                                                                    JointState,
                                                                    queue_size=1)

        # Wait for the service client /joint_command to be running
        joint_command_service_name = "/joint_command"
        rospy.wait_for_service(joint_command_service_name)
        # Create the connection to the service
        self.joint_command_service = rospy.ServiceProxy(joint_command_service_name, JointCommand)

        rospy.loginfo("OpenManipulatorMove Ready!")

    def joint_states_callback(self,msg):
        """
        rosmsg show sensor_msgs/JointState
            std_msgs/Header header
              uint32 seq
              time stamp
              string frame_id
            string[] name
            float64[] position
            float64[] velocity
            float64[] effort

        :param msg:
        :return:
        """
        self.joint_states_msg = msg

    def _check_join_states_ready(self):
        self.joint_states_msg = None
        rospy.logdebug("Waiting for "+self.joint_states_topic_name+" to be READY...")
        while self.joint_states_msg is None and not rospy.is_shutdown():
            try:
                self.joint_states_msg = rospy.wait_for_message(self.joint_states_topic_name, JointState, timeout=5.0)
                rospy.logdebug("Current "+self.joint_states_topic_name+" READY=>")

            except:
                rospy.logerr("Current "+self.joint_states_topic_name+" not ready yet, retrying ")

    def move_all_joints(self, position_array):

        rospy.logwarn("move_all_joints STARTED")
        # We check that the position array has the correct number of elements
        number_of_joints = len(self.joint_states_msg.name)

        if len(position_array) == number_of_joints:
            if self.check_gripper_pos_safe(position_array[4]):
                new_joint_position = JointState()

                h = Header()
                h.stamp = rospy.Time.now()  # Note you need to call rospy.init_node() before this will work
                h.frame_id = self.joint_states_msg.header.frame_id

                new_joint_position.header = h
                new_joint_position.name = self.joint_states_msg.name
                new_joint_position.position = position_array

                # These values arent used, so they dont matter really
                new_joint_position.velocity = self.joint_states_msg.velocity
                new_joint_position.effort = self.joint_states_msg.effort

                rospy.logwarn("PUBLISH STARTED")
                self.goal_dynamixel_position_publisher.publish(new_joint_position)
                rospy.logwarn("PUBLISH FINISHED")
            else:
                rospy.logerr("Gripper position NOT valid=" + str(position_array[4]))
        else:
            rospy.logerr("The Array given doesnt have the correct length="+str(number_of_joints))

        rospy.logwarn("move_all_joints FINISHED")


    def move_one_joint(self, joint_id, position, unit="rad"):
        """
        rossrv show dynamixel_workbench_msgs/JointCommand
            string unit
            uint8 id
            float32 goal_position
            ---
            bool result

        :param joint_id:
        :param position:
        :param units:
        :return:
        """
        joint_cmd_req = JointCommandRequest()
        joint_cmd_req.unit = unit
        joint_cmd_req.id = joint_id
        joint_cmd_req.goal_position = position

        if joint_id == 15:
            rospy.logwarn("CHECKING Gripper Value is safe?")
            if self.check_gripper_pos_safe(position):

                # Send through the connection the name of the object to be deleted by the service
                result = self.joint_command_service(joint_cmd_req)
                rospy.logwarn("move_one_joint went ok?="+str(result))
            else:
                rospy.logwarn("Gripper Value Not safe=" + str(position))
        else:
            # Send through the connection the name of the object to be deleted by the service
            result = self.joint_command_service(joint_cmd_req)
            rospy.logwarn("move_one_joint went ok?=" + str(result))

    def get_joint_names(self):
        return self.joint_states_msg.name


    def check_gripper_pos_safe(self, gripper_value):
        """
        We need to check that the gripper pos is -1.0 > position[4] > -3.14
        Otherwise it gets jammed
        :param gripper_value:
        :return:
        """
        return (-0.5 > gripper_value > -2.0)

def movement_sequence_test():

    openman_obj = OpenManipulatorMove()

    # NOD
    joint_position_home = [3.1231849193573, -0.5230874419212341, -0.08130098134279251, -2.0678062438964844, -1.026233196258545]
    joint_position1 = [-1.9619615077972412, -0.43718454241752625, -0.18254372477531433, -1.9773012399673462, -1.2350101470947266]
    joint_position2 = [2.0862138271331787, -0.6795535087585449, -0.013805827125906944, -2.063204288482666, -1.008136510848999]
    joint_position3 = [-3.1354568004608154, -0.17794176936149597, 0.11658254265785217, -1.9819031953811646, -0.9835927486419678]


    # SAY NO
    #joint_left = [1.886796474456787, -0.4080389142036438, 0.13192234933376312, -2.1061556339263916, -1.1813206672668457]
    #joint_right = [-1.9788352251052856, -0.5967185497283936, -0.0920388475060463, -2.0110487937927246, -1.182854652404785]
    #joint_middle = [3.1231849193573, -0.5230874419212341, -0.08130098134279251, -2.0678062438964844, -1.026233196258545]

    # Pendulum
    #pend_left = [0.46479618549346924, 0.13345633447170258, -1.728796362876892, 1.5907381772994995, -1.6797089576721191, 0.004601942375302315, -1.0799225568771362]
    #pend_middle = [0.39269909262657166, 0.1595340073108673, -2.0984857082366943, -0.09817477315664291, -1.0615147352218628, -0.0015339808305725455, -1.0799225568771362]
    #pend_right = [0.006135923322290182, 0.42337870597839355, -1.8806605339050293, -1.306951642036438, -1.0661166906356812, -0.004601942375302315, -1.0799225568771362]


    joint_position_sequence_nod = []
    joint_position_sequence_nod.append(joint_position_home)
    joint_position_sequence_nod.append(joint_position1)
    joint_position_sequence_nod.append(joint_position2)
    joint_position_sequence_nod.append(joint_position3)
    #joint_position_sequence_nod.append(joint_position2)
    #joint_position_sequence_nod.append(joint_position3)
    joint_position_sequence_nod.append(joint_position1)
    joint_position_sequence_nod.append(joint_position_home)

    #joint_position_sequence_say_no = []
    #joint_position_sequence_nod.append(joint_position_home)
    #joint_position_sequence_nod.append(joint_left)
    #joint_position_sequence_nod.append(joint_middle)
    #joint_position_sequence_nod.append(joint_right)
    #joint_position_sequence_nod.append(joint_left)
    #joint_position_sequence_nod.append(joint_middle)
    #joint_position_sequence_nod.append(joint_right)
    #joint_position_sequence_nod.append(joint_left)
    #joint_position_sequence_nod.append(joint_right)
    #joint_position_sequence_nod.append(joint_left)
    #joint_position_sequence_nod.append(joint_position_home)


    #joint_position_sequence_say_pendulum = []
    #joint_position_sequence_say_pendulum.append(joint_position_home)
    #joint_position_sequence_say_pendulum.append(pend_left)
    #joint_position_sequence_say_pendulum.append(pend_middle)
    #joint_position_sequence_say_pendulum.append(pend_right)
    #joint_position_sequence_say_pendulum.append(pend_left)
    #joint_position_sequence_say_pendulum.append(pend_middle)
    #joint_position_sequence_say_pendulum.append(pend_right)
    #joint_position_sequence_say_pendulum.append(pend_left)
    #joint_position_sequence_say_pendulum.append(pend_middle)
    #joint_position_sequence_say_pendulum.append(pend_right)
    #oint_position_sequence_say_pendulum.append(joint_position_home)



    for joint_position_array in joint_position_sequence_nod:
        openman_obj.move_all_joints(joint_position_array)
        time.sleep(1.5)

    #for joint_position_array in joint_position_sequence_say_no:
    #    openman_obj.move_all_joints(joint_position_array)
    #    time.sleep(0.5)

    #for joint_position_array in joint_position_sequence_say_pendulum:
    #    openman_obj.move_all_joints(joint_position_array)
    #    time.sleep(0.5)

def move_joints_test():
    """
    This is for Geting the positions of the joints without testing them
    live, which is quite dangerous!
    :return:
    """
    openman_obj = OpenManipulatorMove()
    joint_names = openman_obj.get_joint_names()
    rospy.logwarn("Starting Moving Joints GUI...")
    while not rospy.is_shutdown():
        rospy.logwarn("#######"+str(joint_names)+"#####")
        joint_id = int(raw_input("Joint ID="))
        joint_position = float(raw_input("Joint Position Radians="))
        openman_obj.move_one_joint(joint_id, joint_position, unit="rad")
        rospy.logwarn("####################")


if __name__ == "__main__":
    rospy.init_node('move_openmanipulator_node', log_level=rospy.WARN)
    #move_joints_test()
    movement_sequence_test()