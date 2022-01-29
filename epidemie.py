<<<<<<< Updated upstream
class Epidemiologie():

    id = 0

    Epidemie = [
=======
import json
from datetime import datetime
from queue import Empty

class Epidemiologie():

    data = {}
    
    data['Patient'] = []
    data['Covid'] = [
>>>>>>> Stashed changes
        {
            'nom': 'COVID-19',
            'ro': 3,
            'taux_de_letalite': [0.5,1],
            'agent_pathogenes' : 'SARS-Cov-2',
            'mesures_de_lutte': [
                "se laver régulièrement les mains ou utiliser une solution hydro-alcoolique",
                "tousser ou éternuer dans son coude ou dans un mouchoir",
                "se moucher dans un mouchoir à usage unique puis le jeter",
                "éviter de se toucher le visage",
                "respecter une distance d'au moins deux mètres avec les autres",
                "saluer sans serrer la main et arrêter les embrassades",
                "porter un masque chirurgical ou en tissu de catégorie 1 quand la distance de deux mètres ne peut pas être respectée",
                "limiter au maximum ses contacts sociaux (6 personnes maximum)",
                "aérer les pièces le plus souvent possible, au minimum quelques minutes toutes les heures",
                "utiliser les outils numériques (application Tous anti-Covid)"
            ],
<<<<<<< Updated upstream
            'sympthome': {
=======
            'sympthômes': {
>>>>>>> Stashed changes
                "net" : [
                    "La fièvre",
                    "La toux sèche",
                    "Essoufflements",
                    "Perte de l'odorat, perte du goût",
                    "La fatigue",
                    "Courbatures et douleurs musculaires",
                    "Diarrhées, nausées",
                    "Maux de gorge",
                    "Maux de tête",
                    "Conjonctivite, yeux irrités",
                    "Eruptions cutanées",
                    "Douleurs thoraciques"
                ]
            },
            'moyen_de_propagation': [
                "aérien"
<<<<<<< Updated upstream
            ],
            'soin': {
                'soins symptomatiques' : [
                    "Prendre du paracétamol contre la fièvre et les courbatures",
                    "Se reposer",
                    "Boire beaucoup pour se réhydrater",
                    "Désobstruer le nez avec du sérum physiologique",
                    "Et bien sûr, se confiner et respecter les mesures d’hygiène pour éviter de contaminer l’entourage."
                ]
            }
        },

        {
            'nom': 'EBOLA',
            'ro': 2,
            'taux_de_letalite': 53,56,
            'agent_pathogenes' : 'SARS-Cov-2',
            'mesures_de_lutte': [
=======
            ]
        },

        ]  
    data['Ebola'] = [
       
        {
            'nom': 'EBOLA',
            'ro': 2,
            'taux_de_letalite': 53.56,
            'agent_pathogenes' : 'Ebola',
            'mesures_de_lutte': [
                "Se laver les mains régulièrement à l’eau et au savon",
                "Eviter d'être en contact avec des personnes malades, qui doivent être mis en quarantaine",
                "Il ne faut pas toucher, embrasser ou même laver une personne malade",
                "Les soignants doivent porter blouses, gants, masques et lunettes. Et ne pas réutiliser les seringues",
                "Une attention particulière doit être portée lors des rites funéraires puisque les personnes décédées sont encore porteuses du virus et peuvent être contagieux",
                "Apprendre à ne pas porter sa main à sa bouche ou à ses yeux, portes d’entrées du virus",
                "Porter des gants et vêtements de protection pour manipuler les animaux malades et leur chair",
                "Rester vigilants chez les malades guéris qui peuvent encore transmettre le virus pendant 7 semaines. Ils doivent éviter les relations sexuelles pendant ce temps ou utiliser un préservatif."
            ],
            'sympthome': {
                'net' : [
                    "L’apparition brutale d'une fièvre intense, accompagnée de frissons",
                    "Une diarrhée",
                    "Des vomissements",
                    "Une fatigue extrêmement intense",
                    "Une perte d’appétit importante (anorexie)"
                ],
                'facultatifs' : [
                    "maux de tête",
                    "douleurs musculaires",
                    "douleurs articulaires",
                    "faiblesses",
                    "irritation de la gorge",
                    "douleurs abdominales"
                ],
                'grave' : [
                    "toux",
                    "éruption cutanée",
                    "douleurs thoraciques",
                    "yeux rouges",
                    "insuffisance rénale et hépatique",
                    "hémorragies internes et externes"
                ]
            },
            'moyen_de_propagation': [
                "contact de fluide corporel"
            ],
            
        }
        ] 
    data['SIDA'] = [
        {
            'nom': 'SIDA',
            'r0': 0.19,
            'taux_de_letalite': [0.5,1],
            'agent_pathogenes' : 'VIH',
            'mesures_de_lutte': [
                "les préservatifs masculins et féminins",
                "l’administration de médicaments antirétroviraux en guise de prophylaxie préexposition (PPrE)",
                "la circoncision masculine médicale volontaire",
                "les interventions en faveur des changements de comportement pour la limitation du nombre de partenaires sexuels",
                " l’emploi d’aiguilles et de seringues propres",
            
            ],
            'sympthômes': {
                "net" : [
                    "une fièvre de plus de 38 °C ",
                    "l'apparition de ganglions lymphatiques",
                    "une pharyngite",
                    "une éruption de plaques rouges sur le corps et le visage",
                    "des maux de tête, de ventre, des douleurs musculaires",
                    "Courbatures et douleurs musculaires",
                    "une diarrhée, des vomissements",
                    "une perte de poids",
                    "des ulcérations de la bouche ou des organes génitaux ",
                   
                ]
            },
            'moyen_de_propagation': [
                "pénétration (anale ou vaginale) lors d’un rapport sexuel",
                "transfusion sanguine",
                "partage d’aiguilles contaminées",
                "de la mère à l’enfant au cours de la grossesse, de l’accouchement et de l’allaitement",
            ]
        },

        ]
    data['CHOLERA'] = [
       
        {
            'nom': 'CHOLERA',
            'ro': 2,
            'taux_de_letalite': 53.56,
            'agent_pathogenes' : 'bacille Vibrio cholerae. ',
            'mesures_de_lutte': [
                "Se laver les mains régulièrement à l’eau et au savon",
                "Eviter le contact avec des personnes malades, qui doivent être mis en quarantaine",
                "le traitement des eaux usées",
                "la construction de latrines dans les zones de regroupement humains isolées des points d'eau potable",
                "l'hygiène alimentaire",
                
            ],
            'sympthome': {
                'net' : [
                    "une diarrhée aqueuse abondante, mais sans douleur (selles riziformes)",
                    "des vomissements de liquide clair",
                    "des nausées.",
                ],
                
            },
            'moyen_de_propagation': [
                "en ingérant de l'eau contaminée",
                "en ingérant des aliments contaminés",
                "en ingérant de manière non intentionnelle les selles d'une personne infectée."
            ],
            
        }
        ]
    data['Tuberculose'] = [
        {
            'nom': 'TUBERCULOSE',
            'ro': 3,
            'taux_de_letalite': [5,7],
            'agent_pathogenes' : 'Mycobacterium tuberculosis',
            'mesures_de_lutte': [
                "La vaccination par le BBCG",
                "Isolement des patients contagieux"
            ],
            'sympthômes': {
                "net" : [
                    "La Toux",
                    "des douleurs thoraciques",
                    "Un etat de faiblesse",
                    "Une perte de poids",
                    "La fievre",
                    "des sueurs nocturnes",
                ]
            },
            'moyen_de_propagation': [
                "aérien"
            ]
        },

        ] 
    data['FIEVRE JAUNE'] = [
        {
            'nom': 'FIEVRE JAUNE',
            'r0': 3,
            'taux_de_letalite': [2,6],
            'agent_pathogenes' : 'arbovirus',
            'mesures_de_lutte': [
                " la prévention par vaccination",
                " le repos, la réhydratation et l’administration de médicaments visant à limiter la fièvre, les vomissements et la douleur",
            
            ],
            'sympthômes': {
                "net" : [
                    "fièvre, frissons, douleurs musculaires et maux de tête",
                    "une grippe, une dengue ou un paludisme",
                    " l’apparition d’un syndrome hémorragique avec vomissement de sang noirâtre",
                    "un ictère qui donne son nom à la maladie et de troubles rénaux",
                   
                ]
            },
            'moyen_de_propagation': [
                "piqûre de moustiques appartenant aux genres Aedes et Haemagogus",
            ]
        },

        ] 
    data['ROUGEOLE'] = [
       
        {
            'nom': 'ROUGEOLE',
            'ro': 18,
            'taux_de_letalite': [10],
            'agent_pathogenes' : 'virus de la famille de Paramyxoviridae. ',
            'mesures_de_lutte': [
                " le vaccin rougeole-oreillons-rubéole (ROR) ",
            ],
            'sympthome': {
                'net' : [
                    "fièvre, toux",
                    "écoulement nasal",
                    "yeux rouges",
                    "somnolence",

                ],
                
            },
            'moyen_de_propagation': [
                "se transmet très facilement par la toux",
                "se transmet par les éternuements et les sécrétions nasales"
                ],
            
        }
        ]
    
    
    ## cette classmethode crée et ecrit la structure d'enregistrement de donnée dans le 
    ## fichier json nommé "donnees.json"
    @classmethod
    def create_json_file(cls):
        with open('donnees.json', 'w') as fp:
            json.dump(cls.data, fp, indent=4,ensure_ascii=False)

    ## cette classmethode retourne tous les ocurence stoké dans le json d'une epidémie donné en parametre
    @classmethod
    def all(cls,type):
        with open('donnees.json') as fp:
            cls.data = json.load(fp)
        return cls.data[type]

    ## cette classmethode retourne tous les epidemies
    @classmethod
    def alls(cls):
        with open('donnees.json') as fp:
            cls.data = json.load(fp)
        return cls.data

    ## cette classmethode enregistre les epidémies  a l'endroit approprié grace au type et a l'objet 
    @classmethod
    def enregistrer(cls,e,type):

        with open('donnees.json') as fp:
            cls.data = json.load(fp)
            cls.data[type].append(e.__dict__)

        with open('donnees.json', 'w') as fp:
            json.dump(cls.data, fp, indent=4,ensure_ascii=False)
    ## cette classmethode enregistre les epidémies  a l'endroit approprié grace au type  et a un dictionnaire
    @classmethod
    def enregistrer2(cls,e,type):
        with open('donnees.json') as fp:
            cls.data = json.load(fp)
            cls.data[type].append(e)

        with open('donnees.json', 'w') as fp:
            json.dump(cls.data, fp, indent=4,ensure_ascii=False)
            
    ## cette classmethode enregistre une nouvelle epidemie elle prend en parametre un dictionnaire et le nom de l'epidémie        
    @classmethod
    def add(cls,e,type):
        with open('donnees.json') as fp:
            cls.data = json.load(fp)
            cls.data[type] = [e]
     
        with open('donnees.json', 'w') as fp:
            json.dump(cls.data, fp, indent=4,ensure_ascii=False)

class Personne():
    def __init__(self,nom,prenom,age,adresse):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse

    @classmethod
    def all(cls):
        return Epidemiologie.all("Personne")

    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls, e):
        Epidemiologie.enregistrer(e,"Personne") 

    def delete(self):
        del self

class Patient(Personne):
    
    def __init__(self,nom, prenom, age, adresse, sympthome = [], diagnostic = [], traitement = []):
        super().__init__(nom, prenom, age, adresse)
        self.sympthome = sympthome
        self.diagnostic = diagnostic
        self.traitement = traitement
        self.date = str(datetime.now())

    
    
    @classmethod
    def all(cls):
        return Epidemiologie.all("Patient")
    
    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls, e):
        Epidemiologie.enregistrer(e,"Patient") 

    def delete(self):
        del self  

