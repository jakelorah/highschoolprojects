import greenfoot.*;  // (World, Actor, GreenfootImage, and Greenfoot)

/**
 * This class defines a crab. Crabs live on the beach. They like sand worms 
 * (very yummy, especially the green ones).
 * 
 * Version: 5
 * 
 * In this version, the crab behaves as before, but we add animation of the 
 * image.
 */

public class Crab extends Animal
{
    private GreenfootImage image1;
    private GreenfootImage image2;
    private int wormsEaten;
    
    /**
     * Create a crab and initialize its two images.
     */
    public Crab()
    {
        image1 = new GreenfootImage("snowflake1.png");
        image2 = new GreenfootImage("snowflake1.png");
        setImage(image1);
        wormsEaten = 0;
    }
        
    /** 
     * Act - do whatever the crab wants to do. This method is called whenever
     *  the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act()

    {
    
        if ( atWorldEdge() )
        {
            turn(17);
        }
        
        if ( Greenfoot.getRandomNumber(100) < 10 )
        {
            turn(5);
        }
        
       
        move(2);

        switchImage();
        

    }
    
    /**
     * Alternate the crab's image between image1 and image2.
     */
    public void switchImage()
    {
        if (getImage() == image1) 
        {
            setImage(image2);
        }
        else
        {
            setImage(image1);
        }
    }
            
    
    
    /**
     * Check whether we have stumbled upon a worm.
     * If we have, eat it. If not, do nothing. If we have
     * eaten eight worms, we win.
     */
   public void lookForWorm()
    {
        if ( canSee(Worm.class) ) 
        {
            eat(Worm.class);
            Greenfoot.playSound("slurp.wav");
            
            wormsEaten = wormsEaten + 1;
            if (wormsEaten == 8) 
            {
                Greenfoot.playSound("fanfare.wav");
                         getWorld().setBackground("gameover.png");
                Greenfoot.stop();
            }
        }
    }
}