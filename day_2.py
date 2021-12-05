def day_2_part_1(instructions: list) -> tuple:
    horizontal = 0
    depth = 0

    for instruction, units in instructions:
        if instruction == "forward":
            horizontal += int(units)
        elif instruction == "down":
            depth += int(units)
        elif instruction == "up":
            depth -= int(units)
    
    return (horizontal, depth)

    



def main():
    fileObj = open('day_2_input.txt', "r")
    insructions = [instruction.split() for instruction in fileObj.read().splitlines()]
    print(insructions)

    # Part 1
    horizontal, depth = day_2_part_1(insructions)
    print("Horizontal: ", horizontal)
    print("Depth: ", depth)

    
    # day_2_part_2(depths)
    fileObj.close()

        

if __name__ == "__main__":
    main()
