# -*- coding: utf-8 -*-

import random

# Animal data from Wikipedia circa Dec 2014.

animals = [
    'Abditomys',
    'Abeomelomys',
    'Abrawayaomys',
    'Abrocoma',
    'Abrothrix',
    'Acerodon',
    'Acinonyx',
    'Acomys',
    'Aconaemys',
    'Acrobates',
    'Addax',
    'Aegialomys',
    'Aepeomys',
    'Aepyceros',
    'Aepyprymnus',
    'Aeretes',
    'Aeromys',
    'Aethalops',
    'Aethomys',
    'Ailuropoda',
    'Ailurops',
    'Ailurus',
    'Akodon',
    'Alcelaphus',
    'Alces',
    'Alionycteris',
    'Allactaga',
    'Allactodipus',
    'Allenopithecus',
    'Allocebus',
    'Allochrocebus',
    'Allocricetulus',
    'Alouatta',
    'Alticola',
    'Amblonyx',
    'Amblysomus',
    'Ametrida',
    'Ammodillus',
    'Ammodorcas',
    'Ammospermophilus',
    'Ammotragus',
    'Amorphochilus',
    'Amphinectomys',
    'Anathana',
    'Andalgalomys',
    'Andinomys',
    'Anisomys',
    'Anomalurus',
    'Anonymomys',
    'Anotomys',
    'Anoura',
    'Anourosorex',
    'Antechinomys',
    'Antechinus',
    'Anthops',
    'Antidorcas',
    'Antilocapra',
    'Antrozous',
    'Aonyx',
    'Aplodontia',
    'Apodemus',
    'Apomys',
    'Aproteles',
    'Arabitragus',
    'Arborimus',
    'Archboldomys',
    'Arctictis',
    'Arctocebus',
    'Arctocephalus',
    'Arctogalidia',
    'Arctonyx',
    'Ardops',
    'Arielulus',
    'Ariteus',
    'Artibeus',
    'Arvicanthis',
    'Arvicola',
    'Asellia',
    'Aselliscus',
    'Atelerix',
    'Ateles',
    'Atelocynus',
    'Atherurus',
    'Atilax',
    'Atlantoxerus',
    'Auliscomys',
    'Babyrousa',
    'Baiomys',
    'Baiyankamys',
    'Balaena',
    'Balaenoptera',
    'Balantiopteryx',
    'Balionycteris',
    'Bandicota',
    'Barbastella',
    'Bassaricyon',
    'Bassariscus',
    'Bathyergus',
    'Batomys',
    'Bauerus',
    'Bdeogale',
    'Beamys',
    'Beatragus',
    'Belomys',
    'Berardius',
    'Berylmys',
    'Bettongia',
    'Bibimys',
    'Biswamoyopterus',
    'Blanfordimys',
    'Blarina',
    'Blarinella',
    'Blarinomys',
    'Blastocerus',
    'Bos',
    'Boselaphus',
    'Brachiones',
    'Brachylagus',
    'Brachyphylla',
    'Brachytarsomys',
    'Brachyteles',
    'Brachyuromys',
    'Bradypus',
    'Brucepattersonius',
    'Bubalus',
    'Budorcas',
    'Bullimus',
    'Bunolagus',
    'Bunomys',
    'Burramys',
    'Cabassous',
    'Cacajao',
    'Caenolestes',
    'Calcochloris',
    'Callibella',
    'Callicebus',
    'Callimico',
    'Callistomys',
    'Callithrix',
    'Callorhinus',
    'Callosciurus',
    'Calomys',
    'Calomyscus',
    'Caluromys',
    'Caluromysiops',
    'Calyptophractus',
    'Canis',
    'Cannomys',
    'Cansumys',
    'Caperea',
    'Capreolus',
    'Capricornis',
    'Caprolagus',
    'Capromys',
    'Caracal',
    'Cardiocranius',
    'Cardioderma',
    'Carollia',
    'Carpitalpa',
    'Carpomys',
    'Carterodon',
    'Caryomys',
    'Casinycteris',
    'Catagonus',
    'Catopuma',
    'Cavia',
    'Cebuella',
    'Cebus',
    'Centronycteris',
    'Cephalopachus',
    'Cephalophus',
    'Cephalorhynchus',
    'Ceratotherium',
    'Cercartetus',
    'Cercocebus',
    'Cercopithecus',
    'Cerdocyon',
    'Cerradomys',
    'Cervus',
    'Chacodelphys',
    'Chaetocauda',
    'Chaetodipus',
    'Chaetomys',
    'Chaetophractus',
    'Chalinolobus',
    'Cheirogaleus',
    'Cheiromeles',
    'Chelemys',
    'Chibchanomys',
    'Chilomys',
    'Chilonatalus',
    'Chimarrogale',
    'Chinchilla',
    'Chinchillula',
    'Chionomys',
    'Chiroderma',
    'Chiromyscus',
    'Chironax',
    'Chironectes',
    'Chiropodomys',
    'Chiropotes',
    'Chiruromys',
    'Chlamyphorus',
    'Chlorocebus',
    'Chlorotalpa',
    'Chodsigoa',
    'Choeroniscus',
    'Choeronycteris',
    'Choeropsis',
    'Choloepus',
    'Chrotogale',
    'Chrotomys',
    'Chrotopterus',
    'Chrysochloris',
    'Chrysocyon',
    'Chrysospalax',
    'Cistugo',
    'Civettictis',
    'Cloeotis',
    'Clyomys',
    'Coccymys',
    'Coelops',
    'Coendou',
    'Coleura',
    'Colobus',
    'Colomys',
    'Condylura',
    'Conepatus',
    'Congosorex',
    'Conilurus',
    'Connochaetes',
    'Cormura',
    'Corynorhinus',
    'Craseonycteris',
    'Crateromys',
    'Cratogeomys',
    'Cremnomys',
    'Cricetomys',
    'Cricetulus',
    'Cricetus',
    'Crocidura',
    'Crocuta',
    'Crossarchus',
    'Crossomys',
    'Crunomys',
    'Cryptochloris',
    'Cryptomys',
    'Cryptonanus',
    'Cryptoprocta',
    'Cryptotis',
    'Ctenodactylus',
    'Ctenomys',
    'Cuon',
    'Cuscomys',
    'Cynictis',
    'Cynocephalus',
    'Cynogale',
    'Cynomops',
    'Cynomys',
    'Cynopterus',
    'Cyttarops',
    'Dacnomys',
    'Dactylomys',
    'Dactylopsila',
    'Damaliscus',
    'Dasycercus',
    'Dasykaluta',
    'Dasymys',
    'Dasyprocta',
    'Dasypus',
    'Dasyuroides',
    'Dasyurus',
    'Daubentonia',
    'Delanymys',
    'Delomys',
    'Delphinapterus',
    'Delphinus',
    'Deltamys',
    'Dendrogale',
    'Dendrohyrax',
    'Dendrolagus',
    'Dendromus',
    'Dendroprionomys',
    'Deomys',
    'Dephomys',
    'Desmalopex',
    'Desmana',
    'Desmodilliscus',
    'Desmodillus',
    'Desmodus',
    'Desmomys',
    'Diaemus',
    'Dicerorhinus',
    'Diceros',
    'Diclidurus',
    'Dicrostonyx',
    'Didelphis',
    'Dinaromys',
    'Dinomys',
    'Diomys',
    'Diphylla',
    'Diplogale',
    'Diplomesodon',
    'Diplomys',
    'Diplothrix',
    'Dipodillus',
    'Dipodomys',
    'Dipus',
    'Distoechurus',
    'Dobsonia',
    'Dolichotis',
    'Dologale',
    'Dorcatragus',
    'Dorcopsis',
    'Dorcopsulus',
    'Dremomys',
    'Dromiciops',
    'Drymoreomys',
    'Dryomys',
    'Dugong',
    'Dyacopterus',
    'Dymecodon',
    'Echimys',
    'Echinoprocta',
    'Echinosorex',
    'Echiothrix',
    'Echymipera',
    'Ectophylla',
    'Eidolon',
    'Elaphodus',
    'Elaphurus',
    'Elephantulus',
    'Elephas',
    'Eligmodontia',
    'Eliomys',
    'Eliurus',
    'Ellobius',
    'Emballonura',
    'Enchisthenes',
    'Eoglaucomys',
    'Eolagurus',
    'Eonycteris',
    'Eospalax',
    'Eothenomys',
    'Eozapus',
    'Episoriculus',
    'Epixerus',
    'Epomophorus',
    'Epomops',
    'Eptesicus',
    'Eremitalpa',
    'Eremodipus',
    'Eremoryzomys',
    'Erethizon',
    'Erignathus',
    'Erinaceus',
    'Eropeplus',
    'Erophylla',
    'Erythrocebus',
    'Eschrichtius',
    'Eubalaena',
    'Euchoreutes',
    'Euderma',
    'Eudiscopus',
    'Eudorcas',
    'Eulemur',
    'Eumetopias',
    'Eumops',
    'Euneomys',
    'Euoticus',
    'Eupetaurus',
    'Euphractus',
    'Eupleres',
    'Euroscaptor',
    'Euryoryzomys',
    'Euryzygomatomys',
    'Eutamias',
    'Exilisciurus',
    'Falsistrellus',
    'Felis',
    'Felovia',
    'Feresa',
    'Feroculus',
    'Fukomys',
    'Funambulus',
    'Funisciurus',
    'Furipterus',
    'Galemys',
    'Galenomys',
    'Galeopterus',
    'Galerella',
    'Galictis',
    'Galidia',
    'Galidictis',
    'Gazella',
    'Genetta',
    'Geocapromys',
    'Geogale',
    'Geomys',
    'Georychus',
    'Geoxus',
    'Gerbilliscus',
    'Gerbillurus',
    'Gerbillus',
    'Giraffa',
    'Glaucomys',
    'Glauconycteris',
    'Glironia',
    'Glirulus',
    'Glischropus',
    'Globicephala',
    'Glossophaga',
    'Glyphonycteris',
    'Glyphotes',
    'Golunda',
    'Gorilla',
    'Gracilinanus',
    'Grammomys',
    'Graomys',
    'Graphiurus',
    'Gulo',
    'Gymnobelideus',
    'Gymnuromys',
    'Habromys',
    'Hadromys',
    'Haeromys',
    'Halichoerus',
    'Handleyomys',
    'Hapalemur',
    'Hapalomys',
    'Haplonycteris',
    'Harpiocephalus',
    'Harpiola',
    'Harpyionycteris',
    'Heimyscus',
    'Helarctos',
    'Heliophobius',
    'Heliosciurus',
    'Helogale',
    'Hemibelideus',
    'Hemicentetes',
    'Hemiechinus',
    'Hemigalus',
    'Hemitragus',
    'Herpestes',
    'Hesperoptenus',
    'Heterocephalus',
    'Heterohyrax',
    'Heteromys',
    'Hippocamelus',
    'Hippopotamus',
    'Hipposideros',
    'Hippotragus',
    'Histiotus',
    'Histriophoca',
    'Hodomys',
    'Holochilus',
    'Homo',
    'Hoolock',
    'Hoplomys',
    'Hybomys',
    'Hydrictis',
    'Hydrochoerus',
    'Hydromys',
    'Hydropotes',
    'Hydrurga',
    'Hyemoschus',
    'Hyladelphys',
    'Hylaeamys',
    'Hylobates',
    'Hylochoerus',
    'Hylomyscus',
    'Hylonycteris',
    'Hylopetes',
    'Hyomys',
    'Hyosciurus',
    'Hyperacrius',
    'Hyperoodon',
    'Hypogeomys',
    'Hypsignathus',
    'Hypsiprymnodon',
    'Hypsugo',
    'Ictonyx',
    'Idionycteris',
    'Idiurus',
    'Indopacetus',
    'Indri',
    'Inia',
    'Iomys',
    'Irenomys',
    'Isoodon',
    'Isothrix',
    'Isthmomys',
    'Juliomys',
    'Juscelinomys',
    'Kadarsanomys',
    'Kannabateomys',
    'Kerivoula',
    'Kerodon',
    'Kogia',
    'Komodomys',
    'Kunsia',
    'La Plata Dolphin',
    'Laephotis',
    'Lagenodelphis',
    'Lagenorhynchus',
    'Lagidium',
    'Lagorchestes',
    'Lagostomus',
    'Lagostrophus',
    'Lagothrix',
    'Lamottemys',
    'Lampronycteris',
    'Laonastes',
    'Lariscus',
    'Lasionycteris',
    'Lasiopodomys',
    'Lasiorhinus',
    'Lasiurus',
    'Latidens',
    'Lavia',
    'Leggadina',
    'Leimacomys',
    'Leimacomys',
    'Lemmiscus',
    'Lemmus',
    'Lemniscomys',
    'Lemur',
    'Lenomys',
    'Lenothrix',
    'Lenoxus',
    'Leontopithecus',
    'Leopardus',
    'Leopoldamys',
    'Lepilemur',
    'Leporillus',
    'Leptailurus',
    'Leptomys',
    'Leptonychotes',
    'Leptonycteris',
    'Lepus',
    'Lestodelphys',
    'Lestoros',
    'Liberiictis',
    'Lichonycteris',
    'Limnogale',
    'Limnomys',
    'Liomys',
    'Lionycteris',
    'Lipotes',
    'Lissodelphis',
    'Lissonycteris',
    'Litocranius',
    'Lobodon',
    'Lonchophylla',
    'Lonchorhina',
    'Lonchothrix',
    'Lontra',
    'Lophiomys',
    'Lophocebus',
    'Lophostoma',
    'Lophuromys',
    'Lorentzimys',
    'Loxodonta',
    'Loxodontomys',
    'Lundomys',
    'Lutra',
    'Lutreolina',
    'Lutrogale',
    'Lycalopex',
    'Lyncodon',
    'Lynx',
    'Macroderma',
    'Macrogalidia',
    'Macroglossus',
    'Macrophyllum',
    'Macropus',
    'Macroscelides',
    'Macrotarsomys',
    'Macrotis',
    'Macrotus',
    'Macruromys',
    'Madoqua',
    'Madromys',
    'Makalata',
    'Malacomys',
    'Mallomys',
    'Mammelomys',
    'Mandrillus',
    'Manis',
    'Margaretamys',
    'Marmosa',
    'Marmosops',
    'Marmota',
    'Martes',
    'Massoutiera',
    'Mastacomys',
    'Mastomys',
    'Maxomys',
    'Megadendromus',
    'Megaderma',
    'Megadontomys',
    'Megaerops',
    'Megaloglossus',
    'Megaptera',
    'Megasorex',
    'Melanomys',
    'Melasmothrix',
    'Mellivora',
    'Melogale',
    'Melomys',
    'Melonycteris',
    'Melursus',
    'Menetes',
    'Mesechinus',
    'Mesembriomys',
    'Mesocapromys',
    'Mesocricetus',
    'Mesomys',
    'Mesophylla',
    'Mesoplodon',
    'Metachirus',
    'Micaelamys',
    'Microakodontomys',
    'Microcavia',
    'Microcebus',
    'Microdillus',
    'Microdipodops',
    'Microgale',
    'Microhydromys',
    'Micromurexia',
    'Micromys',
    'Micronycteris',
    'Microperoryctes',
    'Micropotamogale',
    'Micropteropus',
    'Microryzomys',
    'Microsciurus',
    'Microtus',
    'Millardia',
    'Mimetillus',
    'Mimon',
    'Mindomys',
    'Miniopterus',
    'Miopithecus',
    'Mirimiri',
    'Mirounga',
    'Mirzamys',
    'Mogera',
    'Molossops',
    'Monachus',
    'Monodelphis',
    'Monodon',
    'Monophyllus',
    'Monticolomys',
    'Mops',
    'Mormoops',
    'Mormopterus',
    'Moschiola',
    'Moschus',
    'Mosia',
    'Mungos',
    'Mungotictis',
    'Muntiacus',
    'Murexechinus',
    'Murexia',
    'Muriculus',
    'Murina',
    'Muscardinus',
    'Musonycteris',
    'Musseromys',
    'Mustela',
    'Mydaus',
    'Mylomys',
    'Myocastor',
    'Myodes',
    'Myoictis',
    'Myomimus',
    'Myomyscus',
    'Myonycteris',
    'Myoprocta',
    'Myopterus',
    'Myopus',
    'Myosciurus',
    'Myosorex',
    'Myospalax',
    'Myotis',
    'Myotomys',
    'Myrmecobius',
    'Myrmecophaga',
    'Mysateles',
    'Mystacina',
    'Mystromys',
    'Myzopoda',
    'Naemorhedus',
    'Nandinia',
    'Nanger',
    'Nannosciurus',
    'Nanonycteris',
    'Napaeozapus',
    'Nasua',
    'Nasuella',
    'Natalus',
    'Neacomys',
    'Neamblysomus',
    'Necromys',
    'Nectogale',
    'Nectomys',
    'Neodon',
    'Neofelis',
    'Neofiber',
    'Neohylomys',
    'Neomys',
    'Neonycteris',
    'Neophascogale',
    'Neophoca',
    'Neophocaena',
    'Neopteryx',
    'Neoromicia',
    'Neotamias',
    'Neotetracus',
    'Neotoma',
    'Neotomodon',
    'Neotomys',
    'Neotragus',
    'Neovison',
    'Nephelomys',
    'Nesokia',
    'Nesolagus',
    'Nesomys',
    'Nesoromys',
    'Nesoryzomys',
    'Neurotrichus',
    'Neusticomys',
    'Nilgiritragus',
    'Nilopegamys',
    'Ningaui',
    'Niumbaha',
    'Niviventer',
    'Noctilio',
    'Nomascus',
    'Notiomys',
    'Notiosorex',
    'Notocitellus',
    'Notomys',
    'Notopteris',
    'Notoryctes',
    'Nyala',
    'Nyctalus',
    'Nyctereutes',
    'Nycteris',
    'Nycticebus',
    'Nycticeinops',
    'Nycticeius',
    'Nyctiellus',
    'Nyctinomops',
    'Nyctomys',
    'Nyctophilus',
    'Ochotona',
    'Ochrotomys',
    'Octodon',
    'Octodontomys',
    'Octomys',
    'Odobenus',
    'Odocoileus',
    'Oecomys',
    'Oenomys',
    'Okapia',
    'Olallamys',
    'Oligoryzomys',
    'Ommatophoca',
    'Ondatra',
    'Onychogalea',
    'Onychomys',
    'Orcaella',
    'Orcinus',
    'Oreamnos',
    'Oreonax',
    'Oreoryzomys',
    'Oreotragus',
    'Ornithorhynchus',
    'Orthogeomys',
    'Oryctolagus',
    'Oryx',
    'Oryzomys',
    'Oryzorictes',
    'Osgoodomys',
    'Otaria',
    'Otocyon',
    'Otolemur',
    'Otomops',
    'Otomys',
    'Otonycteris',
    'Otonyctomys',
    'Otopteropus',
    'Otospermophilus',
    'Ototylomys',
    'Ourebia',
    'Ovibos',
    'Ovis',
    'Oxymycterus',
    'Ozotoceros',
    'Pachyuromys',
    'Pagophilus',
    'Paguma',
    'Palawanomys',
    'Panthera',
    'Pantholops',
    'Papagomys',
    'Papio',
    'Pappogeomys',
    'Paracoelops',
    'Paracrocidura',
    'Paracynictis',
    'Paradipus',
    'Paradoxurus',
    'Paraechinus',
    'Parahydromys',
    'Paraleptomys',
    'Paralomys',
    'Paramelomys',
    'Paramurexia',
    'Parantechinus',
    'Paranyctimene',
    'Parascalops',
    'Parascaptor',
    'Parastrellus',
    'Paratriaenops',
    'Paraxerus',
    'Pardofelis',
    'Parotomys',
    'Paruromys',
    'Pattonomys',
    'Paucidentomys',
    'Paulamys',
    'Pearsonomys',
    'Pecari',
    'Pectinator',
    'Pedetes',
    'Pelomys',
    'Pentalagus',
    'Penthetor',
    'Peponocephala',
    'Perameles',
    'Perimyotis',
    'Perodicticus',
    'Perognathus',
    'Peromyscus',
    'Peropteryx',
    'Peroryctes',
    'Petaurillus',
    'Petaurista',
    'Petauroides',
    'Petaurus',
    'Petinomys',
    'Petrodromus',
    'Petrogale',
    'Petromus',
    'Petromyscus',
    'Petropseudes',
    'Phacochoerus',
    'Phaenomys',
    'Phaiomys',
    'Phalanger',
    'Phaner',
    'Pharotis',
    'Phascogale',
    'Phascolarctos',
    'Phascolosorex',
    'Phascomurexia',
    'Phenacomys',
    'Philantomba',
    'Phloeomys',
    'Phoca',
    'Phocarctos',
    'Phocoena',
    'Phocoenoides',
    'Phodopus',
    'Phoniscus',
    'Phylloderma',
    'Phyllomys',
    'Phyllonycteris',
    'Phyllops',
    'Phyllostomus',
    'Phyllotis',
    'Physeter',
    'Piliocolobus',
    'Pipanacoctomys',
    'Pipistrellus',
    'Pithecheir',
    'Pithecheirops',
    'Pithecia',
    'Plagiodontia',
    'Planigale',
    'Platacanthomys',
    'Platalina',
    'Platanista',
    'Platymops',
    'Platyrrhinus',
    'Plecotus',
    'Plerotes',
    'Podogymnura',
    'Podomys',
    'Podoxymys',
    'Poecilogale',
    'Poelagus',
    'Poephagus',
    'Pogonomelomys',
    'Pogonomys',
    'Poliocitellus',
    'Porcula',
    'Potamochoerus',
    'Potamogale',
    'Potorous',
    'Potos',
    'Praomys',
    'Presbytis',
    'Priodontes',
    'Prionailurus',
    'Prionodon',
    'Prionomys',
    'Procapra',
    'Procavia',
    'Procolobus',
    'Proechimys',
    'Proedromys',
    'Profelis',
    'Prolemur',
    'Prometheomys',
    'Promops',
    'Pronolagus',
    'Propithecus',
    'Prosciurillus',
    'Proteles',
    'Protochromys',
    'Protoxerus',
    'Psammomys',
    'Pseudantechinus',
    'Pseudocheirus',
    'Pseudochirops',
    'Pseudochirulus',
    'Pseudohydromys',
    'Pseudois',
    'Pseudomys',
    'Pseudopotto',
    'Pseudorca',
    'Pseudoryx',
    'Pseudoryzomys',
    'Ptenochirus',
    'Pteralopex',
    'Pteromys',
    'Pteromyscus',
    'Pteronotus',
    'Pteronura',
    'Pteropus',
    'Ptilocercus',
    'Punomys',
    'Pusa',
    'Pygathrix',
    'Pygeretmus',
    'Pygoderma',
    'Raphicerus',
    'Rattus',
    'Ratufa',
    'Redunca',
    'Reithrodon',
    'Reithrodontomys',
    'Rhabdomys',
    'Rhagomys',
    'Rheithrosciurus',
    'Rheomys',
    'Rhinoceros',
    'Rhinolophus',
    'Rhinonicteris',
    'Rhinophylla',
    'Rhinopithecus',
    'Rhinopoma',
    'Rhinosciurus',
    'Rhipidomys',
    'Rhizomys',
    'Rhogeessa',
    'Rhombomys',
    'Rhynchocyon',
    'Rhynchogale',
    'Rhyncholestes',
    'Rhynchomeles',
    'Rhynchomys',
    'Rhynchonycteris',
    'Romerolagus',
    'Rousettus',
    'Rubrisciurus',
    'Rungwecebus',
    'Rupicapra',
    'Ruwenzorisorex',
    'Saccolaimus',
    'Saccopteryx',
    'Saccostomus',
    'Saguinus',
    'Saiga',
    'Saimiri',
    'Salanoia',
    'Salinoctomys',
    'Salinomys',
    'Salpingotulus',
    'Salpingotus',
    'Sarcophilus',
    'Sauromys',
    'Saxatilomys',
    'Scalopus',
    'Scapanulus',
    'Scapanus',
    'Scapteromys',
    'Scaptochirus',
    'Scaptonyx',
    'Sciurillus',
    'Sciurotamias',
    'Sciurus',
    'Scleronycteris',
    'Scolomys',
    'Scoteanax',
    'Scotinomys',
    'Scotoecus',
    'Scotomanes',
    'Scotonycteris',
    'Scotophilus',
    'Scotorepens',
    'Scotozous',
    'Scuirocheirus',
    'Scutisorex',
    'Sekeetamys',
    'Selevinia',
    'Semnopithecus',
    'Setifer',
    'Setonix',
    'Sicista',
    'Sigmodon',
    'Sigmodontomys',
    'Simias',
    'Sminthopsis',
    'Solenodon',
    'Solisorex',
    'Solomys',
    'Sommeromys',
    'Sooretamys',
    'Sorex',
    'Soriculus',
    'Sotalia',
    'Spalacopus',
    'Spalax',
    'Speothos',
    'Spermophilopsis',
    'Spermophilus',
    'Sphaerias',
    'Sphaeronycteris',
    'Sphiggurus',
    'Spilocuscus',
    'Spilogale',
    'Srilankamys',
    'Steatomys',
    'Stenella',
    'Stenocephalemys',
    'Stenoderma',
    'Stochomys',
    'Strigocuscus',
    'Sturnira',
    'Styloctenium',
    'Stylodipus',
    'Suncus',
    'Sundamys',
    'Sundasciurus',
    'Surdisorex',
    'Syconycteris',
    'Sylvicapra',
    'Sylvilagus',
    'Sylvisorex',
    'Symphalangus',
    'Synaptomys',
    'Syncerus',
    'Syntheosciurus',
    'Tachyglossus',
    'Tachyoryctes',
    'Tadarida',
    'Taeromys',
    'Tamias',
    'Tamiasciurus',
    'Tamiops',
    'Tapecomys',
    'Taphozous',
    'Tapirus',
    'Tarsipes',
    'Tarsius',
    'Tarsomys',
    'Tasmacetus',
    'Tateomys',
    'Tatera',
    'Taterillus',
    'Taurotragus',
    'Taxidea',
    'Tayassu',
    'Tetracerus',
    'Thallomys',
    'Thalpomys',
    'Thamnomys',
    'Thaptomys',
    'Theropithecus',
    'Thomasomys',
    'Thomomys',
    'Thoopterus',
    'Thrichomys',
    'Thryonomys',
    'Thylamys',
    'Thylogale',
    'Thyroptera',
    'Tlacuatzin',
    'Tokudaia',
    'Tolypeutes',
    'Tomopeas',
    'Tonatia',
    'Tonkinomys',
    'Toromys',
    'Trachops',
    'Trachypithecus',
    'Tragelaphus',
    'Tragulus',
    'Transandinomys',
    'Tremarctos',
    'Triaenops',
    'Trichechus',
    'Trichosurus',
    'Trichys',
    'Trinomys',
    'Trinycteris',
    'Trogopterus',
    'Tryphomys',
    'Tscherskia',
    'Tursiops',
    'Tylomys',
    'Tylonycteris',
    'Tympanoctomys',
    'Typhlomys',
    'Uranomys',
    'Urocyon',
    'Uroderma',
    'Urogale',
    'Uromys',
    'Uropsilus',
    'Urotrichus',
    'Vampyressa',
    'Vampyrodes',
    'Vampyrum',
    'Vandeleuria',
    'Varecia',
    'Vernaya',
    'Vespadelus',
    'Vespertilio',
    'Vicugna',
    'Viverra',
    'Viverricula',
    'Voalavo',
    'Volemys',
    'Vombatus',
    'Vormela',
    'Vulpes',
    'Waiomys',
    'Wallabia',
    'Wiedomys',
    'Wilfredomys',
    'Wrinkle-faced Bat',
    'Wyulda',
    'Xenogale',
    'Xenomys',
    'Xenuromys',
    'Xeromys',
    'Xeronycteris',
    'Xerospermophilus',
    'Xerus',
    'Zaedyus',
    'Zaglossus',
    'Zalophus',
    'Zapus',
    'Zelotomys',
    'Ziphius',
    'Zygodontomys',
    'Zygogeomys',
    'Zyzomys',
]