class Covid():

    Covid = [
        {
            'nom': 'COVID-19',
            'ro': 3,
            'taux_de_letalite': [0.5,1],
            'agent_pathogenes' : 'SARS-Cov-2',
            'mesures_de_lutte': [
                "se laver régulièrement les mains ou utiliser une solution hydro-alcoolique",
                "tousser ou éternuer dans son coude ou dans un mouchoir",
                "se moucher dans un mouchoir à usage unique puis le jeter",
                "éviter de se toucher le visage",
                "respecter une distance d'au moins deux mètres avec les autres",
                "saluer sans serrer la main et arrêter les embrassades",
                "porter un masque chirurgical ou en tissu de catégorie 1 quand la distance de deux mètres ne peut pas être respectée",
                "limiter au maximum ses contacts sociaux (6 personnes maximum)",
                "aérer les pièces le plus souvent possible, au minimum quelques minutes toutes les heures",
                "utiliser les outils numériques (application Tous anti-Covid)"
            ],
            'sympthômes': {
                "net" : [
                    "La fièvre",
                    "La toux sèche",
                    "Essoufflements",
                    "Perte de l'odorat, perte du goût",
                    "La fatigue",
                    "Courbatures et douleurs musculaires",
                    "Diarrhées, nausées",
                    "Maux de gorge",
                    "Maux de tête",
                    "Conjonctivite, yeux irrités",
                    "Eruptions cutanées",
                    "Douleurs thoraciques"
                ]
            },
            'moyen_de_propagation': [
                "aérien"
            ]
        },

        ] 

    def __init__(self,nom,ro,taux_de_letalite = '',agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = []):
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
        self.date = str(datetime.now())
    
    def __str__(self):
        return "nom :" + self.nom + " ro : " + self.ro + " taux_de_letalite : " + self.taux_de_letalite + " agent_pathogenes : " + self.agent_pathogenes + " mesures de luttes : " + self.mesures_de_lutte + " sympthome : " + self.sympthome + " moyen de propagation : " + self.moyen_de_propagation
   
    # retourne toute les épidémie de covid
    @classmethod
    def all(cls):
        return Epidemiologie.all("Covid")
    
    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls, e):
        Epidemiologie.enregistrer(e,"Covid") 

    def delete(self):
        del self

