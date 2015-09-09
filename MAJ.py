def BM_voting_algo(data):
    candidate = 0
    count = 0
    for x in data:
        if(count == 0):
            candidate = x
            count = 1
        else:
            if(candidate == x):
                count += 1
            else:
                count -= 1
    count = 0
    for x in data:
        if x == candidate:
            count += 1
    if(count <= len(data)/2):
        candidate = -1
    return candidate


def main():
     
    with open('data/maj.txt') as input_data:
        next(input_data)  # Skip the first line, as we don't need that information.
        arrays = [map(int, line.strip().split()) for line in input_data]

    # Get the majority element of each array.
    maj_elmts = map(str, [BM_voting_algo(a) for a in arrays])

    # Print and save the answer.
    print ' '.join(maj_elmts)
    with open('output/output_MAJ.txt', 'w') as output_data:
        output_data.write(' '.join(maj_elmts))

if __name__ == '__main__':
    main()