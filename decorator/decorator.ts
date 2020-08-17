// decorator for functions has three arguments
function readonly(target: Object, key: string, descriptor: PropertyDescriptor) {
  console.log(target);
  console.log(key);
  console.log(descriptor);
  descriptor.writable = false;
  return descriptor;
}

// decorator for classes
function log(...args) {
  return function (target) {
    console.log('===');
    console.log(target, args);
    console.log('===');
  };
}

function wrap(sep) {
  return function (
    target: Object,
    key: string,
    descriptor: PropertyDescriptor
  ) {
    console.log(target, key, descriptor.value);
    const originalFn = descriptor.value;
    descriptor.value = function (...args) {
      console.log(sep);
      const result = originalFn.apply(this, args);
      console.log(sep);
      return result;
    };
  };
}

// class decorator
@log()
class Moon {
  constructor(public radius: number) {}

  // @readonly
  @wrap('xxx')
  circumference() {
    return 2 * Math.PI * this.radius;
  }
}

const moon = new Moon(100);
// moon.circumference = () => 100;
console.log(moon.circumference());
// for (const key of moon) {
//   console.log(key);
// }
