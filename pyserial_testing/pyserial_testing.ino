// Testing Arduino-pyserial connection
// Christina Fong, 11/17/14

// Pin definitions
const int ledPin = 13;

void setup() {
  // Open serial port (data rate = 9600 baud)
  Serial.begin(9600);
  
  // Initialize pins as output:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    Serial.print("testing");
    char c = Serial.read();
    if (c == 'H') {
      digitalWrite(ledPin, HIGH);
    }
    else if (c == 'L') {
      digitalWrite(ledPin, LOW);
    }
  }
}
