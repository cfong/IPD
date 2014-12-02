// Integrated Product Design: Vibration testing
// Christina Fong, 11/2/14

// Pin definitions:
const int vibePin = 3;
const int ledPin = 9;
const int potPin = A0;

// Variable definitions: 
int maxDistance = 25;     // Max detectable distance (ft)
int minDistance = 1;      // Min detectable distance (ft)

//int angle  = -1;        // Angle direction (clockwise from front)
int distance = -1;        // Distance from person (ft)
int intensity = -1;       // Vibration intensity
int potVal = 0;

void setup() {
  // Open serial port; set data rate to 9600 bits/sec
  Serial.begin(9600);
  
  // Initialize pins as output:
  pinMode(ledPin, OUTPUT);
  pinMode(vibePin, OUTPUT);
  }

void loop() {
  potVal = analogRead(potPin);
//  Serial.println(potVal);
  
  maxDistance = map(potVal,0, 1023, 10, 25);
//  Serial.println(maxDistance);
  
  Serial.print("Maximum distance: ");
  Serial.println(maxDistance);
  Serial.print("Alert at: ");
  Serial.print(maxDistance);
  Serial.print(',');
  Serial.print(maxDistance*0.67);
  Serial.print(',');
  Serial.println(maxDistance*0.33);
  Serial.println("*****************");
  
  delay(1000);
  
//  for (distance = maxDistance; distance>=minDistance; distance-=3) {
//    runVibe();
//  }
  
//  while (Serial.available() > 0) {
//    // Reads serial information entered as distance, vibePattern
////    angle = Serial.parseInt()
//    distance = Serial.parseInt();
//    
//    if (Serial.read() == '!') {
//      // Seriously add some in range and coerce constrains here 
//      Serial.println();
//      runVibe();
//    }
//  }
}

void runVibe() {
  // Maps distance to vibration intensity
  intensity = map(distance, minDistance, maxDistance, 255, 0);
  Serial.print("Current distance away: ");
  Serial.println(distance);
  Serial.print("Max range: ");
  Serial.println(maxDistance);
  Serial.print("Vibration intensity: ");
  Serial.println(intensity);  
  Serial.println("*******************");
  
  analogWrite(ledPin, intensity);
  analogWrite(vibePin, intensity);
  delay(1000);
  digitalWrite(ledPin, LOW);
  digitalWrite(vibePin, LOW);
 
  Serial.println();
}
