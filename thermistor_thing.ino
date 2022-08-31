#define TMP_SAMPLES 10000
#define FIXED_RES 22000.0f

unsigned long long acc0 = 0;
unsigned long long acc1 = 0;

float res0 = 0;
float res1 = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A5, INPUT);
  pinMode(A0, INPUT);
  //pinMode(A5, INPUT);
  analogReference(EXTERNAL);
}

void loop() {
  // put your main code here, to run repeatedly:
  acc0 = 0;
  acc1 = 0;

  for(int i = 0; i < TMP_SAMPLES; i++){
    analogRead(A0);
    acc0 += analogRead(A0);
    analogRead(A5);
    acc1 += analogRead(A5);
  }

  acc0 = acc0/TMP_SAMPLES;
  acc1 = acc1/TMP_SAMPLES;

  res0 = FIXED_RES*acc0 / (1023-acc0);
  res1 = FIXED_RES*acc1 / (1023-acc1);

  Serial.println(String(res0));
  Serial.println(String(res1));
  //Serial.println(String(analogRead(A5)));
}