class CHOLERA():

    Cholera = [
       
        {
            'nom': 'CHOLERA',
            'ro': 2,
            'taux_de_letalite': 53.56,
            'agent_pathogenes' : 'bacille Vibrio cholerae. ',
            'mesures_de_lutte': [
                "Se laver les mains régulièrement à l’eau et au savon",
                "Eviter le contact avec des personnes malades, qui doivent être mis en quarantaine",
                "le traitement des eaux usées",
                "la construction de latrines dans les zones de regroupement humains isolées des points d'eau potable",
                "l'hygiène alimentaire",
                
            ],
            'sympthome': {
                'net' : [
                    "une diarrhée aqueuse abondante, mais sans douleur (selles riziformes)",
                    "des vomissements de liquide clair",
                    "des nausées.",
                ],
                
            },
            'moyen_de_propagation': [
                "en ingérant de l'eau contaminée",
                "en ingérant des aliments contaminés",
                "en ingérant de manière non intentionnelle les selles d'une personne infectée."
            ],
            
        }
        ] 

    def __init__(self,nom,ro,taux_de_letalite = '',agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = [],periode = {}):
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
        self.periode=periode
        self.date = str(datetime.now())
        
        def __str__(self):
            return "nom :" + self.nom + " ro : " + self.ro + " taux_de_letalite : " + self.taux_de_letalite + " agent_pathogenes : " + self.agent_pathogenes + " mesures de luttes : " + self.mesures_de_lutte + " sympthome : " + self.sympthome + " moyen de propagation : " + self.moyen_de_propagation
    
    # retourne toute les épidémie de covid
    @classmethod
    def all(cls):
        return Epidemiologie.all("CHOLERA")

    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls,e):
        Epidemiologie.enregistrer(e,"CHOLERA")

    def delete(self):
        del self

