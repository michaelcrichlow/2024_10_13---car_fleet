def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    stack: list[float] = []
    list_of_tuples_from_biggest_to_smallest = sorted(
        zip(position, speed), reverse=True)
    for _, val in enumerate(list_of_tuples_from_biggest_to_smallest):
        pos = val[0]
        vel = val[1]

        distance = target - pos
        if not stack:
            stack.append(distance / vel)
        elif distance / vel > stack[-1]:
            stack.append(distance / vel)

    return len(stack)


def main() -> None:
    val = car_fleet(target=12,
                    position=[10, 8, 0, 5, 3],
                    speed=[2, 4, 1, 1, 3])
    print(val)


if __name__ == '__main__':
    main()
