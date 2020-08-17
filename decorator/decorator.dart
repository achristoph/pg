class Todo {
  final String who;
  final String what;

  const Todo(this.who, this.what);
}

main(List<String> args) {
  @Todo('seth', 'make this do something')
  void doSomething() {
    print('do something');
  }

  doSomething();
}
