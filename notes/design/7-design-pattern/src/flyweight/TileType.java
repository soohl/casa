/*
 * TileType.java
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
public enum TileType {
  //Type    Max Ore  Max Food  Max NRG   Icon
    RIVER    (0,       4,         1,   "river.png"),
    MOUNTAIN (4,       0,         1,   "mtn.png"),
    PLAINS   (1,       2,         4,   "plain.png");
    
    private int maxore;
    private int maxfood;
    private int maxenergy;
    String myicon;
    
    TileType(int ore, int food, int nrg, String icon) {
        maxore = ore;
        maxfood = food;
        maxenergy = nrg;
        myicon = icon;
    }
    
    public int getOreProduction() { return maxore; }
    public int getFoodProduction() { return maxfood; }
    public int getEnergyProduction() { return maxenergy; }
    public String getIcon() { return myicon; }

}
