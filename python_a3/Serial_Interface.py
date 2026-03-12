"""
Write a function to generate bit pattern for a serial interface
"""
def decimal_to_binary(address: int)->list:
    byte_address=[0]*8
    i=7
    while(address>0):
        bit=address&1
        byte_address[i]=bit
        address=address>>1
        i=i-1
    return byte_address

def serial_interface_address_gen(*bytes)->tuple:
    device_slave_address=decimal_to_binary(bytes[0])
    register_address=decimal_to_binary(bytes[1])
    data_to_write=decimal_to_binary(bytes[2])
    return (device_slave_address, register_address, data_to_write)


print(serial_interface_address_gen(20,44,16))  
