package edu.gatech.oad.patterns.builder;

/**
 * Created by robertwaters on 3/14/17.
 */
public class BuilderExample {

    public static void main(String args[]) {
        User user = new User.UserBuilder("Sally").build();
        System.out.println(user);

        User u = new User.UserBuilder("Bob").age(25).location(7.6).build();
        System.out.println(u);

        User u1 = new User.UserBuilder("freddy").address("105 Freemont").email("freddy@kruger.com").build();
        System.out.println(u1);
    }
}
