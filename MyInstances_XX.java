package YELP;

import java.util.ArrayList;
import java.util.List;

public class MyInstances_XX {

    private static List<MyInstances_XX> myInstances = new ArrayList<>();

    public MyInstances_XX() {
        myInstances.add(this);
    }

    public static List<MyInstances_XX> getAllInstances() {
        return new ArrayList<>(myInstances);
    }


    public static void main(String[] args) {
        MyInstances_XX m1  = new MyInstances_XX();
        MyInstances_XX m2 = new MyInstances_XX();

        List<MyInstances_XX> allInstances = MyInstances_XX.getAllInstances();
        for (MyInstances_XX obj: allInstances) {
            System.out.println(obj);

        }


    }


    
}
