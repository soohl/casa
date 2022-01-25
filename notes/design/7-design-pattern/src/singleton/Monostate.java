package edu.gatech.oad.patterns.singleton;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by robertwaters on 3/16/17.
 */
public class Monostate {
    private static Map<String, String> mapData = new HashMap<>();

    public Monostate() { }

    public void add(String key, String value) {
        mapData.put(key, value);
    }

    public String findKey(String key) {
        return mapData.get(key);
    }
}