class Ebola():

    Ebola = [
       
        {
            'nom': 'EBOLA',
            'ro': 2,
            'taux_de_letalite': 53.56,
            'agent_pathogenes' : 'Ebola',
            'mesures_de_lutte': [
>>>>>>> Stashed changes
                "Se laver les mains régulièrement à l’eau et au savon",
                "Eviter d'être en contact avec des personnes malades, qui doivent être mis en quarantaine",
                "Il ne faut pas toucher, embrasser ou même laver une personne malade",
                "Les soignants doivent porter blouses, gants, masques et lunettes. Et ne pas réutiliser les seringues",
                "Une attention particulière doit être portée lors des rites funéraires puisque les personnes décédées sont encore porteuses du virus et peuvent être contagieux",
                "Apprendre à ne pas porter sa main à sa bouche ou à ses yeux, portes d’entrées du virus",
                "Porter des gants et vêtements de protection pour manipuler les animaux malades et leur chair",
                "Rester vigilants chez les malades guéris qui peuvent encore transmettre le virus pendant 7 semaines. Ils doivent éviter les relations sexuelles pendant ce temps ou utiliser un préservatif."
            ],
            'sympthome': {
                'net' : [
                    "L’apparition brutale d'une fièvre intense, accompagnée de frissons",
                    "Une diarrhée",
                    "Des vomissements",
                    "Une fatigue extrêmement intense",
                    "Une perte d’appétit importante (anorexie)"
                ],
                'facultatifs' : [
                    "maux de tête",
                    "douleurs musculaires",
                    "douleurs articulaires",
                    "faiblesses",
                    "irritation de la gorge",
                    "douleurs abdominales"
                ],
                'grave' : [
                    "toux",
                    "éruption cutanée",
                    "douleurs thoraciques",
                    "yeux rouges",
                    "insuffisance rénale et hépatique",
                    "hémorragies internes et externes"
                ]
            },
            'moyen_de_propagation': [
                "contact de fluide corporel"
            ],
<<<<<<< Updated upstream
            'soin': {
                'soins symptomatiques' : [
                    "maintenir une tension artérielle convenable",
                    "lutter contre les pertes sanguines",
                    "fournir de l'oxygène si nécessaire",
                    "réhydrater"
                ]
            }
        }
        ] 

    def __init__(self,nom,ro,taux_de_letalite = 0,agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = []):
