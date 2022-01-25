/*
 * Map.java
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
public class Map {
    Tile[][] tiles;
    
    
    public Map(int x, int y) {
        tiles = new Tile[x][y];
        tiles[0][0] = new Tile(TileType.PLAINS);
        tiles[0][1] = new Tile(TileType.MOUNTAIN);
    }
    
    private void addTile(Tile t, int x, int y) {
        tiles[x][y] = t;
    }
    
    public static Map makeFromFile(String fname) {
        return null;
    }

    /**
     * @param args
     */
    public static void main(String[] args) {
        // TODO Auto-generated method stub

    }

}
