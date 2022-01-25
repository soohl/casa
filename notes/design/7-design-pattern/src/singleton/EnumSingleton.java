package edu.gatech.oad.patterns.singleton;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by robertwaters on 3/16/17.
 */
public enum  EnumSingleton {
    INSTANCE;

    private Map<String, String> mapData = new HashMap<>();

    EnumSingleton(){ }

    public void addData(String key, String value) {
        mapData.put(key, value);
    }

    public String getData(String key) {
        return mapData.get(key);
    }

}
