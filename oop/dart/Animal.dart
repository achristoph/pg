import 'Being.dart';

class Animal extends Being {
  static int counter = 0;
  int _age;
  String _name;
  Animal(age) {
    this._age = age;
    counter++;
  }
  get name => _name;
  set name(val) => _name = val;

  desc() {
    print("${name} is ${_age}, ${counter}");
  }

  static display() {
    print("${counter} times");
  }
}
