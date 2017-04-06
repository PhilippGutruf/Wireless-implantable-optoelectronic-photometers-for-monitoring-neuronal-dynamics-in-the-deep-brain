/* Philipp Gutruf
 * wireless photometry
 * written for ATmega328P
 * handles data aquisition and wireless dataconnection via IR LED
 * dataconnection is handled via NEC protocol
 */
#include <IRremote.h>

int RECV_PIN = 5; 

IRrecv irrecv(RECV_PIN);

decode_results results;

bool code=false;

void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn();
}

void dump(decode_results *results) 
{
  
  if (results->decode_type == NEC) 
  {
    code=true;
  }
  
}

void loop() 
{
  if (irrecv.decode(&results)) 
  {  
    dump(&results);
    if(code==true)
    {
      Serial.print(millis());
      Serial.print(",");
      Serial.println(results.value);
      code=false;
    }
    irrecv.resume();
  }
}
