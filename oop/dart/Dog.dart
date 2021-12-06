import 'Animal.dart';
import 'Mountable.dart';
import 'Wing.dart';

class Dog extends Animal with Wing implements Mountable {
  Dog(age) : super(age) {}

  ride() {
    print('riding');
  }
}
