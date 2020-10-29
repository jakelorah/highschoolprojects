import greenfoot.*;  // imports Actor, World, Greenfoot, GreenfootImage

import java.util.Random;


public class CrabWorld extends World
{
    //    public static final Color pathColor = new Color(227, 202, 148);
    /**
     * Create the crab world (the beach). Our world has a size 
     * of 560x560 cells, where every cell is just 1 pixel.
     */
    public CrabWorld() 
    {
        super(860, 560, 1);
        populateWorld();

        prepare();
    }

    /**
     * Create the objects for the start of the game.
     */
    public void populateWorld()
    {
    
    }

    /**
     * Prepare the world for the start of the program. That is: create the initial
     * objects and add them to the world.
     */
    private void prepare()
    {
        Crab crab = new Crab();
        addObject(crab, 778, 276);
        Crab crab2 = new Crab();
        addObject(crab2, 793, 398);
        Crab crab3 = new Crab();
        addObject(crab3, 779, 488);
        Crab crab4 = new Crab();
        addObject(crab4, 608, 406);
        Crab crab5 = new Crab();
        addObject(crab5, 505, 132);
        Crab crab6 = new Crab();
        addObject(crab6, 659, 92);
        crab6.setLocation(673, 139);
        Crab crab7 = new Crab();
        addObject(crab7, 522, 512);
        Crab crab8 = new Crab();
        addObject(crab8, 144, 342);
        crab3.setLocation(835, 495);
        crab4.setLocation(333, 326);
        Crab crab9 = new Crab();
        addObject(crab9, 264, 533);
        Crab crab10 = new Crab();
        addObject(crab10, 668, 532);
        Crab crab11 = new Crab();
        addObject(crab11, 841, 177);
        Crab crab12 = new Crab();
        addObject(crab12, 534, 367);
        Crab crab13 = new Crab();
        addObject(crab13, 201, 201);
        Crab crab14 = new Crab();
        addObject(crab14, 376, 140);
        Crab crab15 = new Crab();
        addObject(crab15, 154, 528);
        Crab crab16 = new Crab();
        addObject(crab16, 390, 442);
        Crab crab17 = new Crab();
        addObject(crab17, 649, 256);
        Lobster lobster = new Lobster();
        addObject(lobster, 69, 56);
        Lobster lobster2 = new Lobster();
        addObject(lobster2, 266, 145);
        Lobster lobster3 = new Lobster();
        addObject(lobster3, 107, 232);
        Lobster lobster4 = new Lobster();
        addObject(lobster4, 655, 360);
        Lobster lobster5 = new Lobster();
        addObject(lobster5, 753, 93);
        Lobster lobster6 = new Lobster();
        addObject(lobster6, 522, 445);
        Lobster lobster7 = new Lobster();
        addObject(lobster7, 521, 131);
        Lobster lobster8 = new Lobster();
        addObject(lobster8, 185, 467);
        lobster2.setLocation(335, 215);
        lobster7.setLocation(403, 54);
        lobster4.setLocation(623, 275);
        lobster2.setLocation(243, 313);
        lobster7.setLocation(408, 105);
        lobster2.setLocation(236, 171);
        lobster7.setLocation(519, 208);
        lobster2.setLocation(385, 128);
        lobster7.setLocation(466, 190);
        lobster7.setLocation(484, 192);
        lobster7.setLocation(485, 191);
        lobster7.setLocation(532, 202);
        lobster2.setLocation(291, 92);
        lobster7.setLocation(487, 200);
        lobster4.setLocation(712, 302);
        removeObject(lobster7);
        removeObject(lobster3);
        lobster.setLocation(654, 86);
        lobster5.setLocation(750, 92);
        lobster5.setLocation(782, 57);
        lobster2.setLocation(793, 160);
        lobster.setLocation(802, 265);
        lobster4.setLocation(810, 366);
        lobster6.setLocation(816, 466);
        lobster8.setLocation(604, 485);
        removeObject(lobster8);
        lobster5.setLocation(791, 57);
        lobster5.setLocation(474, 61);
        lobster2.setLocation(683, 174);
        lobster4.setLocation(203, 97);
        lobster6.setLocation(481, 263);
        lobster.setLocation(654, 420);
        Lobster lobster9 = new Lobster();
        addObject(lobster9, 794, 295);
        Lobster lobster10 = new Lobster();
        addObject(lobster10, 356, 248);
        Lobster lobster11 = new Lobster();
        addObject(lobster11, 115, 127);
        lobster11.setLocation(98, 164);
        Worm worm = new Worm();
        addObject(worm, 58, 522);
        worm.setLocation(51, 513);
    }
}