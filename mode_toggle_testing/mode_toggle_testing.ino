// Integrated Product Design: Mode toggle testing
// Christina Fong, 11/20/14

// Pin definitions:
const int ledPin = 13;
const int buttonPin = 7;

int val = 0;

void setup() {
  // Open serial port; set data rate to 9600 bits/sec
  Serial.begin(9600);
  
  // Initialize pins
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {
  val = digitalRead(buttonPin);
  if (val == HIGH) { // Button pushed
    digitalWrite(ledPin, LOW);
    Serial.println("Active mode");
    
  }
  else {
    digitalWrite(ledPin, HIGH);
    Serial.println("Passive mode")
  }
}
