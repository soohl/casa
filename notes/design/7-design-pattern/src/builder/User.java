package edu.gatech.oad.patterns.builder;

/**
 * Created by robertwaters on 3/14/17.
 */
public class User {
    private String name; // mandatory
    private String address; // optional
    private int age; //optional
    private String email; //optional
    private double location; //optional

    private User(UserBuilder builder) {
        name = builder.name;
        address = builder.address;
        age = builder.age;
        email = builder.email;
        location = builder.location;

    }

    public String toString() {
        return name + " " + address + " " + age + " " + email + " " + location;
    }

    public static class UserBuilder {
        private final String name;
        private int age;
        private String address;
        private String email;
        private double location;

        public UserBuilder(String s) {
            name = s;
            address = "none";
            age = -1;
            email = "none@none.com";
            location = 0.0;
        }

        public UserBuilder address(String a) {
            address = a;
            return this;
        }

        public UserBuilder age (int a) {
            age = a;
            return this;
        }

        public UserBuilder email (String e) {
            email = e;
            return this;
        }

        public UserBuilder location(double l) {
            location = l;
            return this;
        }

        public User build() {
            return new User(this);
        }
    }


}
