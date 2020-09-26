int trigPin = 13;
int echoPin = 11;
float pingTime; // travel time
float speedOfSound = 1234.8; // in km/h
float targetDistance;

void setup() {
    Serial.begin(9600);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

void loop() {
    digitalWrite(trigPin, LOW); // set trigger low
    delayMicroseconds(2000);    // pause to let settle
    digitalWrite(trigPin, HIGH);    // take trip pin HIGH
    delayMicroseconds(10);          // pause with trigger pin HIGH
    digitalWrite(trigPin, LOW);     // finish trigger pulse by bringing it low

    pingTime = pulseIn(echoPin, HIGH);  // microsecond
    pingTime = pingTime/1000000.;    // convert to second
    pingTime = pingTime/3600.;       // convert ping time to hour

    targetDistance = speedOfSound * pingTime;       // gives us inches per ms
    targetDistance = targetDistance / 2;
    targetDistance = targetDistance*100000; // convert to cm from miles

    Serial.println(targetDistance);
    
    delay(1000);
}
