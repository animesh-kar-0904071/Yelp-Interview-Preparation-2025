package YELP;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class Record {
    int id;
    String name;
    int age;

    public Record(int id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return id + "," + name + "," + age;
    }



}

public class YelpFileStructureData_XX {

    
    
    public static void main(String[] args) throws IOException {

        List<Record> records = new ArrayList<Record>();
        BufferedReader bufferedReader = null;

        try {
            bufferedReader = new BufferedReader(new FileReader("YELP/yelpFileStructure.txt")); // **
            String line = bufferedReader.readLine(); // Skip header

            while ((line = bufferedReader.readLine()) != null) {
                String[] parts = line.split(",");
                int id = Integer.parseInt(parts[0]);
                String name = parts[1];
                int age = Integer.parseInt(parts[2]);
                records.add(new Record(id, name, age));                
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (Exception e ) {
            e.printStackTrace();
        }finally {
            if (bufferedReader != null)
                bufferedReader.close();
        }

        records.sort(Comparator.comparingInt(r -> r.id));

        records.sort(Comparator.comparingInt(r->r.hashCode()));

        for (Record record: records) {
            System.out.println(record.toString());
        }
        
    }



    
}