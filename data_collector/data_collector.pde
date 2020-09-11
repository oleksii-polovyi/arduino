import processing.serial.*;

PrintWriter output;
Serial udSerial;

void setup() {
  udSerial = new Serial(this, Serial.list()[0], 9600);
  output = createWriter ("data.txt");
}

void draw() {
  if (udSerial.available() > 0) {
    String SenVal = udSerial.readString();
    if (SenVal != null) {
      output.print(SenVal);
    }
  }
}

void keyPressed(){
  output.flush();
  output.close();
  exit();
}
