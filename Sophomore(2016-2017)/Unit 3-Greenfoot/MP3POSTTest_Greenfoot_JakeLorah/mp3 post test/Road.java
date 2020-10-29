import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Road here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Road extends World
{

    /**
     * Constructor for objects of class Road.
     * 
     */
    public Road()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(600, 400, 1); 
    }
    
    public void populateRoad()
    {
        addObject(new Car1(), 300, 300);
        
        addObject(new Car1(), 90, 70);
        addObject(new Car1(), 390, 200);
        addObject(new Car1(), 360, 500);
        
        addObject(new Car2(), 20, 500);
        addObject(new Car2(), 30, 200);
        addObject(new Car2(), 60, 90);
        addObject(new Car2(), 80, 310);
        addObject(new Car2(), 150, 50);
        addObject(new Car2(), 210, 410);
        addObject(new Car2(), 220, 520);
    }
}
