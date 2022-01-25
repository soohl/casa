/*
 * TestLines.java
 *
 * Version 1.0
 * Copyright 2011 BobSoft Inc
 */
package edu.gatech.oad.patterns.flyweight;


import static org.junit.Assert.*;

import java.awt.Color;
import java.util.Random;

import org.junit.Before;
import org.junit.Test;

/**
 * @author Robert
 * @version 1.0
 *
 */
public class TestLines {
    private static final Color[] colorPallette = {Color.BLACK, Color.BLUE, Color.RED, 
        Color.WHITE, Color.CYAN};
    private static final Random rand = new Random();
    /**
     * @throws java.lang.Exception
     */
    @Before
    public void setUp() throws Exception {
    }
    
    @Test
    public void testLines() {
        for (int i = 0; i < 1000 ; i++) {
            Line line = LineFactory.INSTANCE.getLine(this.getRandomColor());
        }
        assertTrue(LineFactory.INSTANCE.numberOfLines() <= colorPallette.length);
        System.out.println(LineFactory.INSTANCE.numberOfLines());
    }
    
    private Color getRandomColor() {
        int index = rand.nextInt(colorPallette.length);
        return colorPallette[index];
    }

    
}
