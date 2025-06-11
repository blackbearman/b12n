import os
import locale

from xml.etree.ElementTree import parse


def write_list(filename, lines):
    with open(filename, 'w') as f:
        prev = ""
        for line in lines:
            if line != prev:
                f.write(f"{line}\n")
            prev = line


if __name__ == "__main__":
    paradigms = 0
    variants = 0
    forms = 0
    words = []

    files = os.listdir("dict")
    for file in files:
        if file.endswith(".xml"):
            name = os.path.join("dict", file)
            print(name)
            tree = parse(name)
            root = tree.getroot()
            for paradigm in root:
                if paradigm.tag == "Paradigm":
                    paradigms += 1
                    for variant in paradigm:
                        if variant.tag == "Variant":
                            variants += 1
                            for form in variant:
                                if form.tag == "Form":
                                    forms += 1
                                    words.append(form.text)

    print("All paradigms ", paradigms)

    loc = locale.getlocale()  # get current locale
    # use By locale; name might vary with platform
    locale.setlocale(locale.LC_ALL, 'be_BY.utf8')

    words.sort(key=locale.strxfrm)

    write_list("dict/spellchecker/slovy-2023-stress.txt", words)

    print("All variants ", variants)

    reversed_words = [word[::-1] for word in words]
    reversed_words.sort(key=locale.strxfrm)
    sorted_words = [word[::-1] for word in reversed_words]

    write_list("dict/adv/slovy-2023-stress.txt", sorted_words)

    locale.setlocale(locale.LC_ALL, loc)  # restore saved locale
    print("All forms ", forms)
