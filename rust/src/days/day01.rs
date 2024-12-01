use crate::{Solution, SolutionPair};
use std::fs::read_to_string;

///////////////////////////////////////////////////////////////////////////////

fn solve1(left: &Vec<i32>, right: &Vec<i32>) -> i32 {
    let mut result: i32 = 0;
    let mut sortedleft = left.clone();
    let mut sortedright = right.clone();
    sortedleft.sort();
    sortedright.sort();
    for (i, num) in sortedleft.iter().enumerate() {
        println!("Index {}: {}, {}", i, num, sortedright[i]);
        result += (num - sortedright[i]).abs();
    }
    return result;
}

///////////////////////////////////////////////////////////////////////////////

fn solve2(left: &Vec<i32>, right: &Vec<i32>) -> i32 {
    let mut result: i32 = 0;
    for num in left {
        let mut count: i32 = 0;
        for num2 in right {
            if num == num2 {
                count += 1;
            }
        }
        result += count * num;
    }
    return result;
}

pub fn solve() -> SolutionPair {
    let input = read_to_string("../inputs/day1.txt").unwrap();
    let lines: Vec<&str> = input.lines().collect();
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();
    for line in lines {
        let mut iter = line.split_whitespace();
        left.push(iter.next().unwrap().parse().unwrap());
        right.push(iter.next().unwrap().parse().unwrap());
    }
    println!("{:?}", left);
    let sol1: i32 = solve1(&left, &right);
    let sol2: i32 = solve2(&left, &right);

    (Solution::from(sol1), Solution::from(sol2))
}
