x = 5
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(x,y)

"""
PHP:
if(x > 1){
    y = 3 * x - 5;
} elseif(x >= -1){
    y = x + 2;
} else{
    y = 5 * x + 3;
}
"""


# switch/case 使用字典 实现
def num_to_string(num):
    numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three"
    }

    return numbers.get(num, None)


if __name__ == "__main__":
    print(num_to_string(2))
    print(num_to_string(5))
