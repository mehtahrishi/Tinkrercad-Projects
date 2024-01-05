int ldr = A3;		//assigning ldr pin no.
  int bulb = 7;		//assigning bulb pin no.
  
  void setup()
  {
    pinMode(bulb, OUTPUT);	//setting pinmode as output
    pinMode(ldr, INPUT);	//setting pinmode as input
  }

  void loop()
  {
    if ( analogRead(ldr) > 500)	//reading light intensity
      digitalWrite(bulb, 0);	//turn OFF condition
    
    else
      digitalWrite(bulb, 1);	//turn ON condition
  }