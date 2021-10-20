#define joyX A0
#define joyY A1
bool forward = false;
bool backward = false;
bool left = false;
bool right = false;

int blue = 3;
int yellow = 6;
 
void setup() {
  Serial.begin(9600);
}
 
void loop() {
  int xValue = analogRead(joyX);
  int yValue = analogRead(joyY);

  int xHigh = digitalRead(blue);
  int yHigh = digitalRead(yellow);
  
  if (yValue > 511){
    forward = true;
    backward = false;
  }
  else if (yValue < 510){
    forward = false;
    backward = true;
  }
  else{
    forward = false;
    backward = false;
  }
  
  if (xValue > 500){
    right = true;
    left = false;
  }
  else if (xValue < 498){
    right = false;
    left = true;
  }
  else{
    right = false;
    left = false;
  }

  if(xHigh == HIGH){
    Serial.println("BLUE HIGH");
  }
  if(yHigh == HIGH){
    Serial.println("YELLOW HIGH");
  }

  forward = xHigh && yHigh;
  backward = xHigh || yHigh;

  if(forward){
    Serial.print("forward ");
    analogWrite(9,yValue/4);
    analogWrite(10,yValue/4);
    analogWrite(11,yValue/4);
    analogWrite(6,yValue/4);
  }
  if(backward){
    Serial.print("backward ");
    analogWrite(9,0);
    analogWrite(10,0);
    analogWrite(11,0);
    analogWrite(6,0);
  }
  if(left){
    Serial.print("left ");
    analogWrite(9,yValue/4);
    analogWrite(10,yValue/4);
    analogWrite(11,0);
    analogWrite(6,0);
  }
  if(right){
    Serial.print("right ");
    analogWrite(9,0);
    analogWrite(10,0);
    analogWrite(11,yValue/4);
    analogWrite(6,yValue/4);
  }
  Serial.println();
}
