from com.usbcan_adapter import UsbCanAdapter

class RMDx6:
    def __init__(self):
        self.uca = UsbCanAdapter()
        self.uca.set_port("/dev/ttyUSB0")
        self.uca.adapter_init()
        self.uca.command_settings(speed=1000000)

    def ratio(self, mid, ang, velo):
        if mid == 1:
            ang *= 6.0
            velo *= 6.0
        elif mid == 2:
            ang *= 6.0
            velo *= 6.0
        elif mid == 3:
            ang *= 6.0
            velo *= 6.0
        elif mid == 4:
            ang *= 6.0
            velo *= 6.0
        elif mid == 5:
            ang *= 9.0
            velo *= 9.0
        elif mid == 6:
            ang *= 9.0
            velo *= 9.0
        else:
            ang *= 30.0
            velo *= 30.0
        return int(ang * 100), int(velo * 100)

    def int_byte(self, int_data):
        return int_data & 0xFF

    def run_speed(self, mid, velo):
        result = 0
        # chsum = 0
        degree, speed = self.ratio(mid, 0, velo)
        m_data = []
        m_data.append(0xAA)
        m_data.append(0xC8)
        m_data.append(0x40 + mid)
        m_data.append(0x01)
        m_data.append(0xA2)
        m_data.append(0x00)
        m_data.append(0x00)
        m_data.append(0x00)
        for i in range(8, 12):
            m_data.append(self.int_byte(speed >> 8 * (i - 8)))
        #m_data.append(0x55)
        print("moving")
        self.uca.frame_send(m_data)
        #print(com.uca.extract_data(m_data))

    def read_speed_all(self):
        m_data = []
        m_data.append(0xAA)
        m_data.append(0xC8)
        m_data.append(0x40)
        m_data.append(0x01)
        m_data.append(0xA3)