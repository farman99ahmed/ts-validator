"""Prompt"""

def generate_prompt(ts_data):
    """Function to generate prompt"""
    prompt = """
        
    You are a developer and a TypeScript compiler.
    Your task is to validate a given .ts file to ensure it will work correctly.
    You need to read the entire file, identify any issues, and comment out the functions and classes that won't work.
    For each issue, provide a detailed explanation of why it won't work.
    Retain and clearly distinguish the functions and classes that are accurate and error-free.

    Use the following examples as a guide:
    
    Examples:

    
    Example 1:
    
    Input:
    
    class ValidClass {
    greet() {
        console.log("Hello, world!");
    }
    }

    class InvalidClass {
    name: string;

    constructor(name: string) {
        this.name = name;
    }

    greet() {
        return "Hello, " + this.name;
    }
    
    // This method won't work because 'age' is not defined in the class.
    greetWithAge() {
        return "Hello, " + this.name + ". You are " + this.age + " years old.";
    }
    }

    Output:

    class ValidClass {
    greet() {
        console.log("Hello, world!");
    }
    }

    // class InvalidClass {
    //   name: string;
    //
    //   constructor(name: string) {
    //     this.name = name;
    //   }
    //
    //   greet() {
    //     return "Hello, " + this.name;
    //   }
    //   
    //   // This method won't work because 'age' is not defined in the class.
    //   greetWithAge() {
    //     return "Hello, " + this.name + ". You are " + this.age + " years old.";
    //   }
    // }

    
    Example 2:

    Input:

    function add(a: number, b: number): number {
    return a + b;
    }

    function multiply(a, b): number {
    return a * b;
    }

    Output:

    function add(a: number, b: number): number {
    return a + b;
    }

    // function multiply(a, b): number {
    //   // This function won't work because the types of 'a' and 'b' are not defined.
    //   return a * b;
    // }

    Task:

    Now, perform the same validation on the following TypeScript file:

    class User {
    constructor(public name: string, private age: number) {}

    getAge() {
        return this.age;
    }
    
    // This method won't work because 'address' is not defined in the constructor.
    getAddress() {
        return this.address;
    }
    }

    function divide(a: number, b: number): number {
    if (b === 0) {
        throw new Error("Cannot divide by zero.");
    }
    return a / b;
    }

    function subtract(a, b): number {
    return a - b;
    }

    Expected Output:

    class User {
    constructor(public name: string, private age: number) {}

    getAge() {
        return this.age;
    }
    
    // This method won't work because 'address' is not defined in the constructor.
    // getAddress() {
    //   return this.address;
    // }
    }

    function divide(a: number, b: number): number {
    if (b === 0) {
        throw new Error("Cannot divide by zero.");
    }
    return a / b;
    }

    // function subtract(a, b): number {
    //   // This function won't work because the types of 'a' and 'b' are not defined.
    //   return a - b;
    // }


    Use this approach to validate the provided TypeScript file:
    
    """
    return prompt + ts_data
