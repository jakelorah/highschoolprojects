import greenfoot.*;  // (World, Actor, GreenfootImage, and Greenfoot)

public class Key extends Actor
{
    private boolean isDown;
    private String key;
    private String sound;
    private String upImage;
    private String downImage;
    /**
     * Create a new key.
     */
    public Key()
    {
        sound = ;
        key = keyName;
        upImage = img1;
        downImage = img2;
        setImage(upImage);
        isDown = false;  
    }

    /**
     * Do the action for this key.
     */
    public void act()
    {
       if (!isDown && Greenfoot.isKeyDown(key)) {
            play();
            setImage(downImage);
            isDown = true;
        }
        if (isDown && !Greenfoot.isKeyDown(key)) {
            setImage(upImage);
            isDown = false;
        }
        
    }
    
    /**
     * Play the note of this key.
     */
    public void play()
    {
        Greenfoot.playSound("3a.wav");
    }
}