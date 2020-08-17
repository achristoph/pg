import 'dart:collection';

import 'Animal.dart';
import 'Dog.dart';

enum Color { red, green, blue }
List list = List();
Set set = Set();
Queue queue = Queue();
Map map = Map();
// Concatenation
String s = "sky is ${Color.blue}";
String s1 = "Fact: $s";

hello(int a, [bool b = true]) {
  print(b);
}

hi(a, {c, d: 'd'}) {
  print("$a $c $d");
}

main(List<String> args) {
  hi('a', c: 'c');
  var a = Animal(1);
  a.name = "fido";
  a.desc();
  Animal.display();
  var dog = new Dog(11);
  dog.desc();
  dog.fly();
  dog.ride();
  dog.breath();
}
