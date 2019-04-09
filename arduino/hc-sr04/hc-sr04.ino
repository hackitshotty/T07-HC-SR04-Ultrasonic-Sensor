/*
 * Maker's Digest
 *
 * <description>
 */

int triggerPin = 11;
int echoPin = 12;

long duration, cm, in, mm;


/* End Optional */

void setup() {
  Serial.begin(19200);
  Serial.println("Makers Digest: Ready");

  pinMode(triggerPin, OUTPUT);            // Set the Trigger pin to OUTPUT
  pinMode(echoPin, INPUT);                // Set the Echo Pin to INPUT
}

void loop() {
  /*
   * Trigger the sensor by a HIGH pulse. Needs to be at least
   * 10 microseconds. The shorter 5ms LOW pulse is just to make
   * sure that the 10ms pulse is clean. 
   */
  digitalWrite(triggerPin, LOW);          // Set pin to LOW
  delayMicroseconds(5);                   // Wait 5 microseconds
  
  digitalWrite(triggerPin, HIGH);         // Set pin to HIGH
  delayMicroseconds(10);                  // Wait 10 microseconds (10ms HIGH pulse)
  digitalWrite(triggerPin, LOW);          // Set pin to LOW (End 10ms HIGH pulse)

  duration = pulseIn(echoPin, HIGH);      // Read how long it takes for the pin
                                          // to go from LOW to HIGH. 

  /*
   * Notes about converting from duration to time
   * 
   * Our duration is a round trip, so we need to divide that by 2
   * for the total length of the one way trip. 
   * 
   * Speed of sound is 343 meters per second at sea level. Convert to
   * centimeters per microsecond (0.0343). Same with inches, inches
   * per second at sea level is 13503.9. Covert to inches per microsecond
   * (0.0135)
   */
  
  cm = (duration / 2) * 0.0343;             // Convert duration to centimeters
  in = (duration / 2) * 0.0135;             // Convert duration to inches

  // Display data in Serial Console.
  Serial.print("in: ");
  Serial.print(in);
  Serial.print("\t");
  Serial.print("cm: ");
  Serial.println(cm);


  delay(250);                              // Wait .25 second and do it again!


}
