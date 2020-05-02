package collection.list;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.function.Function;

/**
 * list
 */
public class List {
  public static void main(String[] args) {
    var a = Arrays.asList("Art", "b", "ART");

    // 1. Creating a new sorted array with a comparator
    var b = new ArrayList<>(a);
    Collections.sort(b, (x, y) -> {
      return x.toLowerCase().compareTo(y.toLowerCase());
    });

    System.out.println(b);

    // 2. Creating a new sorted array with multiple comparators
    var c = new ArrayList<>(a);
    Collections.sort(b, (x, y) -> {
      return x.toLowerCase().compareTo(y.toLowerCase());
    });
  }

}