#define PIN_TMP0 A0
#define PIN_TMP1 A1
#define PIN_HUM A5

const int TMP_SAMPLES = 100;

long tmp0, tmp1, hum = 0;
int interval = 0;
int dataIn = 0;

void setup() {
  analogReference(EXTERNAL);
  pinMode(PIN_TMP0, INPUT);
  pinMode(PIN_TMP1, INPUT);
  pinMode(PIN_HUM, INPUT);
 Serial.begin(9600);
}

void loop() {
  tmp0 = 0;
  tmp1 = 0;
  interval = millis();
  for(int i = 0; i < TMP_SAMPLES; i++){
    tmp0 += analogRead(PIN_TMP0);
    tmp1 += analogRead(PIN_TMP1);
  }
  interval = millis() - interval;
  hum = analogRead(PIN_HUM);
  if(Serial.available() > 0){
    dataIn = Serial.read();
    if(dataIn == 'a'){
        Serial.write((byte*)&hum, 2);
        Serial.write((byte*)&tmp0, 4);
        Serial.write((byte*)&tmp1, 4);
    }
    else if(dataIn == 's'){
      Serial.write((byte*)&TMP_SAMPLES, 2);
    }
    else Serial.write(dataIn);
  }
}
