int forward;
int backward;
int left;
int right;

int fwd = 10;
int bwd = 11;
int lft = 12;
int rt = 13;

int rb = 2;
int bb = 3;
int yb = 4;
int gb = 5;

int rf = 6;
int bf = 7;
int yf = 8;
int gf = 9;
 
void setup() {
  Serial.begin(9600);
}
 
void loop() {
  forward = !digitalRead(fwd);
  backward = !digitalRead(bwd);
  left = !digitalRead(lft);
  right = !digitalRead(rt);
  
  if(forward){
    
    Serial.println("forward");
    int val1 = HIGH;
    digitalWrite(rf,val1);
    digitalWrite(bf,val1);
    digitalWrite(yf,val1);
    digitalWrite(gf,val1);

    int val2 = LOW;
    digitalWrite(rb,val2);
    digitalWrite(bb,val2);
    digitalWrite(yb,val2);
    digitalWrite(gb,val2);
  }
  else if(backward){
    Serial.println("backward");
    int val1 = LOW;
    digitalWrite(rf,val1);
    digitalWrite(bf,val1);
    digitalWrite(yf,val1);
    digitalWrite(gf,val1);

    int val2 = HIGH;
    digitalWrite(rb,val2);
    digitalWrite(bb,val2);
    digitalWrite(yb,val2);
    digitalWrite(gb,val2);
  }
  else if(left){
    Serial.println("left");
    int val1 = HIGH;
    int val2 = LOW;
    
    digitalWrite(rf,val2);
    digitalWrite(bf,val1);
    digitalWrite(yf,val1);
    digitalWrite(gf,val2);
    
    digitalWrite(rb,val1);
    digitalWrite(bb,val2);
    digitalWrite(yb,val2);
    digitalWrite(gb,val1);
  }
  else if(right){
    Serial.println("right");
    int val1 = LOW;
    int val2 = HIGH;
    
    digitalWrite(rf,val2);
    digitalWrite(bf,val1);
    digitalWrite(yf,val1);
    digitalWrite(gf,val2);
    
    digitalWrite(rb,val1);
    digitalWrite(bb,val2);
    digitalWrite(yb,val2);
    digitalWrite(gb,val1);
  }
  else{
    Serial.println("stop");
    int val1 = LOW;
    digitalWrite(rf,val1);
    digitalWrite(bf,val1);
    digitalWrite(yf,val1);
    digitalWrite(gf,val1);

    int val2 = LOW;
    digitalWrite(rb,val2);
    digitalWrite(bb,val2);
    digitalWrite(yb,val2);
    digitalWrite(gb,val2);
  }
}
