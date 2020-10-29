import greenfoot.*;  // imports Actor, World, Greenfoot, GreenfootImage

import java.util.Random;
import java.awt.Color;

public class CrabWorld extends World
{
    //    public static final Color pathColor = new Color(227, 202, 148);
    /**
     * Create the crab world (the beach). Our world has a size 
     * of 560x560 cells, where every cell is just 1 pixel.
     */
    public CrabWorld() 
    {
        super(560, 560, 1);
        populateWorld();

        prepare();
    }

    /**
     * Create the objects for the start of the game.
     */
    public void populateWorld()
    {
        addObject(new Crab(), 300, 300);

        addObject(new Lobster(), 90, 70);
        addObject(new Lobster(), 390, 200);
        addObject(new Lobster(), 360, 500);
        addObject(new dolphin(), 60, 180);
        addObject(new dolphin(), 390, 23);
        addObject(new fish1(), 12, 24);
     

        
    }

    /**
     * Prepare the world for the start of the program. That is: create the initial
     * objects and add them to the world.
     */
    private void prepare()
    {
        dolphin dolphin = new dolphin();
        addObject(dolphin, 379, 64);
        dolphin dolphin2 = new dolphin();
        addObject(dolphin2, 81, 393);
        fish1 fish1 = new fish1();
        addObject(fish1, 277, 202);
        fish2 fish2 = new fish2();
        addObject(fish2, 519, 403);
        fish3 fish3 = new fish3();
        addObject(fish3, 330, 425);
        fish2.setLocation(166, 252);
        fish2 fish22 = new fish2();
        addObject(fish22, 509, 156);
        fish2 fish23 = new fish2();
        addObject(fish23, 125, 131);
    }
}