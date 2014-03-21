typedef enum
{
   INIT = 0;
   LOWER_FEEDER = 1;
   RETRACT_THROWER = 2;
   MOVE_FORWARD = 3;
   STOP = 4;
   THROW = 5;
   LOWER_THROWER = 6;
} STATE;

class LowerFeeder{
public:
LowerFeeder(){complete = false;}
void iterate(){complete = true;}
bool complete;
};

int main()
{
   STATE state = INIT;
   LowerFeeder lowerFeeder;

   while(1)
   {
      if (state == INIT)
      {
         state = LOWER_FEEDER;
      }
      else if (state == LOWER_FEEDER)
      {
          lowerFeeder.iterate();
          if(lowerFeeder.complete)
          {
              state = RETRACT_THROWER;
          }
      }
   }
   return 0;
}

