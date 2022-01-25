/*
 * FlyweightPattern.java
 *
 * Version 1.0
 * Copyright 2011 BobSoft Inc
 */
package edu.gatech.oad.patterns.flyweight;

import java.awt.Color;
import java.util.HashMap;
import java.util.Map;

/**
 * A factory to make instances of lines
 * @author Robert
 * @version 1.0
 *
 */
public class LineFactory {
	/** This factory is a singleton */
    public static final LineFactory INSTANCE = new LineFactory();
    
    /** Keep track of what lines we have already made */
    private Map<Color, Line> lines;
    
    /**
     * Creates a new factory
     */
    private LineFactory() {
        lines = new HashMap<Color, Line>();
    }
    
    /**
     * Try to get a line of a particular color.  If that color line already exists,
     * then just reuse the instance (flyweight).  Otherwise, make a new one.
     * @param aColor
     * @return
     */
    public Line getLine(Color aColor) {
    	//look up this color line in the map
        Line line = lines.get(aColor);
        
        if (line == null) {
        	//didn't find one, so make a new one and add it to the map
            line = new Line(aColor);
            lines.put(aColor, line);
        }
        
        //return the line
        return line;
    }
    
    /**
     * 
     * @return the number of unique created lines in the factory
     */
    public int numberOfLines() {
        return lines.size();
    }
     
}
