import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Person1 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Person1 extends Actor
{
    /**
     * Act - do whatever the Person1 wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
  public void act()
    {
        if ( Greenfoot.getRandomNumber(100) < 10 )
        {
            turn(0);
        }
        
        checkKeypress();
    }
    
    public void checkKeypress()
    {
        if (Greenfoot.isKeyDown("left")) 
        {
            turn(-4);
        }
        if (Greenfoot.isKeyDown("right")) 
        {
            turn(4);
        }
         if (Greenfoot.isKeyDown("up")) 
        {
            turn(-2);
        }
        if (Greenfoot.isKeyDown("down")) 
        {
            turn(4);
        }
    }
}