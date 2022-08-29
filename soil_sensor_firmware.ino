
#define MODE_STREAM 0x0
#define MODE_ACK 0x1
#define MODE_HUM 0x2
#define MODE_TMP 0x4
#define MODE_STRING 0x8
#define MODE_RAW 0x10
#define MODE_RECV_LUT 0x11

//'a', 'b' respectively
#define CMD_ACK 0x61
#define CMD_NEWMODE 0x62

#define PIN_HUM A0

int current_mode = 0;
int incoming_byte = 0;

bool ackd = false;
bool recv_mode = false;

bool stream_mode = false;
bool ack_mode = true;

bool hum_mode = true;
bool temp_mode = true
;
bool string_mode = true;
bool raw_mode = true;

int val_hum = 0;

void setup() {
  pinMode(PIN_HUM, INPUT);
  Serial.begin(9600);

}


void loop() {
  ackd = false;
  if(Serial.available() > 0){
    incoming_byte = Serial.read();
    if(recv_mode){
      current_mode = incoming_byte;
      
      stream_mode = MODE_STREAM & current_mode == MODE_STREAM;
      ack_mode = MODE_ACK & current_mode == MODE_ACK;
      hum_mode = MODE_HUM & current_mode == MODE_HUM;
      string_mode = MODE_STRING & current_mode == MODE_STRING;
      raw_mode = MODE_RAW & current_mode == MODE_RAW;
      
      recv_mode = false;
      //TODO: Test mode receive;
    }
    else if(incoming_byte == CMD_ACK){
      ackd = true;
    }
    else if(incoming_byte == CMD_NEWMODE){
      recv_mode = true;
    }
  }


  if( stream_mode || (ack_mode && ackd)){
    
    if(hum_mode){
      val_hum = analogRead(PIN_HUM);
    }
    //TODO: Implement temp read mode
  }

  if(string_mode){
    
    if(hum_mode && (stream_mode || (ack_mode && ackd) )) Serial.println(val_hum);
    
  } else if(raw_mode){
    
    if(hum_mode && (stream_mode || (ack_mode && ackd) ))Serial.write(val_hum);
    
  }
  
}
