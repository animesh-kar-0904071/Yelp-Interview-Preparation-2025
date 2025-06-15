package YELP;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

public class YelpIterator {


    public static void main(String[] args) {

        List<String> names = new ArrayList<String>();
        StringBuilder stringBuilder = new StringBuilder();

        names.add("Guru1");
        names.add("Guru2");
        names.add("Guru3");
        names.add("Guru4");
        names.add("Guru5");

        //System.out.println("aaa");

        // ListIterator<String> listIterator = names.listIterator(names.size());

        // while (listIterator.hasPrevious()) {
        //     stringBuilder.append(listIterator.previous());
        // }

        Iterator<String> iterator = names.iterator();

        while (iterator.hasNext()) {
            String name = iterator.next();
            if (name.equals("Guru2")) {
                iterator.remove();
            }
            
        }

       System.out.println(stringBuilder.toString());
        
    }
}