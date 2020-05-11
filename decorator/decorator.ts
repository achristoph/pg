// decorator fo functions require to have three arguments
function readonly(target: Object, key: string, descriptor: PropertyDescriptor) {
  console.log(target);
  console.log(key);
  console.log(descriptor);
  descriptor.writable = false;
  return descriptor;
}

//
function log(args) {
  return function (target) {
    console.log('===');
    console.log(target, args);
    console.log('===');
  };
}

function wrap() {
  return function (
    target: Object,
    key: string,
    descriptor: PropertyDescriptor
  ) {
    console.log('===');
    console.log(target);
    console.log('===');
  };
}

// class decorator
@log('arguments')
class Moon {
  constructor(public radius: number) {}

  // @readonly
  @wrap()
  circumference() {
    return 2 * Math.PI * this.radius;
  }
}

const moon = new Moon(100);
moon.circumference = () => 100;
// for (const key of moon) {
//   console.log(key);
// }
