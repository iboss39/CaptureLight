int ledPin = 3;
int delayms = 200;

void setup() {
  pinMode(ledPin, OUTPUT);
}

int myNum=0;

void loop() {
  printPrefix();
  printNum(myNum);
  myNum++;
  if(myNum>9)
    myNum=0;
}

void printPrefix()
{
  printOne();
  printOne();
  printZero();
}
void printNum(int num)
{
  int bitCnt=0;
  while(num>0)
  {
    if(num%2==0)
      printZero();      
    else
      printOne();
    bitCnt++;
    num/=2;
  }
  if(bitCnt<4)
  {
    for(int i=0;i<4-bitCnt;i++)
      printZero();
  }
}

void printOne()
{
  digitalWrite(ledPin, HIGH);
  delay(delayms);
}

void printZero()
{
  digitalWrite(ledPin, LOW);
  delay(delayms);
}