=======
            
        }
        ] 

    def __init__(self,nom,ro,taux_de_letalite = '',agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = []):
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
        self.date = str(datetime.now())

    def __str__(self):
        return "nom :" + self.nom + " ro : " + self.ro + " taux_de_letalite : " + self.taux_de_letalite + " agent_pathogenes : " + self.agent_pathogenes + " mesures de luttes : " + self.mesures_de_lutte + " sympthome : " + self.sympthome + " moyen de propagation : " + self.moyen_de_propagation
    
    # retourne toute les épidémie de covid
    @classmethod
    def all(cls):
        return Epidemiologie.all("Ebola")

    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls,e):
        Epidemiologie.enregistrer(e,"Ebola")

    def delete(self):
        del self

class FIEVRE_JAUNE():

    Fievre_jaune = [
        {
            'nom': 'FIEVRE JAUNE',
            'r0': 3,
            'taux_de_letalite': [2,6],
            'agent_pathogenes' : 'arbovirus',
            'mesures_de_lutte': [
                " la prévention par vaccination",
                " le repos, la réhydratation et l’administration de médicaments visant à limiter la fièvre, les vomissements et la douleur",
            
            ],
            'sympthômes': {
                "net" : [
                    "fièvre, frissons, douleurs musculaires et maux de tête",
                    "une grippe, une dengue ou un paludisme",
                    " l’apparition d’un syndrome hémorragique avec vomissement de sang noirâtre",
                    "un ictère qui donne son nom à la maladie et de troubles rénaux",
                   
                ]
            },
            'moyen_de_propagation': [
                "piqûre de moustiques appartenant aux genres Aedes et Haemagogus",
            ]
        },

        ] 

    def __init__(self,nom,ro,taux_de_letalite = '',agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = []):
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
        self.date = str(datetime.now())
        
    def __str__(self):
        return "nom :" + self.nom + " ro : " + self.ro + " taux_de_letalite : " + self.taux_de_letalite + " agent_pathogenes : " + self.agent_pathogenes + " mesures de luttes : " + self.mesures_de_lutte + " sympthome : " + self.sympthome + " moyen de propagation : " + self.moyen_de_propagation
    # retourne toute les épidémie de covid
    @classmethod
    def all(cls):
        return Epidemiologie.all("FIEVRE JAUNE")
    
    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls, e):
        Epidemiologie.enregistrer(e,"FIEVRE JAUNE") 

    def delete(self):
        del self

class ROUGEOLE():

    Rougeole = [
       
        {
            'nom': 'ROUGEOLE',
            'ro': 18,
            'taux_de_letalite': [10],
            'agent_pathogenes' : 'virus de la famille de Paramyxoviridae. ',
            'mesures_de_lutte': [
                " le vaccin rougeole-oreillons-rubéole (ROR) ",
            ],
            'sympthome': {
                'net' : [
                    "fièvre, toux",
                    "écoulement nasal",
                    "yeux rouges",
                    "somnolence",

                ],
                
            },
            'moyen_de_propagation': [
                "se transmet très facilement par la toux",
                "se transmet par les éternuements et les sécrétions nasales",            ],
            
        }
        ] 

    def __init__(self,nom,ro,taux_de_letalite = '',agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = []):
