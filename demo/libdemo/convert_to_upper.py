
source = "test.txt"
target = "upper_test.txt"

try:
    with open(source, "rt") as sf:
        with open(target, "wt") as tf:
            tf.write( sf.read().upper())
except Exception as ex:
    print(ex)

