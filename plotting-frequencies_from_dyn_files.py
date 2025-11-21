import numpy as np


def kpath_distance(all_q_points):



    # you need reciprocal matrix below (copy it from scf.out)
    f=open("scf.out", "r")
    for line in f:
        if "b(1) =" in line:
            b1 = list(map(float, line.split()[3:6]))
        if "b(2) =" in line:
            b2 = list(map(float, line.split()[3:6]))
        if "b(3) =" in line:
            b3 = list(map(float, line.split()[3:6]))

    reciprocal_mat = np.array([b1, b2, b3])

    # You need a text file with kpts in fractional coordinates: only float values are accepted in np.loadtxt
    kpts = np.array(all_q_points)

    cart_kpts = kpts @ reciprocal_mat

    distance = 0.0
    distances=[0.0]

    for i in range(len(cart_kpts) - 1):
        distance += np.sqrt(
            (cart_kpts[i, 0] - cart_kpts[i + 1, 0]) ** 2 + (cart_kpts[i, 1] - cart_kpts[i + 1, 1]) ** 2 + (
                        cart_kpts[i, 2] - cart_kpts[i + 1, 2]) ** 2)
        if [cart_kpts[i + 1, 0],  cart_kpts[i + 1, 1], cart_kpts[i + 1, 2]] == [0.5, 0.5, 0.5]:
            print("distance of R point:", distance)
            x = distance

        # print(distance)
        distances.append(distance)
    return distances

# print(lines)/


if __name__ == "__main__":

    files = []
    # creating a list containing the names of all dyn files.
    for i in range(1, 21):
        files.append("As.dyn" + str(i))  # list of files

    all_frequencies = []
    all_qpoints = []

    for file_name in files:
        f = open(file_name, "r")
        frequencies = []

        for line in f:

            if "Diagonalizing the dynamical matrix" in line:
                next(f)
                next_line = next(f)
                # 3:6 picks up qx (at 3), qy (at 4), qz(at 5)
                q_point = list(map(float, next_line.split()[3:6]))

            if "freq " in line:
                # 7 picks up frequency in cm-1
                frequencies.append(float(line.split()[7]))

        all_frequencies.append(frequencies)
        all_qpoints.append(q_point)




    distances = kpath_distance(all_qpoints)
    print(distances[0], distances[-1])


    g=open("file.dat","w")

    for i in range(len(distances)):
        g.write(str(distances[i]) +" " + str(all_frequencies[i][0]) +"  " +  str(all_frequencies[i][1])
                + " " + str(all_frequencies[i][2]) +"\n")