first_names = [
    'Abigail',
    'Alexander',
    'Alexis',
    'Amanda',
    'Amy',
    'Andrew',
    'Angela',
    'Ashley',
    'Ava',
    'Barbara',
    'Betty',
    'Brittany',
    'Carol',
    'Charles',
    'Christopher',
    'Daniel',
    'David',
    'Deborah',
    'Debra',
    'Donna',
    'Dorothy',
    'Emily',
    'Emma',
    'Ethan',
    'Hannah',
    'Heather',
    'Helen',
    'Isabella',
    'Jacob',
    'James',
    'Jason',
    'Jayden',
    'Jennifer',
    'Jessica',
    'Joan',
    'John',
    'Joseph',
    'Joshua',
    'Judith',
    'Karen',
    'Kimberly',
    'Liam',
    'Linda',
    'Lisa',
    'Madison',
    'Margaret',
    'Mary',
    'Mason',
    'Matthew',
    'Melissa',
    'Michael',
    'Michelle',
    'Nicholas',
    'Noah',
    'Olivia',
    'Patricia',
    'Richard',
    'Robert',
    'Ruth',
    'Samantha',
    'Sandra',
    'Sarah',
    'Shirley',
    'Sophia',
    'Susan',
    'Tyler',
    'William',
]

last_names = [
    'Abbott',
    'Acevedo',
    'Acosta',
    'Adams',
    'Adkins',
    'Aguilar',
    'Aguirre',
    'Albert',
    'Alexander',
    'Alford',
    'Allen',
    'Allison',
    'Alston',
    'Alvarado',
    'Alvarez',
    'Anderson',
    'Andrews',
    'Anthony',
    'Armstrong',
    'Arnold',
    'Ashley',
    'Atkins',
    'Atkinson',
    'Austin',
    'Avery',
    'Avila',
    'Ayala',
    'Ayers',
    'Bailey',
    'Baird',
    'Baker',
    'Baldwin',
    'Ball',
    'Ballard',
    'Banks',
    'Barber',
    'Barker',
    'Barlow',
    'Barnes',
    'Barnett',
    'Barr',
    'Barrera',
    'Barrett',
    'Barron',
    'Barry',
    'Bartlett',
    'Barton',
    'Bass',
    'Bates',
    'Battle',
    'Bauer',
    'Baxter',
    'Beach',
    'Bean',
    'Beard',
    'Beasley',
    'Beck',
    'Becker',
    'Bell',
    'Bender',
    'Benjamin',
    'Bennett',
    'Benson',
    'Bentley',
    'Benton',
    'Berg',
    'Berger',
    'Bernard',
    'Berry',
    'Best',
    'Bird',
    'Bishop',
    'Black',
    'Blackburn',
    'Blackwell',
    'Blair',
    'Blake',
    'Blanchard',
    'Blankenship',
    'Blevins',
    'Bolton',
    'Bond',
    'Bonner',
    'Booker',
    'Boone',
    'Booth',
    'Bowen',
    'Bowers',
    'Bowman',
    'Boyd',
    'Boyer',
    'Boyle',
    'Bradford',
    'Bradley',
    'Bradshaw',
    'Brady',
    'Branch',
    'Bray',
    'Brennan',
    'Brewer',
    'Bridges',
    'Briggs',
    'Bright',
    'Britt',
    'Brock',
    'Brooks',
    'Brown',
    'Browning',
    'Bruce',
    'Bryan',
    'Bryant',
    'Buchanan',
    'Buck',
    'Buckley',
    'Buckner',
    'Bullock',
    'Burch',
    'Burgess',
    'Burke',
    'Burks',
    'Burnett',
    'Burns',
    'Burris',
    'Burt',
    'Burton',
    'Bush',
    'Butler',
    'Byers',
    'Byrd',
    'Cabrera',
    'Cain',
    'Calderon',
    'Caldwell',
    'Calhoun',
    'Callahan',
    'Camacho',
    'Cameron',
    'Campbell',
    'Campos',
    'Cannon',
    'Cantrell',
    'Cantu',
    'Cardenas',
    'Carey',
    'Carlson',
    'Carney',
    'Carpenter',
    'Carr',
    'Carrillo',
    'Carroll',
    'Carson',
    'Carter',
    'Carver',
    'Case',
    'Casey',
    'Cash',
    'Castaneda',
    'Castillo',
    'Castro',
    'Cervantes',
    'Chambers',
    'Chan',
    'Chandler',
    'Chaney',
    'Chang',
    'Chapman',
    'Charles',
    'Chase',
    'Chavez',
    'Chen',
    'Cherry',
    'Christensen',
    'Christian',
    'Church',
    'Clark',
    'Clarke',
    'Clay',
    'Clayton',
    'Clements',
    'Clemons',
    'Cleveland',
    'Cline',
    'Cobb',
    'Cochran',
    'Coffey',
    'Cohen',
    'Cole',
    'Coleman',
    'Collier',
    'Collins',
    'Colon',
    'Combs',
    'Compton',
    'Conley',
    'Conner',
    'Conrad',
    'Contreras',
    'Conway',
    'Cook',
    'Cooke',
    'Cooley',
    'Cooper',
    'Copeland',
    'Cortez',
    'Cote',
    'Cotton',
    'Cox',
    'Craft',
    'Craig',
    'Crane',
    'Crawford',
    'Crosby',
    'Cross',
    'Cruz',
    'Cummings',
    'Cunningham',
    'Curry',
    'Curtis',
    'Dale',
    'Dalton',
    'Daniel',
    'Daniels',
    'Daugherty',
    'Davenport',
    'David',
    'Davidson',
    'Davis',
    'Dawson',
    'Day',
    'Dean',
    'Decker',
    'Dejesus',
    'Delacruz',
    'Delaney',
    'Deleon',
    'Delgado',
    'Dennis',
    'Diaz',
    'Dickerson',
    'Dickson',
    'Dillard',
    'Dillon',
    'Dixon',
    'Dodson',
    'Dominguez',
    'Donaldson',
    'Donovan',
    'Dorsey',
    'Dotson',
    'Douglas',
    'Downs',
    'Doyle',
    'Drake',
    'Dudley',
    'Duffy',
    'Duke',
    'Duncan',
    'Dunlap',
    'Dunn',
    'Duran',
    'Durham',
    'Dyer',
    'Eaton',
    'Edwards',
    'Elliott',
    'Ellis',
    'Ellison',
    'Emerson',
    'England',
    'English',
    'Erickson',
    'Espinoza',
    'Estes',
    'Estrada',
    'Evans',
    'Everett',
    'Ewing',
    'Farley',
    'Farmer',
    'Farrell',
    'Faulkner',
    'Ferguson',
    'Fernandez',
    'Ferrell',
    'Fields',
    'Figueroa',
    'Finch',
    'Finley',
    'Fischer',
    'Fisher',
    'Fitzgerald',
    'Fitzpatrick',
    'Fleming',
    'Fletcher',
    'Flores',
    'Flowers',
    'Floyd',
    'Flynn',
    'Foley',
    'Forbes',
    'Ford',
    'Foreman',
    'Foster',
    'Fowler',
    'Fox',
    'Francis',
    'Franco',
    'Frank',
    'Franklin',
    'Franks',
    'Frazier',
    'Frederick',
    'Freeman',
    'French',
    'Frost',
    'Fry',
    'Frye',
    'Fuentes',
    'Fuller',
    'Fulton',
    'Gaines',
    'Gallagher',
    'Gallegos',
    'Galloway',
    'Gamble',
    'Garcia',
    'Gardner',
    'Garner',
    'Garrett',
    'Garrison',
    'Garza',
    'Gates',
    'Gay',
    'Gentry',
    'George',
    'Gibbs',
    'Gibson',
    'Gilbert',
    'Giles',
    'Gill',
    'Gillespie',
    'Gilliam',
    'Gilmore',
    'Glass',
    'Glenn',
    'Glover',
    'Goff',
    'Golden',
    'Gomez',
    'Gonzales',
    'Gonzalez',
    'Good',
    'Goodman',
    'Goodwin',
    'Gordon',
    'Gould',
    'Graham',
    'Grant',
    'Graves',
    'Gray',
    'Green',
    'Greene',
    'Greer',
    'Gregory',
    'Griffin',
    'Griffith',
    'Grimes',
    'Gross',
    'Guerra',
    'Guerrero',
    'Guthrie',
    'Gutierrez',
    'Guy',
    'Guzman',
    'Hahn',
    'Hale',
    'Haley',
    'Hall',
    'Hamilton',
    'Hammond',
    'Hampton',
    'Hancock',
    'Haney',
    'Hansen',
    'Hanson',
    'Hardin',
    'Harding',
    'Hardy',
    'Harmon',
    'Harper',
    'Harrell',
    'Harrington',
    'Harris',
    'Harrison',
    'Hart',
    'Hartman',
    'Harvey',
    'Hatfield',
    'Hawkins',
    'Hayden',
    'Hayes',
    'Haynes',
    'Hays',
    'Head',
    'Heath',
    'Hebert',
    'Henderson',
    'Hendricks',
    'Hendrix',
    'Henry',
    'Hensley',
    'Henson',
    'Herman',
    'Hernandez',
    'Herrera',
    'Herring',
    'Hess',
    'Hester',
    'Hewitt',
    'Hickman',
    'Hicks',
    'Higgins',
    'Hill',
    'Hines',
    'Hinton',
    'Hobbs',
    'Hodge',
    'Hodges',
    'Hoffman',
    'Hogan',
    'Holcomb',
    'Holden',
    'Holder',
    'Holland',
    'Holloway',
    'Holman',
    'Holmes',
    'Holt',
    'Hood',
    'Hooper',
    'Hoover',
    'Hopkins',
    'Hopper',
    'Horn',
    'Horne',
    'Horton',
    'House',
    'Houston',
    'Howard',
    'Howe',
    'Howell',
    'Hubbard',
    'Huber',
    'Hudson',
    'Huff',
    'Huffman',
    'Hughes',
    'Hull',
    'Humphrey',
    'Hunt',
    'Hunter',
    'Hurley',
    'Hurst',
    'Hutchinson',
    'Hyde',
    'Ingram',
    'Irwin',
    'Jackson',
    'Jacobs',
    'Jacobson',
    'James',
    'Jarvis',
    'Jefferson',
    'Jenkins',
    'Jennings',
    'Jensen',
    'Jimenez',
    'Johns',
    'Johnson',
    'Johnston',
    'Jones',
    'Jordan',
    'Joseph',
    'Joyce',
    'Joyner',
    'Juarez',
    'Justice',
    'Kane',
    'Kaufman',
    'Keith',
    'Keller',
    'Kelley',
    'Kelly',
    'Kemp',
    'Kennedy',
    'Kent',
    'Kerr',
    'Key',
    'Kidd',
    'Kim',
    'King',
    'Kinney',
    'Kirby',
    'Kirk',
    'Kirkland',
    'Klein',
    'Kline',
    'Knapp',
    'Knight',
    'Knowles',
    'Knox',
    'Koch',
    'Kramer',
    'Lamb',
    'Lambert',
    'Lancaster',
    'Landry',
    'Lane',
    'Lang',
    'Langley',
    'Lara',
    'Larsen',
    'Larson',
    'Lawrence',
    'Lawson',
    'Le',
    'Leach',
    'Leblanc',
    'Lee',
    'Leon',
    'Leonard',
    'Lester',
    'Levine',
    'Levy',
    'Lewis',
    'Lindsay',
    'Lindsey',
    'Little',
    'Livingston',
    'Lloyd',
    'Logan',
    'Long',
    'Lopez',
    'Lott',
    'Love',
    'Lowe',
    'Lowery',
    'Lucas',
    'Luna',
    'Lynch',
    'Lynn',
    'Lyons',
    'Macdonald',
    'Macias',
    'Mack',
    'Madden',
    'Maddox',
    'Maldonado',
    'Malone',
    'Mann',
    'Manning',
    'Marks',
    'Marquez',
    'Marsh',
    'Marshall',
    'Martin',
    'Martinez',
    'Mason',
    'Massey',
    'Mathews',
    'Mathis',
    'Matthews',
    'Maxwell',
    'May',
    'Mayer',
    'Maynard',
    'Mayo',
    'Mays',
    'Mcbride',
    'Mccall',
    'Mccarthy',
    'Mccarty',
    'Mcclain',
    'Mcclure',
    'Mcconnell',
    'Mccormick',
    'Mccoy',
    'Mccray',
    'Mccullough',
    'Mcdaniel',
    'Mcdonald',
    'Mcdowell',
    'Mcfadden',
    'Mcfarland',
    'Mcgee',
    'Mcgowan',
    'Mcguire',
    'Mcintosh',
    'Mcintyre',
    'Mckay',
    'Mckee',
    'Mckenzie',
    'Mckinney',
    'Mcknight',
    'Mclaughlin',
    'Mclean',
    'Mcleod',
    'Mcmahon',
    'Mcmillan',
    'Mcneil',
    'Mcpherson',
    'Meadows',
    'Medina',
    'Mejia',
    'Melendez',
    'Melton',
    'Mendez',
    'Mendoza',
    'Mercado',
    'Mercer',
    'Merrill',
    'Merritt',
    'Meyer',
    'Meyers',
    'Michael',
    'Middleton',
    'Miles',
    'Miller',
    'Mills',
    'Miranda',
    'Mitchell',
    'Molina',
    'Monroe',
    'Montgomery',
    'Montoya',
    'Moody',
    'Moon',
    'Mooney',
    'Moore',
    'Morales',
    'Moran',
    'Moreno',
    'Morgan',
    'Morin',
    'Morris',
    'Morrison',
    'Morrow',
    'Morse',
    'Morton',
    'Moses',
    'Mosley',
    'Moss',
    'Mueller',
    'Mullen',
    'Mullins',
    'Munoz',
    'Murphy',
    'Murray',
    'Myers',
    'Nash',
    'Navarro',
    'Neal',
    'Nelson',
    'Newman',
    'Newton',
    'Nguyen',
    'Nichols',
    'Nicholson',
    'Nielsen',
    'Nieves',
    'Nixon',
    'Noble',
    'Noel',
    'Nolan',
    'Norman',
    'Norris',
    'Norton',
    'Nunez',
    'Obrien',
    'Ochoa',
    'Oconnor',
    'Odom',
    'Odonnell',
    'Oliver',
    'Olsen',
    'Olson',
    'Oneal',
    'Oneil',
    'Oneill',
    'Orr',
    'Ortega',
    'Ortiz',
    'Osborn',
    'Osborne',
    'Owen',
    'Owens',
    'Pace',
    'Pacheco',
    'Padilla',
    'Page',
    'Palmer',
    'Park',
    'Parker',
    'Parks',
    'Parrish',
    'Parsons',
    'Pate',
    'Patel',
    'Patrick',
    'Patterson',
    'Patton',
    'Paul',
    'Payne',
    'Pearson',
    'Peck',
    'Pena',
    'Pennington',
    'Perez',
    'Perkins',
    'Perry',
    'Peters',
    'Petersen',
    'Peterson',
    'Petty',
    'Phelps',
    'Phillips',
    'Pickett',
    'Pierce',
    'Pittman',
    'Pitts',
    'Pollard',
    'Poole',
    'Pope',
    'Porter',
    'Potter',
    'Potts',
    'Powell',
    'Powers',
    'Pratt',
    'Preston',
    'Price',
    'Prince',
    'Pruitt',
    'Puckett',
    'Pugh',
    'Quinn',
    'Ramirez',
    'Ramos',
    'Ramsey',
    'Randall',
    'Randolph',
    'Rasmussen',
    'Ratliff',
    'Ray',
    'Raymond',
    'Reed',
    'Reese',
    'Reeves',
    'Reid',
    'Reilly',
    'Reyes',
    'Reynolds',
    'Rhodes',
    'Rice',
    'Rich',
    'Richard',
    'Richards',
    'Richardson',
    'Richmond',
    'Riddle',
    'Riggs',
    'Riley',
    'Rios',
    'Rivas',
    'Rivera',
    'Rivers',
    'Roach',
    'Robbins',
    'Roberson',
    'Roberts',
    'Robertson',
    'Robinson',
    'Robles',
    'Rocha',
    'Rodgers',
    'Rodriguez',
    'Rodriquez',
    'Rogers',
    'Rojas',
    'Rollins',
    'Roman',
    'Romero',
    'Rosa',
    'Rosales',
    'Rosario',
    'Rose',
    'Ross',
    'Roth',
    'Rowe',
    'Rowland',
    'Roy',
    'Ruiz',
    'Rush',
    'Russell',
    'Russo',
    'Rutledge',
    'Ryan',
    'Salas',
    'Salazar',
    'Salinas',
    'Sampson',
    'Sanchez',
    'Sanders',
    'Sandoval',
    'Sanford',
    'Santana',
    'Santiago',
    'Santos',
    'Sargent',
    'Saunders',
    'Savage',
    'Sawyer',
    'Schmidt',
    'Schneider',
    'Schroeder',
    'Schultz',
    'Schwartz',
    'Scott',
    'Sears',
    'Sellers',
    'Serrano',
    'Sexton',
    'Shaffer',
    'Shannon',
    'Sharp',
    'Sharpe',
    'Shaw',
    'Shelton',
    'Shepard',
    'Shepherd',
    'Sheppard',
    'Sherman',
    'Shields',
    'Short',
    'Silva',
    'Simmons',
    'Simon',
    'Simpson',
    'Sims',
    'Singleton',
    'Skinner',
    'Slater',
    'Sloan',
    'Small',
    'Smith',
    'Snider',
    'Snow',
    'Snyder',
    'Solis',
    'Solomon',
    'Sosa',
    'Soto',
    'Sparks',
    'Spears',
    'Spence',
    'Spencer',
    'Stafford',
    'Stanley',
    'Stanton',
    'Stark',
    'Steele',
    'Stein',
    'Stephens',
    'Stephenson',
    'Stevens',
    'Stevenson',
    'Stewart',
    'Stokes',
    'Stone',
    'Stout',
    'Strickland',
    'Strong',
    'Stuart',
    'Suarez',
    'Sullivan',
    'Summers',
    'Sutton',
    'Swanson',
    'Sweeney',
    'Sweet',
    'Sykes',
    'Talley',
    'Tanner',
    'Tate',
    'Taylor',
    'Terrell',
    'Terry',
    'Thomas',
    'Thompson',
    'Thornton',
    'Tillman',
    'Todd',
    'Torres',
    'Townsend',
    'Tran',
    'Travis',
    'Trevino',
    'Trujillo',
    'Tucker',
    'Turner',
    'Tyler',
    'Tyson',
    'Underwood',
    'Valdez',
    'Valencia',
    'Valentine',
    'Valenzuela',
    'Vance',
    'Vang',
    'Vargas',
    'Vasquez',
    'Vaughan',
    'Vaughn',
    'Vazquez',
    'Vega',
    'Velasquez',
    'Velazquez',
    'Velez',
    'Villarreal',
    'Vincent',
    'Vinson',
    'Wade',
    'Wagner',
    'Walker',
    'Wall',
    'Wallace',
    'Waller',
    'Walls',
    'Walsh',
    'Walter',
    'Walters',
    'Walton',
    'Ward',
    'Ware',
    'Warner',
    'Warren',
    'Washington',
    'Waters',
    'Watkins',
    'Watson',
    'Watts',
    'Weaver',
    'Webb',
    'Weber',
    'Webster',
    'Weeks',
    'Weiss',
    'Welch',
    'Wells',
    'West',
    'Wheeler',
    'Whitaker',
    'White',
    'Whitehead',
    'Whitfield',
    'Whitley',
    'Whitney',
    'Wiggins',
    'Wilcox',
    'Wilder',
    'Wiley',
    'Wilkerson',
    'Wilkins',
    'Wilkinson',
    'William',
    'Williams',
    'Williamson',
    'Willis',
    'Wilson',
    'Winters',
    'Wise',
    'Witt',
    'Wolf',
    'Wolfe',
    'Wong',
    'Wood',
    'Woodard',
    'Woods',
    'Woodward',
    'Wooten',
    'Workman',
    'Wright',
    'Wyatt',
    'Wynn',
    'Yang',
    'Yates',
    'York',
    'Young',
    'Zamora',
    'Zimmerman',
]

