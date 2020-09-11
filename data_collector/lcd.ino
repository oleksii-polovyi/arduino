// Import the Liquid Crystal library
#include <LiquidCrystal.h> 

//Initialise the LCD with the arduino. LiquidCrystal(rs, enable, d4, d5, d6, d7)
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

float voltage = 0;                          //the voltage measured from the TMP36
float degreesC = 0;                         //the temperature in Celsius, calculated from the voltage

String row1 = "Arduino weather";
String row2 = "";

void setup() {  
  Serial.begin(9600);                       //declare serial port
  
  lcd.begin(16, 2);                         // Switch on the LCD screen
}

void loop() {
  voltage = analogRead(A0) * 0.004882813;   //convert the analog reading, which varies from 0 to 1023, back to a voltage value from 0-5 volts
  degreesC = (voltage - 0.5) * 100.0;       //convert the voltage to a temperature in degrees Celsius
  
  lcd.setCursor(0, 0);                      //set the cursor to the 0,0 position (top left corner)
  lcd.print(row1);       
  lcd.setCursor(0, 1);                      //move the cursor to the first space of the bottom row
  
  lcd.print(String(degreesC) + (char)223 + "C");
  Serial.println(String(degreesC));         //send data to the serial port

  delay(1000);                              //delay for 1 second between each reading (this makes the display less noisy)
}
