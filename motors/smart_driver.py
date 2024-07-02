import com.can as com
import can
import struct


def callback(speedmode, stop, reset, voltagemode, goal, motor_id):
    canMsgData = [0,0,0,0, 0, 0, 0, 0, 0, 0, 0,0, 0]
    canMsgData[0] = 0xAA
    canMsgData[1] = 0xC8
    canMsgData[2] = 0x00+motor_id
    canMsgData[3] = 0x00
    canMsgData[4] = (
        speedmode +
        (stop << 1) +
        (reset << 2) +
        (voltagemode << 3)
    )
    
    goal_bytes = struct.pack("<f", goal)
    
    canMsgData[6:10] = list(goal_bytes)
    canMsgData[12] = 0x55
    
    # can_msg = can.Message(arbitration_id=motor_id, data=canMsgData, is_extended_id=False)
    try:
        print(canMsgData[4])
        com.uca.frame_send(canMsgData)
        # bus.send(can_msg)
        # print("Message sent on {}".format(bus.channel_info))
    except can.CanError:
        print("Message NOT sent")

def callback_test():
    com.uca.frame_receive()
    print(com.uca.frame)