chinese_last_names = [
    '李',
    '王',
    '张',
    '刘',
    '陈',
    '杨',
    '赵',
    '黄',
    '周',
    '吴',
    '徐',
    '孙',
    '胡',
    '朱',
    '高',
    '林',
    '何',
    '郭',
    '马',
    '罗',
    '梁',
    '宋',
    '郑',
    '谢',
    '韩',
    '唐',
    '冯',
    '于',
    '董',
    '萧',
    '程',
    '曹',
    '袁',
    '邓',
    '许',
    '傅',
    '沈',
    '曾',
    '彭',
    '吕',
    '苏',
    '卢',
    '蒋',
    '蔡',
    '贾',
    '丁',
    '魏',
    '薛',
    '叶',
    '阎',
    '余',
    '潘',
    '杜',
    '戴',
    '夏',
    '钟',
    '汪',
    '田',
    '任',
    '姜',
    '范',
    '方',
    '石',
    '姚',
    '谭',
    '盛',
    '邹',
    '熊',
    '金',
    '陆',
    '郝',
    '孔',
    '白',
    '崔',
    '康',
    '毛',
    '邱',
    '秦',
    '江',
    '史',
    '顾',
    '侯',
    '邵',
    '孟',
    '龙',
    '万',
    '段',
    '章',
    '钱',
    '汤',
    '尹',
    '黎',
    '易',
    '常',
    '武',
    '乔',
    '贺',
    '赖',
    '龚',
    '文',
]

chinese_first_names = [
    '佩',
    '佳',
    '俊',
    '偉',
    '冠',
    '凱',
    '君',
    '哲',
    '嘉',
    '如',
    '婷',
    '子',
    '宇',
    '安',
    '宏',
    '宜',
    '家',
    '庭',
    '廷',
    '建',
    '彥',
    '志',
    '怡',
    '惠',
    '慧',
    '文',
    '明',
    '智',
    '柏',
    '欣',
    '涵',
    '淑',
    '玉',
    '玲',
    '瑋',
    '瑜',
    '秀',
    '穎',
    '維',
    '美',
    '翔',
    '育',
    '芳',
    '華',
    '萱',
    '豪',
    '軒',
    '銘',
    '雅',
    '雯',
]

def animal():
    return random.choice(animals)

def english_name():
    return "{} {}".format(random.choice(first_names), random.choice(last_names))

def chinese_name():
    return "{} {}".format(random.choice(chinese_first_names), random.choice(chinese_last_names))
