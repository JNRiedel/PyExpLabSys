import serial
import time
import FindSerialPorts

class Polyscience_4100():

    def __init__(self, port='/dev/ttyUSB0'):
        self.f = serial.Serial(port,9600,timeout=0.5)
        self.max_setpoint = 30
        self.min_setpoint = 10
        assert(self.min_setpoint<self.max_setpoint)

    def comm(self, command):
        self.f.write(command + '\r')
        reply = self.f.readline()
        return reply[:-1]

    def set_setpoint(self, value): 
        if value > self.max_setpoint:
            value = self.max_setpoint
        if value < self.min_setpoint:
            value = self.min_setpoint

        string = '{0:.0f}'.format(value)
        if len(string) == 1:
            string = '00' + string
        else:
            string = '0' + string
        assert len(string) == 3
        value = self.comm('SS' + string)
        success = value == '!'
        return success

    def turn_unit_on(self, turn_on): 
        if turn_on == True:
            value = self.comm('SO1')
        if turn_on == False:
            value = self.comm('SO0')
        return value

    def read_setpoint(self): 
        value = self.comm('RS')
        return float(value)

    def read_unit(self): 
        value = self.comm('RU')
        return value

    def read_temperature(self): 
        try:
            status = self.comm('RW')
            if status == '1':
                value = self.comm('RT')
            else:
                value = float('nan')
        except:
            value = float('nan')
        return float(value)

    def read_pressure(self): 
        try:
            status = self.comm('RW')
            if status == '1':
                value = self.comm('RK')
            else:
                value = float('nan')
        except:
            value = float('nan')
        return float(value)/100.0

    def read_flow_rate(self): 
        try:
            status = self.comm('RW')
            if status == '1':
                value = self.comm('RL')
            else:
                value = float('nan')
        except:
            va.ue = float('nan')
        return float(value)

    def read_ambient_temperature(self): 
        try:
            status = self.comm('RW')
            if status == '1':
                value = self.comm('RA')
            else:
                value = float('nan')
        except:
            value = float('nan')
        return float(value)


    def read_status(self): 
        value = self.comm('RW')
        status = 'error'
        if value == '0':
            status = 'Off'
        if value == '1':
            status = 'On'
        return status

if __name__ == '__main__':
    ports = FindSerialPorts.find_ports()

    #chiller = Polyscience_4100('/dev/ttyUSB0')
    #print chiller.read_status()

    for port in ports:
        chiller = Polyscience_4100('/dev/' + port)
        if not (chiller.read_status() == 'error'):
            print port
            break
        
    print 'Setpoint: {0:.1f}'.format(chiller.read_setpoint())
    print 'Temperature: {0:.1f}'.format(chiller.read_temperature())
    print 'Flow rate: {0:.2f}'.format(chiller.read_flow_rate())
    print 'Pressure: {0:.3f}'.format(chiller.read_pressure())
    print 'Status: ' + chiller.read_status()
    print 'Ambient temperature: {0:.2f}'.format(chiller.read_ambient_temperature()) 

