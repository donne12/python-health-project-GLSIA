class Epidemiologie():

    id = 0

    Epidemie = [
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
            'sympthome': {
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
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
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

    def delete(self):
        del self



    

    
