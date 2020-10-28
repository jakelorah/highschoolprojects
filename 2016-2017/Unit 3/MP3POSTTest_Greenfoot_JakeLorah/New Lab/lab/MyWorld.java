import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class MyWorld here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class MyWorld extends World
{

    /**
     * Constructor for objects of class MyWorld.
     * 
     */
    public MyWorld()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(600, 400, 1); 
        prepare();
    }

    /**
     * Prepare the world for the start of the program.
     * That is: create the initial objects and add them to the world.
     */
    private void prepare()
    {
        car1 car1 = new car1();
        addObject(car1,148,79);
        car2 car2 = new car2();
        addObject(car2,162,251);
        car2.setLocation(181,230);
        car3 car3 = new car3();
        addObject(car3,129,331);
        car2.setLocation(135,175);
        car1.setLocation(97,71);
        car2.setLocation(105,184);
        car3.setLocation(97,308);
        car2.setLocation(99,176);
    }
}
