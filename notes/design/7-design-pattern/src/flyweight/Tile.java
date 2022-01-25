/*
 * Tile.java
 *
 * Version 1.0
 *
 * Copyright 2013 CS2340 Productions, Inc
 */
package edu.gatech.oad.patterns.flyweight;

/**
 * This class 
 * @author Robert
 * @version 1.0
 *
 */
public class Tile {
    TileType type;
    Player owner;
    Mule mymule;
    
    public Tile (TileType t) {
        type = t;
        owner = null;
        mymule = null;
    }
    
    public boolean isOwned() {
        return owner != null;
    }
    
    public boolean hasMule() {
        return mymule != null;
    }
    
    public int getProduction() {
        if (hasMule()) {
            return mymule.getProductionFor(type);
        } else {
            return 0;
        }
    }

}
