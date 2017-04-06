/* Philipp Gutruf
 * 
 * wireless photometry
 * written for attiny84
 * handles data aquisition and wireless dataconnection via IR LED
 * dataconnection is handled via NEC protocol
 */

#include <IRremote.h>
#include <IRremoteInt.h>
IRsend irsend;
void setup()
{
 pinMode(5,OUTPUT);
}

float analogReadXXbit(uint8_t analogPin, uint8_t bits_of_precision, unsigned long num_samples_to_avg)
{
  uint8_t n = bits_of_precision - 10;
  unsigned long oversample_num = 1<<(2*n); 
  uint8_t divisor = 1<<n; 
  unsigned long reading_sum = 0;
  for (unsigned long i=0; i<num_samples_to_avg; i++)
  {
    unsigned long inner_sum = 0;
    for (unsigned long j=0; j<oversample_num; j++)
    {
      inner_sum += analogRead(analogPin);
    }
  unsigned int reading = (inner_sum + (unsigned long)divisor/2UL) >> n; 
    reading_sum += reading;
  }
  float avg_reading = (float)reading_sum/(float)num_samples_to_avg;
  return avg_reading;
}

void loop() 
{
  unsigned long data=0;
  while(1)
  {
    digitalWrite(5,HIGH); 
    data=analogReadXXbit(7, 12, 5);
    digitalWrite(5,LOW);
    irsend.sendNEC(data,12);
  }
  
}

