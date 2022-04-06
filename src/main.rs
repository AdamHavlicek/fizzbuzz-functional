use std::env;

fn add(x: i32) -> impl Fn(i32) -> i32 {
    move |y| x + y
}

fn fizzbuzz(n: &i32) -> String {
    let fizz = || {
        let mut val = String::with_capacity(4);
        if n % 3 == 0 {
            val += "Fizz";
        }

        val
    };
    let buzz = || {
        let mut val = String::with_capacity(4);
        if n % 5 == 0 {
            val += "Buzz"
        } 

        val
    };

    return fizz() + &buzz()
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let list: Vec<String> = (1..=100).map(|n| fizzbuzz(&n)).collect();
    println!("{:?}", list);
}


#[cfg(test)]
mod tests {
    use crate::*;

    #[test]
    fn test_add() {
        // Arrange
        let x = 5;
        let y = 10;
        // Act
        let result = add(x)(y);
        // Assert
        assert_eq!(result, 15);
    }

    #[test]
    fn test_fizzbuzz() {
        // Arrange
        // Act
        let result = fizzbuzz(&3);
        // Assert
        assert_eq!(result.as_str(), "Fizz");
    }

}
