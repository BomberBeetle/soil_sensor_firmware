import scale

scale.start(port="/dev/ttyS0")

data = scale.read(raw=True)

print(data)
