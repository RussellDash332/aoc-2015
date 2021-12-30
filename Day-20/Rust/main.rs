fn get_input() -> String {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).expect("Failed");
    buffer
}

fn main() {
    let target = get_input().trim().parse::<usize>().unwrap();
    let mut presents = [0; 1000000];
    for i in 1..presents.len() {
        for j in (i - 1..presents.len()).step_by(i) {
            presents[j] += 10 * i;
        }
        if presents[i - 1] >= target {
            println!("Part 1: {}", i);
            break;
        }
    }

    presents = [0; 1000000];
    let mut tmp;
    for i in 1..presents.len() {
        tmp = i - 1;
        for _ in 0..50 {
            if tmp >= presents.len() {
                break;
            }
            presents[tmp] += 11 * i;
            tmp += i;
        }
        if presents[i - 1] >= target {
            println!("Part 2: {}", i);
            break;
        }
    }
}