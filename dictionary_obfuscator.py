dictionary = ["zoophyte",
"zoophytes",
"zoophytic",
"zoophytical",
"zoophytish",
"zoophytography",
"zoophytoid",
"zoophytology",
"zoophytological",
"zoophytologist",
"zoophobe",
"zoophobes",
"zoophobia",
"zoophobous",
"zoophori",
"zoophoric",
"zoophorous",
"zoophorus",
"zooplankton",
"zooplanktonic",
"zooplasty",
"zooplastic",
"zoopraxiscope",
"zoopsia",
"zoopsychology",
"zoopsychological",
"zoopsychologist",
"zoos",
"zooAs",
"zooscopy",
"zooscopic",
"zoosis",
"zoosmosis",
"zoosperm",
"zoospermatic",
"zoospermia",
"zoospermium",
"zoosperms",
"zoospgia",
"zoosphere",
"zoosporange",
"zoosporangia",
"zoosporangial",
"zoosporangiophore",
"zoosporangium",
"zoospore",
"zoospores",
"zoosporic",
"zoosporiferous",
"zoosporocyst",
"zoosporous",
"zoosterol",
"zootaxy",
"zootaxonomist",
"zootechny",
"zootechnic",
"zootechnical",
"zootechnician",
"zootechnics",
"zooter",
"zoothecia",
"zoothecial",
"zoothecium",
"zootheism",
"zootheist",
"zootheistic",
"zootherapy",
"zoothome",
"zooty",
"zootic",
"zootype",
"zootypic",
"Zootoca",
"zootomy",
"zootomic",
"zootomical",
"zootomically",
"zootomies",
"zootomist",
"zoototemism",
"zootoxin",
"zootrophy",
"zootrophic",
"zoot-suiter",
"zooxanthella",
"zooxanthellae",
"zooxanthin",
"zoozoo",
"Zophar",
"zophophori",
"zophori",
"zophorus",
"zopilote",
"Zoque",
"Zoquean",
"Zora",
"Zorah",
"Zorana",
"Zoraptera",
"zorgite",
"zori",
"zoril",
"zorilla",
"zorillas",
"zorille",
"zorilles",
"Zorillinae",
"zorillo",
"zorillos",
"zorils",
"Zorina",
"Zorine",
"zoris",
"Zorn",
"Zoroaster",
"zoroastra",
"Zoroastrian",
"Zoroastrianism",
"zoroastrians",
"Zoroastrism",
"Zorobabel",
"Zorotypus",
"zorrillo",
"zorro",
"Zortman",
"zortzico",
"Zosema",
"Zoser",
"Zosi",
"Zosima",
"Zosimus",
"Zosma",
"zoster",
"Zostera",
"Zosteraceae",
"Zosteria",
"zosteriform",
"Zosteropinae",
"Zosterops",
"zosters",
"Zouave",
"zouaves",
"Zoubek",
"Zoug",
"zounds",
"zowie",
"ZPG",
"ZPRSN",
"Zr",
"Zrich",
"Zrike",
"zs",
"zAs",
"Zsa",
"Zsazsa",
"Z-shaped",
"Zsigmondy",
"Zsolway",
"ZST",
"ZT",
"Ztopek",
"Zubeneschamali",
"Zubird",
"Zubkoff",
"zubr",
"Zuccari",
"zuccarino",
"Zuccaro",
"Zucchero",
"zucchetti",
"zucchetto",
"zucchettos",
"zucchini",
"zucchinis",
"zucco",
"zuchetto",
"Zucker",
"Zuckerman",
"zudda",
"zuffolo",
"zufolo",
"Zug",
"zugtierlast",
"zugtierlaster",
"zugzwang",
"Zui",
"Zuian",
"Zuidholland",
"zuisin",
"Zulch",
"Zuleika",
"Zulema",
"Zulhijjah",
"Zulinde",
"Zulkadah",
"ZuAlkadah",
"Zullinger",
"Zullo",
"Zuloaga",
"Zulu",
"Zuludom",
"Zuluize",
"Zulu-kaffir",
"Zululand",
"Zulus",
"zumatic",
"zumbooruk",
"Zumbrota",
"Zumstein",
"Zumwalt",
"Zungaria",
"Zuni",
"Zunian",
"zunyite",
"zunis",
"zupanate",
"Zupus",
"Zurbar",
"Zurbaran",
"Zurek",
"Zurheide",
"Zurich",
"Zurkow",
"zurlite",
"Zurn",
"Zurvan",
"Zusman",
"Zutugil",
"zuurveldt",
"zuza",
"Zuzana",
"Zu-zu",
"zwanziger",
"Zwart",
"ZWEI",
"Zweig",
"Zwick",
"Zwickau",
"Zwicky",
"Zwieback",
"zwiebacks",
"Zwiebel",
"zwieselite",
"Zwingle",
"Zwingli",
"Zwinglian",
"Zwinglianism",
"Zwinglianist",
"zwitter",
"zwitterion",
"zwitterionic",
"Zwolle",
"Zworykin",
"ZZ",
"zZt",
"ZZZ",
]
payload = ["\xfc","\x48",] #PASTE THE PAYLOAD INSIDE THE BRACKETS 
hex_to_index = [ord(hex) for hex in payload]
result = [dictionary[index] for index in hex_to_index]

print(result)
print("Size of payload is: ", len(result))

