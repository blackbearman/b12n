import os
from xml.etree.ElementTree import parse

paradigms = set()
variants = set()
forms = set()

files = os.listdir("dict")
for file in files:
    if file.endswith(".xml"):
        filename = os.path.join("dict", file)
        print(filename)
        tree = parse(filename)
        root = tree.getroot()
        for paradigm in root:
            paradigms.add(paradigm.attrib["lemma"])
            for variant in paradigm:
                if variant.tag == "Variant":
                    variants.add(variant.attrib["lemma"])
                    for form in variant:
                        if form.tag == "Form":
                            forms.add(form.text)

print("All paradigms ", len(paradigms))
print("All variants ", len(variants))
print("All forms ", len(forms))
