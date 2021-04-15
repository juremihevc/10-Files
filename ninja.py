# with open("ninja.txt", "r") as ninja_doc:
#     ninja_lines = ninja_doc.read().splitlines()
#
#     for line in ninja_lines:
#         print(line)

with open("ninja2.txt", "w") as ninja_doc2:
    ninja_doc2.write("Jure was here!")

with open("ninja2.txt", "r") as ninja_doc2:
    ninja_files = ninja_doc2.read()

    print(ninja_files)
