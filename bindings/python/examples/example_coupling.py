#!/usr/bin/python3
import yarp

def main():
    yarp.Network.init()

    options = yarp.Property()
    driver = yarp.PolyDriver()

    # Configure the ergoCub hand coupling device
    options.put("device", "couplingXCubHandMk5")
    
    # Joint names
    joint_names = "l_thumb_add l_thumb_prox l_thumb_dist l_index_add l_index_prox l_index_dist l_middle_prox l_middle_dist l_ring_prox l_ring_dist l_pinkie_prox l_pinkie_dist"
    options.addGroup("jointNames")
    joint_names_list = options.findGroup("jointNames").addList()
    for name in joint_names.split():
        joint_names_list.addString(name)
    
    # COUPLING section
    coupling_group = options.addGroup("COUPLING")
    
    # actuatedAxesNames
    actuated_axes_names = "l_thumb_add l_thumb_oc l_index_add l_index_oc l_middle_oc l_ring_pinky_oc"
    coupling_group.addGroup("actuatedAxesNames")
    actuated_axes_list = coupling_group.findGroup("actuatedAxesNames").addList()
    for name in actuated_axes_names.split():
        actuated_axes_list.addString(name)
    
    # actuatedAxesPosMin
    pos_min_values = "0.0 0.0 0.0 0.0 0.0 0.0"
    coupling_group.addGroup("actuatedAxesPosMin")
    pos_min_list = coupling_group.findGroup("actuatedAxesPosMin").addList()
    for value in pos_min_values.split():
        pos_min_list.addString(value)
    
    # actuatedAxesPosMax
    pos_max_values = "90.0 82.1 15.0 90.0 90.0 90.0"
    coupling_group.addGroup("actuatedAxesPosMax")
    pos_max_list = coupling_group.findGroup("actuatedAxesPosMax").addList()
    for value in pos_max_values.split():
        pos_max_list.addString(value)
    
    # COUPLING_PARAMS section
    params_group = options.addGroup("COUPLING_PARAMS")
    
    # L0x
    l0x_values = "-0.00555 -0.0050 -0.0050 -0.0050 -0.0050"
    params_group.addGroup("L0x")
    l0x_list = params_group.findGroup("L0x").addList()
    for value in l0x_values.split():
        l0x_list.addString(value)
    
    # L0y
    l0y_values = "0.00285 0.0040 0.0040 0.0040 0.0040"
    params_group.addGroup("L0y")
    l0y_list = params_group.findGroup("L0y").addList()
    for value in l0y_values.split():
        l0y_list.addString(value)
    
    # q2bias
    q2bias_values = "-180.0 -173.35 -173.35 -173.35 -170.54"
    params_group.addGroup("q2bias")
    q2bias_list = params_group.findGroup("q2bias").addList()
    for value in q2bias_values.split():
        q2bias_list.addString(value)
    
    # q1off
    q1off_values = "4.29 2.86 2.86 2.86 3.43"
    params_group.addGroup("q1off")
    q1off_list = params_group.findGroup("q1off").addList()
    for value in q1off_values.split():
        q1off_list.addString(value)
    
    # k
    k_values = "0.0171 0.02918 0.02918 0.02918 0.02425"
    params_group.addGroup("k")
    k_list = params_group.findGroup("k").addList()
    for value in k_values.split():
        k_list.addString(value)
    
    # d
    d_values = "0.02006 0.03004 0.03004 0.03004 0.02504"
    params_group.addGroup("d")
    d_list = params_group.findGroup("d").addList()
    for value in d_values.split():
        d_list.addString(value)
    
    # l
    l_values = "0.0085 0.00604 0.00604 0.00604 0.00608"
    params_group.addGroup("l")
    l_list = params_group.findGroup("l").addList()
    for value in l_values.split():
        l_list.addString(value)
    
    # b
    b_values = "0.00624 0.0064 0.0064 0.0064 0.0064"
    params_group.addGroup("b")
    b_list = params_group.findGroup("b").addList()
    for value in b_values.split():
        b_list.addString(value)
    
    # LIMITS section
    limits_group = options.addGroup("LIMITS")
    
    # jntPosMax
    jnt_pos_max_values = "90.0 82.1 53.6 15.0 90.0 99.2 90.0 99.2 90.0 99.2 90.0 93.3"
    limits_group.addGroup("jntPosMax")
    jnt_pos_max_list = limits_group.findGroup("jntPosMax").addList()
    for value in jnt_pos_max_values.split():
        jnt_pos_max_list.addString(value)
    
    # jntPosMin
    jnt_pos_min_values = "0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0"
    limits_group.addGroup("jntPosMin")
    jnt_pos_min_list = limits_group.findGroup("jntPosMin").addList()
    for value in jnt_pos_min_values.split():
        jnt_pos_min_list.addString(value)

    # Open the driver
    print('Opening the ergoCub hand coupling device...')
    driver.open(options)
    if not driver.isValid():
        print('Cannot open the ergoCub hand coupling device!')
        return

    # Get the joint coupling interface
    ijc = driver.viewIJointCoupling()
    if ijc is None:
        print('Cannot view joint coupling interface!')
        driver.close()
        return

    print('Opened the ergoCub hand coupling device successfully!')
    # Display coupling information
    print(f"Number of physical joints: {ijc.getNrOfPhysicalJoints()}")
    print(f"Number of actuated axes: {ijc.getNrOfActuatedAxes()}")
    
    # Get joint names
    print("\nPhysical joint names:")
    for i in range(ijc.getNrOfPhysicalJoints()):
        name = ijc.getPhysicalJointName(i)
        print(f"  Joint {i}: {name}")
    
    print("\nActuated axis names:")
    for i in range(ijc.getNrOfActuatedAxes()):
        name = ijc.getActuatedAxisName(i)
        print(f"  Axis {i}: {name}")

    # Example coupling conversion
    print("\nTesting coupling conversion...")
    # Create YARP Vector objects instead of Python lists
    phys_joints = yarp.Vector(12)
    act_axes = yarp.Vector(ijc.getNrOfActuatedAxes())
    
    # Fill with example positions
    example_positions = [10.0, 20.0, 30.0, 5.0, 15.0, 25.0, 35.0, 45.0, 20.0, 30.0, 25.0, 35.0]
    for i, pos in enumerate(example_positions):
        phys_joints.set(i, pos)
    
    if ijc.convertFromPhysicalJointsToActuatedAxesPos(phys_joints, act_axes):
        print(f"Physical joints: {[phys_joints.get(i) for i in range(phys_joints.size())]}")
        print(f"Actuated axes: {[act_axes.get(i) for i in range(act_axes.size())]}")
    else:
        print("Conversion failed!")

    # Close the driver
    driver.close()
    yarp.Network.fini()

if __name__ == "__main__":
    main()