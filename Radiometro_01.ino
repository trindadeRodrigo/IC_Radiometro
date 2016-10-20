#include <Wire.h>
#include <Adafruit_MCP4725.h>
#include <math.h>
#include <PID_v1.h>

#define voltsIn A0

Adafruit_MCP4725 dac; // constructor

#define ThermistorPIN1 0   // Analog Pin 0
#define ThermistorPIN2 1
#define ThermistorPIN3 2


double temp1, temp2, temp3;
double dac_volts = 0;

//Def PID variables and parameters
double Setpoint, Input, Output;
double Kp = 2, Ki = 5, Kd = 1;

PID myPID(&Input, &Output, &Setpoint, Kp, Ki, Kd, DIRECT);

void setup() {
  
 Serial.begin(9600);
 dac.begin(0x60); 

 //turn the PID on
 myPID.SetOutputLimits(0, 4095);
 myPID.SetMode(AUTOMATIC);
 Setpoint = 40;
 
}

void loop() {

  temp1 = Thermistor(analogRead(ThermistorPIN1));           // read ADC and convert it to Celsius
  temp2 = Thermistor(analogRead(ThermistorPIN2));
  temp3 = Thermistor(analogRead(ThermistorPIN3));
  
  Input = temp3;
  myPID.Compute();
  
  dac.setVoltage(Output, false);

  dac_volts = (5.0/4095.0)*Output;
  
  printDouble(temp1, 3, false);     // display Celsius
  printDouble(temp2, 3, false);      // display Celsius
  printDouble(temp3, 3, false);
  
  Serial.println(dac_volts);
 
}
