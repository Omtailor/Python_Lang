# Overide the len method to display the dimensions of the vector


class Vector3D:
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)


# Example usage
v1 = Vector3D([1, 2, 3])
print(len(v1))
