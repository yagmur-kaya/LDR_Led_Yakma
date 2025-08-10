#define Led 7
#define LDR A0
void setup() {
  pinMode(Led,OUTPUT);
  pinMode(LDR,INPUT);
  Serial.begin(9600);
  

}

void loop() {
  int isik=analogRead(A0);
  Serial.println(isik);
  if (Serial.available()){
    char komut=Serial.read();
    if (komut=='1'){
      digitalWrite(Led,HIGH);
    } else if (komut=='0'){
      digitalWrite(Led,LOW);
    }
  }
 delay(50);

}