>>>>>>> Stashed changes
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
<<<<<<< Updated upstream
        self.id = self.id + 1

    @classmethod
    def all(cls):
        return cls.Epidemie
    
    @classmethod
    def find(cls, id):
        return cls.Epidemie[id-1]

    @classmethod
    def save(cls, e):
        cls.Epidemie.append(e.__dict__) 
=======
        self.date = str(datetime.now())
        
    def __str__(self):
        return "nom :" + self.nom + " ro : " + self.ro + " taux_de_letalite : " + self.taux_de_letalite + " agent_pathogenes : " + self.agent_pathogenes + " mesures de luttes : " + self.mesures_de_lutte + " sympthome : " + self.sympthome + " moyen de propagation : " + self.moyen_de_propagation
    # retourne toute les épidémie de covid
    @classmethod
    def all(cls):
        return Epidemiologie.all("ROUGEOLE")

    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls,e):
        Epidemiologie.enregistrer(e,"ROUGEOLE")

    def delete(self):
        del self

class SIDA():

    Sida = [
        {
            'nom': 'SIDA',
            'r0': 0.19,
            'taux_de_letalite': [0.5,1],
            'agent_pathogenes' : 'VIH',
            'mesures_de_lutte': [
                "les préservatifs masculins et féminins",
                "l’administration de médicaments antirétroviraux en guise de prophylaxie préexposition (PPrE)",
                "la circoncision masculine médicale volontaire",
                "les interventions en faveur des changements de comportement pour la limitation du nombre de partenaires sexuels",
                " l’emploi d’aiguilles et de seringues propres",
            
            ],
            'sympthômes': {
                "net" : [
                    "une fièvre de plus de 38 °C ",
                    "l'apparition de ganglions lymphatiques",
                    "une pharyngite",
                    "une éruption de plaques rouges sur le corps et le visage",
                    "des maux de tête, de ventre, des douleurs musculaires",
                    "Courbatures et douleurs musculaires",
                    "une diarrhée, des vomissements",
                    "une perte de poids",
                    "des ulcérations de la bouche ou des organes génitaux ",
                   
                ]
            },
            'moyen_de_propagation': [
                "pénétration (anale ou vaginale) lors d’un rapport sexuel",
                "transfusion sanguine",
                "partage d’aiguilles contaminées",
                "de la mère à l’enfant au cours de la grossesse, de l’accouchement et de l’allaitement",
            ]
        },

        ] 

    def __init__(self,nom,ro,taux_de_letalite = '',agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = []):
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
        self.date = str(datetime.now())
        
    
    # retourne toute les épidémie de covid
    @classmethod
    def all(cls):
        return Epidemiologie.all("SIDA")
    
    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls, e):
        Epidemiologie.enregistrer(e,"SIDA") 

    def delete(self):
        del self

class Tuberculose():

    Tuberculose = [
        {
            'nom': 'TUBERCULOSE',
            'ro': 3,
            'taux_de_letalite': [5,7],
            'agent_pathogenes' : 'Mycobacterium tuberculosis',
            'mesures_de_lutte': [
                "La vaccination par le BBCG",
                "Isolement des patients contagieux"
            ],
            'sympthômes': {
                "net" : [
                    "La Toux",
                    "des douleurs thoraciques",
                    "Un etat de faiblesse",
                    "Une perte de poids",
                    "La fievre",
                    "des sueurs nocturnes",
                ]
            },
            'moyen_de_propagation': [
                "aérien"
            ]
        },

        ] 

    def __init__(self,nom,ro,taux_de_letalite = '',agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = []):
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
        self.date = str(datetime.now())
    
    def __str__(self):
        return "nom :" + self.nom + " ro : " + self.ro + " taux_de_letalite : " + self.taux_de_letalite + " agent_pathogenes : " + self.agent_pathogenes + " mesures de luttes : " + self.mesures_de_lutte + " sympthome : " + self.sympthome + " moyen de propagation : " + self.moyen_de_propagation
    
    # retourne toute les épidémie de covid
    @classmethod
    def all(cls):
        return Epidemiologie.all("Tuberculose")
    
    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls, e):
        Epidemiologie.enregistrer(e,"Tuberculose") 
>>>>>>> Stashed changes

    def delete(self):
        del self



<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
    

    
