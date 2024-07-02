import com.can as com

def run_solenoid(mid, solenoid):
    boolean_data = 0x01 if solenoid else 0x00
    m_data = []
    m_data.append(0xAA)
    m_data.append(0xC8)
    m_data.append(0x00 + mid)
    m_data.append(0x01)
    m_data.append(boolean_data)
    for i in range(5, 12):
        m_data.append(0x00)
    m_data.append(0x55)
    com.uca.frame_send(m_data)