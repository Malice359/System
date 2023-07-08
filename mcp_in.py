import time
import board
import busio
import digitalio

from adafruit_mcp230xx.mcp23017 import MCP23017


# Initialize the I2C bus:
i2c = busio.I2C(board.SCL, board.SDA)

mcp1 = MCP23017(i2c) 
mcp2 = MCP23017(i2c, address=0x21)

#mcp# = MCP23017(i2c, address=0x##)

# Define Pins and address to 
pin0 = mcp1.get_pin(0)
pin1 = mcp1.get_pin(1)
pin2 = mcp1.get_pin(2)
pin3 = mcp1.get_pin(3)
pin4 = mcp1.get_pin(4)
pin5 = mcp1.get_pin(5)
pin6 = mcp1.get_pin(6)
pin7 = mcp1.get_pin(7)
pin8 = mcp1.get_pin(8)
pin9 = mcp1.get_pin(9)
pin10 = mcp1.get_pin(10)
pin11 = mcp1.get_pin(11)
pin12 = mcp1.get_pin(12)
pin13 = mcp1.get_pin(13)
pin14 = mcp1.get_pin(14)
pin15 = mcp1.get_pin(15)
pin16 = mcp1.get_pin(0)
pin17 = mcp2.get_pin(1)
pin18 = mcp2.get_pin(2)
pin19 = mcp2.get_pin(3)
pin20 = mcp2.get_pin(4)
pin21 = mcp2.get_pin(5)
pin22 = mcp2.get_pin(6)
pin23 = mcp2.get_pin(7)
pin24 = mcp2.get_pin(8)
pin25 = mcp2.get_pin(9)
pin26 = mcp2.get_pin(10)
pin27 = mcp2.get_pin(11)
pin28 = mcp2.get_pin(12)
pin29 = mcp2.get_pin(13)
pin30 = mcp2.get_pin(14)
pin31 = mcp2.get_pin(15)

# Setup pin0 as an output that's at a high logic level.
#pin0.switch_to_output(value=True)
#pin2.switch_to_output(value=True)
#pin3.switch_to_output(value=True)
#pin4.switch_to_output(value=True)
# Setup pin1 as an input with a pull-up resistor enabled.  Notice you can also
# use properties to change this state.
pin0.direction = digitalio.Direction.INPUT
pin0.pull = digitalio.Pull.UP
pin1.direction = digitalio.Direction.INPUT
pin1.pull = digitalio.Pull.UP
pin2.direction = digitalio.Direction.INPUT
pin2.pull = digitalio.Pull.UP
pin3.direction = digitalio.Direction.INPUT
pin3.pull = digitalio.Pull.UP
pin4.direction = digitalio.Direction.INPUT
pin4.pull = digitalio.Pull.UP
#pin5.direction = digitalio.Direction.INPUT
#pin5.pull = digitalio.Pull.UP


# Now loop blinking the pin 0 output and reading the state of pin 1 input.
while True:
    # Blink pin 0 on and then off.
    #pin0.value = True
    #pin1.value = True
    #pin2.value = True
    #pin3.value = True
    #pin4.value = True
    pin5.value = True
    pin6.value = True
    pin7.value = True
    pin8.value = True
    pin9.value = True
    pin10.value = True
    pin11.value = True
    pin12.value = True
    pin13.value = True
    pin14.value = True
    pin15.value = True
    pin16.value = True
    pin17.value = True
    pin18.value = True
    pin19.value = True
    pin20.value = True
    pin21.value = True
    pin22.value = True
    pin23.value = True
    pin18.value = True
    pin19.value = True
    pin20.value = True
    pin21.value = True
    pin22.value = True
    pin23.value = True
    pin24.value = True
    pin25.value = True
    pin26.value = True
    pin27.value = True
    pin28.value = True
    pin29.value = True
    pin30.value = True
    pin31.value = True
    time.sleep(0.5)
    #pin0.value = False
    #pin1.value = False
    #pin2.value = False
    #pin3.value = False
    #pin4.value = False
    pin5.value = False
    pin6.value = False
    pin7.value = False
    pin8.value = False
    pin9.value = False
    pin10.value = False
    pin11.value = False
    pin12.value = False
    pin13.value = False
    pin14.value = False
    pin15.value = False
    pin16.value = False
    pin17.value = False
    pin18.value = False
    pin19.value = False
    pin20.value = False
    pin21.value = False
    pin22.value = False
    pin23.value = False
    pin18.value = False
    pin19.value = False
    pin20.value = False
    pin21.value = False
    pin22.value = False
    pin23.value = False
    pin24.value = False
    pin25.value = False
    pin26.value = False
    pin27.value = False
    pin28.value = False
    pin29.value = False
    pin30.value = False
    pin31.value = False
    time.sleep(0.5)
    # Read pin 1 and print its state.
    """print("Pin 0 is at a high level: {0}".format(pin0.value))
    print("Pin 1 is at a high level: {0}".format(pin1.value))
    print("Pin 2 is at a high level: {0}".format(pin2.value))
    print("Pin 3 is at a high level: {0}".format(pin3.value))
    print("Pin 4 is at a high level: {0}".format(pin4.value))
    print("Pin 5 is at a high level: {0}".format(pin5.value))"""
    if not pin0.value and not pin1.value and not pin2.value and not pin3.value and not pin4.value:
        WaterTank = 60
    elif not pin0.value and not pin1.value and not pin2.value and not pin3.value:
        WaterTank = 50
    elif not pin0.value and not pin1.value and not pin2.value:
        WaterTank = 40
    elif not pin0.value and not pin1.value:
        WaterTank = 25
    elif not pin0.value:
        WaterTank = 10
    Print("Water Tank is: " + WaterTank+"%")
