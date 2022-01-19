from classes import *
from personne import *
from maladie import *
from generator import Generator
import datetime

class Consultation:
    id: str
    patient: Patient()
    maladie: Maladie()
    medecin: Medecin()
    date_consultation: str
    prescriptions: []
    observations: []
    rdv: str

    def __init__(self):
        g = Generator()
        self.id = g.generate_id_formated()
        self.patient = None
        self.maladie = None
        self.medecin = None
        self.prescriptions = []
        self.observations = []
        self.date_consultation = ''
        self.rdv = ''



    def __str__(self):
        return f"ID: {self.id} \nMaladie: \n{self.maladie} \nMedécin: {self.medecin} \nDate de consultation: {self.date_consultation} \nRDV: {self.rdv}"

    # Enregistrer une consultation pour un patient dans le fichier json
    def write_consultation(self, data: Patient):
        with open('json/data.json') as myFile:
            file_data = json.load(myFile)

        cpt = 0
        for i in file_data["patients"]:
            if i["id"] == data.id:
                file_data["patients"][cpt]["consultations"] = data.consultations
                break
            cpt += 1

        with open('json/data.json', 'w', encoding='utf-8') as myFile:
            json.dump(file_data, myFile)
        myFile.close()
        print('Enregistrement réussi!!!')

    # Séléctionner le patient, médecin et la maladie participant à une consultation
    def select(self):
        data = read("patients")
        find = str(input('Le patient existe? o/n: '))
        if find == 'n':
            self.patient = Patient()
            self.patient.add()
        else:
            while self.patient is None:
                id = str(input('\n>>> L\'identifiant du patient: '))
                self.patient = Patient()
                self.patient.to_class_data(get_element(data, id))

        data = read("medecins")
        find = str(input('Le médecin existe? o/n: '))
        if find == 'n':
            self.medecin = Medecin()
            self.medecin.add()
        else:
            while self.medecin is None:
                id = str(input('\n>>> L\'identifiant du médecin: '))
                self.medecin = Medecin()
                self.medecin.to_class_data(get_element(data, id))

        data = read("maladies")
        find = str(input('La maladie existe? o/n: '))
        if find == 'n':
            self.maladie = Maladie()
            self.maladie.add()
        else:
            while self.maladie is None:
                id = str(input('\n>>> L\'identifiant de la maladie: '))
                self.maladie = Maladie()
                self.maladie.to_class_data(get_element(data, id))

    # Fonction pour ajouter une consultation
    def add(self):
        title("Ajouter une consultation")
        self.select()

        data = {
            "id": self.id,
            "medecin": self.medecin.nom + ' ' + self.medecin.prenom,
            "maladie": self.maladie.nom,
            "date consultation": str(datetime.datetime.now().date()),
            "prescriptions": str(input("Prescriptions (séparez avec des virgules): ")).split(','),
            "observations": str(input("Observations (séparez avec des virgules): ")).split(','),
            "rdv": str(input("Prochain RDV: "))
        }

        con = self.patient.consultations
        con.append(data)
        self.patient.consultations = con

        self.write_consultation(self.patient)
        self.to_class_data(data)

    # def to_class_data(self, data):
    #     self.id = data["id"]
    #     self.maladie = data["maladie"]
    #     self.medecin = data["medecin"]
    #     self.prescriptions = data["prescriptions"]
    #     self.observations = data["observations"]
    #     self.date_consultation = data["date consultation"]
    #     self.rdv = data["rdv"]
    #
    # def afficher(self):
    #     title("Une Consultation")
    #     bar = '+' + '-'*27 + '+' + '-'*49 + '+'
    #     print(bar)
    #     print('|', 'ID'.center(25), '|', self.id.center(47), '|')
    #     print(bar)
    #     print('|', 'Medécin'.center(25), '|', self.medecin.center(47), '|')
    #     print(bar)
    #     print('|', 'Maladie'.center(25), '|', self.maladie.nom.center(47), '|')
    #     print(bar)
    #     print('|', 'Observations'.center(25), '|', self.observations[0].center(47), '|')
    #     for elt in range(1, len(self.observations)):
    #         print('|', ''.center(25), '|', self.observations[elt].center(47), '|')
    #     print(bar)
    #     print('|', 'Prescriptions'.center(25), '|', self.prescriptions[0].center(47), '|')
    #     for elt in range(1, len(self.prescriptions)):
    #         print('|', ''.center(25), '|', self.prescriptions[elt].center(47), '|')
    #     print(bar)
    #     print('|', 'Date de consultation'.center(25), '|', self.date_consultation.center(47), '|')
    #     print(bar)
    #     print('|', 'rdv'.center(25), '|', self.rdv.center(47), '|')
    #     print(bar)
    #
    #
    # def update(self):
    #     title("Modifier une consuletation")
    #
    # def get(self):
    #     read("consultations")

