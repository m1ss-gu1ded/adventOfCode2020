with open("input_14.txt") as file:
    data = file.readlines()
data = [x.strip() for x in data]
data = [x.split(" = ") for x in data]

mem = {}
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# read line for line
for index in range(len(data)):
    instruction = data[index][0]
    if instruction == "mask":
        mask = data[index][1]
    else:
        # isolate the address
        instruction = instruction.removeprefix("mem[")
        instruction = int(instruction.removesuffix("]"))
        # convert value
        number = f"{int(data[index][1]):036b}"
        new_number = ""
        # loop over mask
        for i in range(36):
            # 0 or 1: overwrite
            if mask[i] != "X":
                new_number += mask[i]
            # X: overwrite
            else:
                new_number += number[i]
        mem.update({instruction: new_number})
print(mem)

val_sum = 0
for val in mem.values():
    val_sum += int(val, 2)

print(f"sum of all values: {val_sum}")
