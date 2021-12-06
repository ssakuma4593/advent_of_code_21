def day_2_part_1(instructions: list) -> int:
    horizontal = 0
    depth = 0

    for instruction, units in instructions:
        print(instruction, units)
        unit = int(units)
        if instruction == "forward":
            # print("--Forward", horizontal, "+", unit)
            horizontal += unit
        elif instruction == "down":
            # print("--Depth", depth, "+", unit)
            depth += unit
        elif instruction == "up":
            # print("--Depth", depth, "-", unit)
            depth -= unit
    
    return (horizontal * depth)

def day_2_part_2(instructions: list) -> int:
    horizontal = 0
    depth = 0
    aim = 0

    for instruction, units in instructions:
        print(instruction, units)
        unit = int(units)
        if instruction == "forward":
            # print("--Forward", horizontal, "+", unit)
            # print("--Depth", depth, "+", aim, "*", unit)
            horizontal += unit
            depth = (aim * unit) + depth
            # print("Horizontal: ", horizontal, "Depth: ", depth)
        elif instruction == "down":
            # print("--Aim", aim, "+", unit)
            aim += unit
            # print("Depth: ", depth, "Aim: ", aim)
        elif instruction == "up":
            # print("--Aim", aim, "-", unit)
            aim -= unit
            # print("Depth: ", depth, "Aim: ", aim)
    
    return (horizontal * depth)

    



def main():
    fileObj = open('day_2_input.txt', "r")
    insructions = [instruction.split() for instruction in fileObj.read().splitlines()]
    print(insructions)

    # Part 1
    horizontal_depth_product = day_2_part_1(insructions)
    print("Product: ", horizontal_depth_product)

    # Part 2
    horizontal_depth_product_2 = day_2_part_2(insructions)
    print("Product 2: ", horizontal_depth_product_2)
    
    fileObj.close()

        

if __name__ == "__main__":
    main()
