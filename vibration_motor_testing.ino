// Integrated Product Design: Vibration testing
// Christina Fong, 11/2/14

// Pin definitions:
const int vibePin = 3;
const int ledPin = 9;

// Variable definitions: 
int maxDistance = 10;     // Max detectable distance (ft)
int minDistance = 0;      // Min detectable distance (ft)
//int angle  = -1;        // Angle direction (clockwise from front)
int distance = -1;        // Distance from person (ft)
int intensity = -1;       // Vibration intensity
int vibePattern = -1;     // Vibration pattern

void setup() {
  // Open serial port; set data rate to 9600 bits/sec
  Serial.begin(9600);
  
  // Initialize pins as output:
  pinMode(ledPin, OUTPUT);
  }

void loop() {
  while (Serial.available() > 0) {
    // Reads serial information entered as distance, vibePattern
//    angle = Serial.parseInt()
    distance = Serial.parseInt();
    vibePattern = Serial.parseInt();
    
    if (Serial.read() == '!') {
      // Seriously add some in range and coerce constrains here 
      Serial.println();
      runVibe();
    }
  }
}

void runVibe() {
  // Maps distance to vibration intensity
  intensity = map(distance, minDistance, maxDistance, 0, 255);
  Serial.print("Vibration intensity: ");
  Serial.println(intensity);  
  
  switch (vibePattern) {
    case 0:
      Serial.print("1 second vibration");
      analogWrite(ledPin, intensity);
      analogWrite(vibePin, intensity);
      delay(1000);
      digitalWrite(ledPin, LOW);
      digitalWrite(vibePin, LOW);
      break;  
    case 1:
      Serial.print("2 second vibration");
      analogWrite(ledPin, intensity);
      analogWrite(vibePin, intensity);
      delay(2000);
      digitalWrite(ledPin, LOW);
      digitalWrite(vibePin, LOW);
      break;
    case 2:
      Serial.print("0.25s on-0.25s off pulses");
      for (int i=0; i<2; i++) {
        analogWrite(ledPin, intensity);
        analogWrite(vibePin, intensity);
        delay(250);
        digitalWrite(ledPin, LOW);
        digitalWrite(vibePin, LOW);
        delay(250);
      }
      break;
    case 3:
      Serial.print("0.5s on-0.5s off pulses");
      for (int i=0; i<2; i++) {
        analogWrite(ledPin, intensity);
        analogWrite(vibePin, intensity);
        delay(500);
        digitalWrite(ledPin, LOW);
        digitalWrite(vibePin, LOW);
        delay(500);
      }
      break;
    default:
      Serial.print("Not a valid pattern");
      break;
    
    Serial.println();
  }
}
