bool guiControl = true;
bool joyStickControl = false;

#define echoPin 10 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 9 //attach pin D3 Arduino to pin Trig of HC-SR04

// Motor A connections
int enA = 11;
int in1 = 8;
int in2 = 7;
// Motor B connections
int enB = 3;
int in3 = 5;
int in4 = 4;

int pin_f = 22;
int pin_b = 24;
int pin_l = 26;
int pin_r = 28;

int spd = 155;

// defines variables
long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement
int buzzer = 12;//the pin of the active buzzer

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  pinMode(buzzer, OUTPUT); //initialize the buzzer pin as an output
  // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

  pinMode(pin_f, INPUT_PULLUP);
  pinMode(pin_b, INPUT_PULLUP);
  pinMode(pin_l, INPUT_PULLUP);
  pinMode(pin_r, INPUT_PULLUP);

  // Turn off motors - Initial state
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);

  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
}

void loop() {
  // put your main code here, to run repeatedly:

}

void joystickControl()  {

  if (!digitalRead(pin_f) || !digitalRead(pin_b) || !digitalRead(pin_l) || !digitalRead(pin_r)) {
    if (!digitalRead(pin_f)) {
      Serial.println("forward!");
      forward();
    }
    if (!digitalRead(pin_b)) {
      Serial.println("backward!");
      backward();
    }
    if (!digitalRead(pin_l)) {
      Serial.println("left!");
      left();
    }
    if (!digitalRead(pin_r)) {
      Serial.println("right!");
      right();
    }
  }
  else {
    Serial.println("stop!");
    off();
  }
}


  void forward() {
    analogWrite(enA, spd);
    analogWrite(enB, spd);
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
  }
  
  void backward() {
    analogWrite(enA, spd);
    analogWrite(enB, spd);
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
  }
  
  void left() {
    analogWrite(enA, spd);
    analogWrite(enB, spd);
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
  }
  
  void right() {
    analogWrite(enA, spd);
    analogWrite(enB, spd);
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
  }
  
  void off() {
    analogWrite(enA, 0);
    analogWrite(enB, 0);
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, LOW);
  }

}
