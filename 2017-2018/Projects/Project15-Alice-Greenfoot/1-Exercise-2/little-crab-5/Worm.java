import greenfoot.World;
import greenfoot.Actor;
import greenfoot.*;

public class Worm extends Animal
{
 public void act()
 {
     checkKeypress();
     move();
    }
 public void checkKeypress()
    {
        if (Greenfoot.isKeyDown("left")) 
        {
            turn(-8);
        }
        if (Greenfoot.isKeyDown("right")) 
        {
            turn(8);
        }
    }
}
