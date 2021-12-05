def day_1_part_1(depths: list) -> int:
    last_depth = 0
    current_depth = 0
    count_depth_increased = 0
    
    for depth in depths:
        if last_depth == 0:
            last_depth = depth
            continue

        current_depth = depth

        if current_depth > last_depth:
            count_depth_increased += 1
        #     print(depth, "increased", count_depth_increased)
        # else:
        #     print(depth, "decreased", count_depth_increased)

        # Set last depth for next loop
        last_depth = depth
    return count_depth_increased

def day_1_part_2(depths: list) -> int:
    last_depth = 0
    current_depth = 0
    count_depth_increased = 0
    for i in range(0, len(depths)-2):
        if last_depth == 0:
            last_depth = sum([depths[i], depths[i+1], depths[i+2]])
            continue
        current_depth = sum([depths[i], depths[i+1], depths[i+2]])

        if current_depth > last_depth:
            count_depth_increased += 1
        #     print(last_depth, current_depth, "increased", count_depth_increased)
        # else:
        #     print(last_depth, current_depth, "decreased", count_depth_increased)

        # Set last depth for next loop
        last_depth = current_depth
    return count_depth_increased

    



def main():
    fileObj = open('day_1_input.txt', "r")
    depths = [int(depth) for depth in fileObj.read().splitlines()]
    print(depths)

    # Part 1
    count_depth_increased = day_1_part_1(depths)
    print("Depth increased: ", count_depth_increased)

    # Part 2
    count_depth_increased_2 = day_1_part_2(depths)
    print("Depth increased 2: ", count_depth_increased_2)
    fileObj.close()

        

if __name__ == "__main__":
    main()
