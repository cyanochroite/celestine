from celestine.application.translator.file import save


todo = [
    "BG",
    "CS",
    "DA",
    "DE",
    "EL",
    "EN",
    "ES",
    "ET",
    "FI",
    "FR",
    "HR",
    "HU",
    "IT",
    "LT",
    "LV",
    "MT",
    "NL",
    "PL",
    "PT",
    "RO",
    "SK",
    "SL",
    "SV",
]

for item in todo:
    data = []
    path = F"../../hold/EUPL v1_2 {item}.txt"
    with open(path, "rt", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.replace("  ", " ")
            data.append(line)

    path = F"../../hold/EUPL_1.2_{item}.txt"
    save(path, "\n".join(data))
`
