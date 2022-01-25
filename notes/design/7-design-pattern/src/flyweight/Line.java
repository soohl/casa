/*
 * Tile.java
 *
 * Version 1.0
 * Copyright 2011 BobSoft Inc
 */
package edu.gatech.oad.patterns.flyweight;

import java.awt.Color;

/**
 * Represents a single colored line in hte system
 * @author Robert
 * @version 1.0
 *
 */
public class Line {
  
    /** the color of this line */
    private Color myColor;
    
    /**
     * Makes a new Line
     * @param aColor
     */
    public Line(Color aColor) {
        myColor = aColor;
    }

}
