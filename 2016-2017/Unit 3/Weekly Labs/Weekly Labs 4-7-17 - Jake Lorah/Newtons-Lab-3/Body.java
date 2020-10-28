import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

import java.util.List;

public class Body extends SmoothMover
{
    private static final double GRAVITY = 7.8;
    private static final Color defaultColor = new Color(255, 216, 0);
    
    private double mass;
    
    /**
     * Construct a Body with default size, mass, movement and color.
     */
    public Body()
    {
        this (20, 300, new Vector(0, 0.0), defaultColor);
    }
    
    /**
     * Construct a Body with a specified size, mass, movement and color.
     */
    public Body(int size, double mass, Vector movement, Color color)
    {
        this.mass = mass;
        addForce(movement);
        GreenfootImage image = new GreenfootImage (size, size);
        image.setColor (color);
        image.fillOval (0, 0, size-1, size-1);
        setImage (image);
    }
    
    /**
     * Act. That is: apply  the gravitation forces from
     * all other bodies around, and then move.
     */
    public void act() 
    {
        applyForces();
        move();
        bounceAtEdge();
    }
    
    /**
     * Check whether we have hit the edge of the universe. If so, bounce off it.
     */
    private void bounceAtEdge()
    {
        if (getX() == 0 || getX() == getWorld().getWidth()-1) {
            setLocation((double)getX(), (double)getY());
            getMovement().revertHorizontal();
            accelerate(0.9);
        }
        else if (getY() == 0 || getY() == getWorld().getHeight()-1) {
            setLocation((double)getX(), (double)getY());
            getMovement().revertVertical();
            accelerate(0.9);
        }
    }
    
    /**
     * Apply the forces of gravity from all other celestial bodies in this universe.
     */
    private void applyForces()
    {
        List<Body> bodies = (List<Body>) getWorld().getObjects(Body.class);
        
        for (Body body : bodies) 
        {
            if (body != this) 
            {
                applyGravity (body);
            }
        }
        
        // ensure that we don't get too fast: If the current speed is very fast, decelerate a bit.
        if (getSpeed() > 7) 
        {
            accelerate (0.9);  // acceleration with factor < 1 is actually slowing down.
        }
    }
    
    /**
     * Apply the gravity force of a given body to this one.
     */
    private void applyGravity(Body other)
    {
        double dx = other.getExactX() - this.getExactX();
        double dy = other.getExactY() - this.getExactY();
        Vector force = new Vector (dx, dy);
        double distance = Math.sqrt (dx*dx + dy*dy);
        double strength = GRAVITY * this.mass * other.mass / (distance * distance);
        double acceleration = strength / this.mass;
        force.setLength (acceleration);
        addForce (force);
    }
    
    /**
     * Return the mass of this body.
     */
    public double getMass()
    {
        return mass;
    }
}
