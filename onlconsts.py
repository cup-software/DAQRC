kSOFTWARE_VER = '3.1.0'
kONLDAQ_DIR = '/home/cupsoft/Devs/dev_3.0.0'
kRAWDATA_DIR = '/home/cupsoft/Devs/test'
kRUNCATALOGDBFILE = '/home/cupsoft/Devs/rcdev/runcatalog.db'

kRUNTYPELIST = ['', 'physics', 'calibration', 'test']

kDAQSERVER_IP = '192.168.0.150'
kDAQSERVER_PORT = 7809
kDAQSERVER_ADDR = (kDAQSERVER_IP, kDAQSERVER_PORT)


#
# Do not modify from here!!!
#
kEXESCRIPT = 'executenulldaq.sh'
kMESSLEN = 32

# Commands
kCONFIGRUN = 1
kSTARTRUN = 2
kENDRUN = 3
kEXIT = 4
kQUERYDAQSTATUS = 10
kQUERYRUNINFO = 12
kQUERYTRGINFO = 14
kQUERYMONITOR = 21

# RUN Status
kDOWN = 0
kBOOTED = 1
kCONFIGURED = 2
kRUNNING = 3
kRUNENDED = 4
kPROCENDED = 5
kWARNING = 8
kERROR = 9

kDAQSTATE = ['Down', 'Booted', 'Configured',
             'Running', 'RunEnd', 'RunEnd', '', '', 'Error']
